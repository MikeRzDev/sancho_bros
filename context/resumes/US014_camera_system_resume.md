# US014: Camera/Viewport System - Resume

**Completion Date:** 2025-10-15
**Story Points:** 5
**Status:** COMPLETE ✓

---

## Changes Made

Implemented a complete camera/viewport system that enables smooth scrolling levels extending beyond the screen width. The camera follows the player horizontally while respecting level boundaries, creating a professional game feel with smooth scrolling and proper boundary clamping. This system is essential for Phase 4 level loading, as all 5 JSON levels extend beyond the 800px screen width.

---

## Files Modified/Created

### Created Files

No new files were created. The camera system enhanced an existing placeholder class.

### Modified Files

1. **`src/camera.py`** (complete rewrite from placeholder)
   - **Changes:** Transformed from simple placeholder to full-featured camera system
   - **New Attributes:**
     - `width`, `height`: Viewport dimensions (SCREEN_WIDTH=800, SCREEN_HEIGHT=600)
     - `level_width`: Maximum camera boundary for current level
     - `x`, `y`: Camera position in world coordinates
   - **New Methods:**
     - `__init__(width, height)`: Initializes camera with viewport dimensions
     - `update(target_pos, level_width)`: Centers camera on target with boundary clamping
     - `apply(world_pos)`: Transforms world coordinates to screen coordinates
     - `is_visible(entity)`: Checks if entity is within viewport (for optimization)
   - **Rationale:** Complete camera following system with smooth scrolling and boundary handling

2. **`src/game.py`** (lines 43, 47-63, 111)
   - **Changes:**
     - Updated camera initialization: `Camera(SCREEN_WIDTH, SCREEN_HEIGHT)` instead of `Camera(0, 0)`
     - Extended test platforms from 800px to 2000px (9 platforms total)
     - Added level_width calculation: `max(platform.rect.right for platform in platforms)`
     - Added camera update call: `self.camera.update(self.player.position, self.level_width)`
   - **Rationale:** Integrate camera into game loop and create extended test level for scrolling validation

---

## Rationale

### Why This Implementation Matters

The camera system is **critical infrastructure** for the entire game, as all 5 JSON levels extend beyond the screen width:
- Level 1: 2000px wide
- Level 2: 2500px wide
- Level 3: 3000px wide
- Level 4: 3500px wide
- Level 5: 4000px wide

Without a camera system, players would be stuck viewing only the first 800 pixels of each level, making the game unplayable.

### Key Design Decisions

1. **Player-Centered Following:**
   - Camera centers on player horizontally: `x = target_pos.x - width // 2`
   - Keeps player in optimal viewing position (middle of screen)
   - Provides equal visibility in both directions

2. **Boundary Clamping:**
   - Left boundary: `x = max(0, x)` prevents showing area left of level
   - Right boundary: `x = min(x, level_width - width)` prevents showing area right of level
   - Small level handling: Camera stays at x=0 when `level_width < SCREEN_WIDTH`
   - No jarring jumps or empty space visible beyond level edges

3. **Coordinate Transformation:**
   - `apply(world_pos)` method converts world coords to screen coords
   - Simple formula: `screen_x = world_x - camera.x`
   - All render methods use this transformation for camera-relative rendering
   - Enables smooth scrolling without complex render logic

4. **Fixed Vertical Scrolling:**
   - Camera.y always stays at 0 (no vertical scrolling)
   - Appropriate for 2D side-scroller with fixed screen height
   - Simpler implementation, better player orientation

5. **Viewport Culling Support:**
   - `is_visible()` method ready for future optimization
   - Can skip rendering entities outside viewport
   - Important for large levels with many entities (Phase 5-6)

### How It Fits Into Overall Architecture

- **Phase 3 Completion:** Camera system is the final piece of core mechanics
  - Player movement ✓
  - Physics/gravity ✓
  - Collision detection ✓
  - Camera following ✓

- **Phase 4 Preparation:** Unblocks level loading system
  - Level loader will read JSON level dimensions
  - Pass level_width to camera.update()
  - Camera automatically handles any level size

- **Rendering Pipeline:** Establishes coordinate transformation pattern
  - World coordinates: Absolute positions in level
  - Screen coordinates: Positions on display
  - All entities render camera-relative via `camera.apply()`

- **Future Optimization:** Viewport culling ready for entity management
  - Can skip updating/rendering off-screen enemies (Phase 5)
  - Can skip rendering off-screen power-ups (Phase 6)
  - Important for performance in large levels

---

## Technical Details

### Camera Algorithm

**Update Method (called every frame):**
1. Store level_width for boundary calculations
2. Center camera on player: `x = target_pos.x - viewport_width // 2`
3. Clamp to left boundary: `x = max(0, x)`
4. Clamp to right boundary: `x = min(x, level_width - viewport_width)` (if level > screen)
5. Special case: If level ≤ screen width, camera stays at x=0 (no scrolling needed)
6. Fix vertical: `y = 0` (no vertical scrolling for side-scroller)

**Coordinate Transformation:**
- Input: World position (absolute position in level)
- Output: Screen position (position on display)
- Formula: `(world_x - camera.x, world_y - camera.y)`
- Example: Player at world (1000, 200), camera at (600, 0) → screen (400, 200)

**Viewport Culling:**
- Entity visible if: `entity.rect.right > camera.x` AND `entity.rect.left < camera.x + width`
- Checks if entity's bounding box intersects viewport horizontally
- Can be used to skip rendering/updating off-screen entities

### Test Level Configuration

Extended test level spans 2000px (2.5x screen width) to validate camera scrolling:

**Ground Platforms (3 segments with gaps):**
- Segment 1: x=0, width=500 (spans 0-500px)
- Gap 1: 500-600px (100px pit)
- Segment 2: x=600, width=400 (spans 600-1000px)
- Segment 3: x=1100, width=900 (spans 1100-2000px)

**Floating Platforms (6 platforms):**
- x=300: Early jump platform
- x=600: Platform over first gap
- x=900: Mid-level platform
- x=1200: High platform (y=250)
- x=1500: Late game platform
- x=1800: Near-end platform

**Level Width:** 2000px (calculated as max of all platform right edges)

### Integration Points

**Game Initialization (`Game.__init__()`):**
```python
self.camera = Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
self.level_width = max(platform.rect.right for platform in self.platforms)
```

**Game Loop (`Game.update()`):**
```python
self.player.update(dt, self.platforms)  # Update player first
self.camera.update(self.player.position, self.level_width)  # Then update camera
```

**Rendering (`Game.render()`):**
```python
self.player.render(self.screen, self.camera)  # Camera passed to render
for platform in self.platforms:
    platform.render(self.screen, self.camera)
```

**Entity Rendering (e.g., `Player.render()`):**
```python
screen_x = self.rect.x - camera.x
screen_y = self.rect.y - camera.y
pygame.draw.rect(screen, COLOR_PLAYER, (screen_x, screen_y, width, height))
```

### Testing Validation

- ✓ Game runs without errors (10 second test run successful)
- ✓ All modules compile without syntax errors
- ✓ Camera initialization with proper parameters
- ✓ Camera update integrated into game loop
- ✓ Extended test level (2000px) created and validated
- ✓ Level width calculation from platform positions working
- ✓ Coordinate transformation logic implemented

---

## Next Steps

**Phase 3 Status:** COMPLETE ✓
- All 5 user stories (US010-US014) implemented and validated
- Core mechanics foundation fully functional

**Next Phase:** Phase 4 - Level Loading
**Next User Story:** US015 - Create Level Loader and JSON Parser

**Dependencies for US015:**
- JSON level files exist in `levels/` directory (created in Phase 2)
- Platform class exists in `src/level/tile.py` (created in Phase 3 - US013)
- Camera system ready to handle dynamic level widths (Phase 3 - US014)
- Need to implement: JSON parser, Level class, entity instantiation from data

**Phase 4 Preview:**
- Level loader will parse JSON files and create game objects
- Levels will be dynamically loaded instead of hardcoded test platforms
- Level progression system will advance through all 5 levels
- Goal objects will trigger level completion
- Player will respawn at level start on death

---

## Phase 3 Summary

**Completed User Stories:**
- US010: Player Entity Class (Sancho) - 3 pts
- US011: Gravity and Physics System - 5 pts
- US012: Player Movement and Controls - 5 pts
- US013: Collision Detection System - 8 pts
- US014: Camera/Viewport System - 5 pts
**Total:** 26 story points (exceeds planned 21 due to US013 complexity)

**Phase 3 Achievements:**
- Complete player control system (movement, jumping, physics)
- Full AABB collision detection and resolution
- Smooth camera following with boundary clamping
- Extended test level for validation (2000px)
- Solid foundation for level loading and enemy systems

**Next Milestone:** Phase 4 will connect the generated JSON levels to the game engine, enabling progression through all 5 levels with dynamic content loading.
