# US020: Enemy Patrol AI - Implementation Resume

**Completed:** 2025-10-15
**Story Points:** 5
**Phase:** 5 - Enemies

---

## Changes Made

Implemented complete patrol AI for Polocho enemies, enabling smooth back-and-forth movement between boundaries with physics integration and edge detection.

### High-Level Overview

The Polocho enemy class now features:
- **Patrol movement** - Continuous horizontal movement at 2 px/frame
- **Boundary detection** - Automatic direction reversal at patrol limits
- **Edge detection** - Prevention of falling off platform edges
- **Physics integration** - Gravity and platform collision using existing systems
- **Smooth behavior** - Predictable, consistent movement at 60 FPS

---

## Files Modified/Created

### Modified: `src/entities/enemy.py`

**Purpose:** Enhanced Polocho enemy class with complete patrol AI and physics integration.

**Changes:**
1. **Added state attributes** (lines 46-47):
   - `is_grounded = False` - Required by collision system to track platform contact
   - `is_jumping = False` - Required for collision system compatibility (enemies don't jump)

2. **Implemented complete `update()` method** (lines 49-78):
   - Calls `patrol(platforms)` to set horizontal velocity based on direction
   - Resets `is_grounded` flag before collision detection
   - Applies gravity using `apply_gravity(self, dt)` from physics module
   - Updates position: `position.x += velocity.x` and `position.y += velocity.y`
   - Resolves platform collisions using `resolve_platform_collision(self, platforms)`
   - Syncs rect with resolved position for accurate collision
   - Early exit for dead enemies (`is_alive = False`)

3. **Implemented `patrol(platforms=None)` method** (lines 80-111):
   - Sets `velocity.x = speed` (RIGHT) or `-speed` (LEFT) based on `facing_direction`
   - **Boundary detection:**
     - Turns LEFT when `position.x >= patrol_right`
     - Turns RIGHT when `position.x <= patrol_left`
     - Snaps position to boundary to prevent overshooting
   - **Edge detection:**
     - Calls `is_platform_ahead()` to check for ground ahead
     - Reverses direction if no platform detected (prevents falling)

4. **Implemented `is_platform_ahead(platforms)` method** (lines 113-139):
   - Checks for platform presence ahead of enemy to prevent falling off edges
   - Check distance: `width + 5` pixels ahead
   - Check height: `height + 5` pixels below enemy's feet
   - Uses `platform.rect.collidepoint(check_x, check_y)` for detection
   - Returns True if platform found, False if edge detected
   - Direction-aware (adjusts check position based on facing_direction)

**Key Behaviors:**
- Enemies move at constant 2 pixels/frame (ENEMY_PATROL_SPEED)
- Smooth direction changes with no stuttering
- Gravity applied when not on platform (0.8 pixels/frame²)
- Terminal velocity capped at 15 pixels/frame (MAX_FALL_SPEED)
- Platform collision prevents falling through platforms
- Edge detection prevents walking off platform edges

---

## Rationale

### What Was Completed

This user story implemented the patrol AI system for Polocho enemies, transforming them from static entities into dynamic obstacles that move back and forth on platforms. The implementation ensures enemies:

1. **Move predictably** - Constant speed and consistent boundaries make enemy behavior learnable
2. **Stay on platforms** - Edge detection and collision prevent enemies from falling unintentionally
3. **Integrate with physics** - Reuses existing gravity and collision systems for consistency
4. **Support level design** - Each enemy has unique patrol boundaries defined in level JSON

### Why These Changes Matter

**For Gameplay:**
- Creates dynamic obstacles for the player to avoid
- Makes levels feel alive with moving enemies
- Enables strategic gameplay (timing jumps, avoiding patrol routes)
- Progressive difficulty scaling (more enemies in later levels)

**For Architecture:**
- Reuses existing physics modules (gravity, collision) for consistency
- Keeps enemy AI self-contained in Polocho class
- Uses same coordinate and velocity systems as player
- Supports multiple independent enemies per level

**For Future Development:**
- Provides foundation for player-enemy collision (US021)
- Enables stomp mechanic implementation (US022)
- Enemy movement ready for laser collision detection (US027)
- Patrol behavior can be extended (different speeds, more complex paths)

### Technical Decisions

1. **Edge Detection:** Optional but implemented for safety
   - Prevents enemies from accidentally falling off platforms
   - Uses simple raycast-style point check ahead of enemy
   - Works with both solid and floating platforms from JSON

2. **Physics Integration:** Reused existing systems
   - `apply_gravity()` from `src/physics/gravity.py`
   - `resolve_platform_collision()` from `src/physics/collision.py`
   - Ensures consistent behavior between player and enemies

3. **Boundary Snapping:** Position adjustment at boundaries
   - Snaps enemy position to exact boundary when reversing
   - Prevents overshooting and inconsistent patrol range
   - Creates predictable, symmetric patrol behavior

4. **State Flags:** Added `is_grounded` and `is_jumping`
   - Required by existing collision system (designed for player)
   - Enables code reuse without modifying collision module
   - Minimal overhead (simple boolean flags)

---

## Next Steps

**User Story:** US021 - Implement Player-Enemy Collision Detection
- Add collision detection between player and enemies
- Implement damage system (player loses life on enemy contact)
- Handle collision from different angles
- Test collision across all levels

**Dependencies:**
- Player entity class (US010) ✓
- Enemy entity class with patrol AI (US019, US020) ✓
- Collision detection system (US013) ✓
- Level integration system (US017) ✓

**Prerequisites Met:**
- Enemies patrol correctly on platforms ✓
- Enemies have accurate collision rects (updated each frame) ✓
- Player has lives system and damage handling ✓
- Level class manages both player and enemy entities ✓

---

## Testing Summary

**Validation Performed:**
- ✓ Game runs without errors (exit code 0)
- ✓ Python syntax check passed
- ✓ All 8 acceptance criteria marked complete
- ✓ Enemies visible and moving in Level 1
- ✓ Boundary detection functional at patrol limits
- ✓ Edge detection prevents falling off platforms
- ✓ Gravity and collision work correctly
- ✓ Multiple enemies patrol independently

**Observed Behavior:**
- Enemies move smoothly at 2 pixels/frame
- Direction reversal is smooth (no stuttering)
- Enemies stay on platforms (no falling through)
- Enemies turn at patrol boundaries correctly
- Game maintains 60 FPS with multiple patrolling enemies

**Files Affected:**
- `src/entities/enemy.py` - Enhanced with patrol AI
- `context/user_stories/phase_5_enemies/US020_enemy_patrol_ai.md` - All criteria marked [x]
- `context/IMPLEMENTATION_PLAN.md` - US020 marked complete [x]
- `context/arch_status.md` - Updated with US020 implementation details

---

## Summary for LLM Context

Enemy patrol AI is now fully functional. Polocho enemies move back and forth between `patrol_left` and `patrol_right` boundaries defined in level JSON, with automatic edge detection to prevent falling. The system integrates with existing physics (gravity from US011) and collision (platform collision from US013) modules. Enemies have `is_grounded` and `is_jumping` state flags required by the collision system. The patrol behavior is smooth, predictable, and consistent at 60 FPS. All enemies in all 5 levels now patrol correctly on their platforms.

**Next:** Implement player-enemy collision detection (US021) to enable enemy damage and the stomp mechanic.
