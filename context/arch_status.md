# ARCHITECTURE STATUS

**Last Updated:** 2025-10-15
**Current Development Phase:** Phase 4 - Level Loading (COMPLETE)

---

## Current Project Structure

```
sancho_bros/
   .gitignore                     # Python/macOS/IDE gitignore configuration
   README.md                      # Project overview and setup instructions
   requirements.txt               # Python dependencies (pygame>=2.0.0)
   CLAUDE.md                      # Project documentation and guidelines
   venv/                          # Python virtual environment (excluded from git)
   src/                           # Source code directory
      __init__.py
      main.py                    # Game entry point
      game.py                    # Main Game class with game loop
      constants.py               # Game configuration constants
      camera.py                  # Camera system (placeholder for US014)
      entities/                  # Player, enemies, power-ups, projectiles
         __init__.py
         player.py               # Player entity class (Sancho)
      level/                     # Level loading and management
         __init__.py
         tile.py                 # Platform class for collision and rendering
         level_loader.py         # JSON level file loader with validation
         level.py                # Level class for game management
      physics/                   # Collision detection and gravity
         __init__.py
         gravity.py              # Gravity physics system
         collision.py            # AABB collision detection and resolution
      ui/                        # Menus and HUD
         __init__.py
      utils/                     # Utility functions
          __init__.py
   tools/                         # Development tools
      level_generator.py         # Level generator tool
   levels/                        # JSON level files
      level_1.json               # Level 1 data (2000px, tutorial)
      level_2.json               # Level 2 data (2500px)
      level_3.json               # Level 3 data (3000px)
      level_4.json               # Level 4 data (3500px)
      level_5.json               # Level 5 data (4000px, maximum challenge)
   assets/                        # Game assets
      sprites/                   # Sprite images
         sancho/               # Player sprites
         polocho/              # Enemy sprites
         tiles/                # Platform/tile sprites
         items/                # Power-up sprites
      sounds/                    # Sound effects
      music/                     # Background music
   context/                       # Implementation documentation
       IMPLEMENTATION_PLAN.md    # User story tracking
       arch_status.md            # This file (technical state)
       game_implementation.md    # Detailed implementation guide
       problem_description.md    # Original requirements
       task_execution.md         # Execution workflow
       resumes/                  # User story completion summaries
       user_stories/             # Individual user story files
           phase_*_*/            # User stories organized by phase
```

---

## Development Environment

### Python Environment
- **Python Version:** 3.13.3
- **Virtual Environment:** `venv/` directory (excluded from version control)
- **Dependency Management:** `requirements.txt` with flexible versioning (`pygame>=2.0.0`)

### Installed Dependencies
- **Pygame:** 2.6.1 (SDL 2.28.4)
  - Verified compatible with Python 3.13.3
  - All core modules tested and functional (display, events, drawing, collision, clock, font)
  - Pre-built wheels available for macOS ARM64

---

## Architecture Overview

### Core Game Loop
The game uses a centralized Game class (`src/game.py`) that manages:
- **Initialization**: Pygame setup, window creation (800x600), display settings
- **Main Loop**: 60 FPS game loop using `pygame.time.Clock()`
- **Event Handling**: Input processing (ESC key, window close)
- **Update Cycle**: Frame-independent updates using delta time
- **Render Cycle**: Screen clearing and entity rendering

### Modular Package Structure
The codebase follows a clean separation of concerns:

- **src/main.py**: Entry point that instantiates and runs the Game
- **src/game.py**: Main Game class containing the game loop and state management
- **src/constants.py**: Centralized game configuration
- **src/entities/**: Game objects (Player, Enemy, PowerUp, Projectile classes)
- **src/level/**: Level loading system and JSON parsing
- **src/physics/**: Collision detection and gravity systems
- **src/ui/**: User interface components (menus, HUD)
- **src/utils/**: Shared utility functions

### Asset Organization
Assets are organized by type for easy management:
- **sprites/**: Visual assets with subdirectories per entity type
- **sounds/**: Sound effect files
- **music/**: Background music files

### Development Tools
- **tools/**: Contains level generator and other development utilities

---

## Technical Decisions

### Dependency Management
- Using Python virtual environments for isolation (PEP 668 compliance)
- Flexible pygame versioning (`>=2.0.0`) supports Python 3.8 through 3.13+
- README documents full setup process for developer onboarding

### Code Organization
- All Python packages have `__init__.py` for proper module imports
- Modular architecture enables independent development of game systems
- Clear separation between game logic, rendering, and data management

### Game Constants Configuration
The `src/constants.py` file centralizes all game configuration values:
- **Screen constants**: 800x600 resolution at 60 FPS
- **Physics constants**: Gravity (0.8), jump strength (-15), player speed (5), max fall speed (15)
- **Game rules**: 3 starting lives, 10-second laser duration, 0.5-second cooldown
- **Entity dimensions**: Player (40x60), Enemy (40x50), Platform (100x20 default), Power-up (30x30), Laser (10x4)
- **Color constants**: RGB tuples for placeholder graphics (player blue, enemy red, platforms brown/gray, power-up gold, laser cyan)
- **AI constants**: Enemy patrol speed (2 pixels/frame)

All constants follow UPPER_SNAKE_CASE naming convention and can be imported via `from src.constants import *`.

---

## Current State

### What Exists
- ✓ Complete directory structure
- ✓ Python virtual environment configured
- ✓ Pygame 2.6.1 installed and verified
- ✓ All package directories initialized
- ✓ Development documentation in place
- ✓ Game constants configuration (`src/constants.py`)
- ✓ Main game loop and window initialization (`src/main.py`, `src/game.py`)
- ✓ Basic game state management (running/stopped states)
- ✓ 60 FPS game loop with delta time calculation
- ✓ Event handling system (ESC key, window close)
- ✓ Level generator tool (`tools/level_generator.py`) - COMPLETE
- ✓ 5 complete JSON level files with all game elements (Phase 2 - US005-US009)
- ✓ Platform generation logic with ground and floating platforms (Phase 2 - US006)
- ✓ Pit placement logic with proper spacing and validation (Phase 2 - US006, US008)
- ✓ Enemy placement logic with patrol routes (Phase 2 - US007)
- ✓ Power-up placement logic with strategic positioning (Phase 2 - US008)
- ✓ Complete level JSON generation validated (Phase 2 - US009)
- ✓ Player entity class with all core attributes and methods (Phase 3 - US010)
- ✓ Camera placeholder system for rendering offsets (Phase 3 - US010)
- ✓ Player rendering as blue rectangle (Phase 3 - US010)
- ✓ Player integrated into main game loop (Phase 3 - US010)
- ✓ Gravity physics system with terminal velocity (Phase 3 - US011)
- ✓ Player jump mechanics (Phase 3 - US011)
- ✓ Basic platform collision detection for grounded state (Phase 3 - US011)
- ✓ Physics integrated into player update loop (Phase 3 - US011)
- ✓ Player horizontal movement controls (LEFT/RIGHT, A/D keys) (Phase 3 - US012)
- ✓ Direction tracking (facing_direction) (Phase 3 - US012)
- ✓ Complete input handling system in handle_input() method (Phase 3 - US012)
- ✓ Smooth movement at 60 FPS (Phase 3 - US012)
- ✓ Jump key press detection (requires release/repress) (Phase 3 - US012)
- ✓ AABB collision detection system (Phase 3 - US013)
- ✓ Platform collision resolution (top, bottom, left, right) (Phase 3 - US013)
- ✓ Platform class with rendering and collision (Phase 3 - US013)
- ✓ Side collision detection (wall blocking) (Phase 3 - US013)
- ✓ Proper grounded state management via collision system (Phase 3 - US013)
- ✓ Camera system with smooth player following (Phase 3 - US014)
- ✓ Camera boundary clamping (prevents showing empty space) (Phase 3 - US014)
- ✓ Coordinate transformation system (world to screen coords) (Phase 3 - US014)
- ✓ Viewport culling support (is_visible method) (Phase 3 - US014)
- ✓ Extended test level (2000px) for camera scrolling validation (Phase 3 - US014)
- ✓ Level Loader system with JSON parsing and validation (Phase 4 - US015)
- ✓ Comprehensive level data validation (all fields, types, bounds) (Phase 4 - US015)
- ✓ Error handling for missing/corrupted level files (Phase 4 - US015)
- ✓ Tested loading of all 5 generated level files (Phase 4 - US015)
- ✓ Level class for complete game management (Phase 4 - US016)
- ✓ Level initialization from JSON data with Platform object creation (Phase 4 - US016)
- ✓ Pit detection and goal detection systems (Phase 4 - US016)
- ✓ Level rendering with background, platforms, and goal indicator (Phase 4 - US016)
- ✓ Level entity management methods (update, render, reset, getters) (Phase 4 - US016)
- ✓ Game loop integration with level loading system (Phase 4 - US017)
- ✓ Level management system (load_level, load_next_level, respawn_player methods) (Phase 4 - US017)
- ✓ Player spawning at level-defined spawn positions (Phase 4 - US017)
- ✓ Win condition detection with level progression (Phase 4 - US017)
- ✓ Lose condition detection with life system and respawning (Phase 4 - US017)
- ✓ Game over handling when lives reach 0 (Phase 4 - US017)
- ✓ All 5 levels playable in sequence (Phase 4 - US017)

### What's Pending
- Phase 4: Comprehensive playability testing across all 5 levels (US018)
- Phase 5: Enemies (Polocho entity, AI, combat)
- Phase 6: Power-Ups (PowerUp entity, laser system)
- Phase 7: UI & Polish (Menus, HUD, game states)

---

## System Requirements

### Minimum Requirements
- Python 3.8 or higher
- Pygame 2.0 or higher

### Current Development Environment
- Python 3.13.3
- Pygame 2.6.1 (SDL 2.28.4)
- macOS (Darwin 24.6.0)

---

## Implemented Systems

### Game Loop Architecture (US004)
The core game loop is implemented in `src/game.py` with the following structure:

**Game Class Methods:**
- `__init__()`: Initializes Pygame, creates 800x600 window with title "Sancho Bros", sets up clock and running state
- `run()`: Main game loop that maintains 60 FPS, calculates delta time, and calls handle_events/update/render
- `handle_events()`: Processes pygame events (QUIT event, ESC key for exit)
- `update(dt)`: Placeholder for game state updates (receives delta time in seconds)
- `render()`: Clears screen with background color, updates display

**Entry Point (`src/main.py`):**
- Simple entry point that imports Game class and calls `game.run()`
- Follows standard Python `if __name__ == "__main__"` pattern

**State Management:**
- Boolean `self.running` flag controls game loop execution
- Clean shutdown with `pygame.quit()` when loop exits

### Level Generator Tool (US005, US006, US007)
The level generator tool creates all 5 JSON level files with progressive difficulty. Located at `tools/level_generator.py`.

**LevelGenerator Class:**
- `__init__()`: Initializes difficulty configurations for all 5 levels
- `generate_level(level_num)`: Creates complete level data structure with all required fields
- `place_platforms(level_data, difficulty)`: Platform generation with ground and floating platforms (US006 ✓)
- `place_enemies(level_data, difficulty)`: Enemy placement with patrol routes (US007 ✓)
- `place_powerups(level_data, difficulty)`: Power-up placement (to be implemented in US008)
- `create_pits(level_data, difficulty)`: Pit hazard generation (basic implementation in US006 ✓)
- `save_to_file(level_data, filename)`: Writes JSON with proper formatting
- `generate_all_levels()`: Generates all 5 levels at once

**Difficulty Configuration:**
- Level 1: 2000px wide, 2-3 enemies, 1 power-up, 1-2 pits (tutorial)
- Level 2: 2500px wide, 4-5 enemies, 1 power-up, 2-3 pits
- Level 3: 3000px wide, 6-7 enemies, 2 power-ups, 3-4 pits
- Level 4: 3500px wide, 8-9 enemies, 2 power-ups, 4-5 pits
- Level 5: 4000px wide, 10-12 enemies, 2-3 power-ups, 5-6 pits (maximum challenge)

**Platform Generation (US006):**
The `place_platforms()` method creates:
- **Ground platforms**: Solid platforms at y=550 with 50px height, split by pit gaps
- **Floating platforms**: Platforms at varying heights (200-500) with 20px height
  - Level 1: 5 floating platforms (120-150px wide) at heights 350-450
  - Level 2: 8 floating platforms (100-140px wide) at heights 300-480
  - Level 3: 12 floating platforms (80-130px wide) at heights 300-480
  - Level 4: 15 floating platforms (70-120px wide) at heights 200-500
  - Level 5: 18 floating platforms (60-110px wide) at heights 200-500
- **Progression platforms**: Special platforms near spawn (x=250) and goal to ensure completability
- **Distribution**: Platforms evenly distributed across level using segmentation
- **Validation**: No overlaps, reasonable spacing, completable paths

**Pit Generation (US006):**
The `create_pits()` method generates pit hazards:
- Pits placed in safe zones (500px from spawn, 500px from goal)
- Evenly distributed across level using segmentation
- Pit widths scale with difficulty: 80-150px (larger for higher levels)
- Ground platforms automatically split at pit locations

**Enemy Placement (US007):**
The `place_enemies()` method positions Polocho enemies with patrol routes:
- **Enemy Count**: Random count within difficulty range (Level 1: 2-3, Level 5: 10-12)
- **Platform Selection**: Enemies spawn only on platforms >= 100px wide and x > 200 (avoiding spawn area)
- **Strategic Placement**: Weighted selection favors platforms near level goal (2.0x priority vs 1.0x)
- **Positioning**: Enemies placed at `platform.y - 40` (standing on platform surface)
- **Patrol Routes**: Each enemy has `patrol_left` and `patrol_right` boundaries
  - Patrol width: 100-300px (within platform boundaries)
  - 10px buffer from platform edges to prevent falling
  - Enemy spawns at center of patrol range
- **Spread**: Enemies distributed across multiple platforms (tracks placed platforms)
- **Output**: Sorted by x position for debugging, includes type, x, y, patrol_left, patrol_right

**JSON Output Structure:**
Each level file contains:
- `level_number`: Level identifier (1-5)
- `width`, `height`: Level dimensions (variable width, 600px height)
- `background_color`: RGB array [135, 206, 235] (sky blue)
- `player_spawn`: Starting position {x: 100, y: 400}
- `platforms`: Array of platform objects with type, x, y, width, height (US006 ✓)
- `enemies`: Array of enemy spawn points with type, x, y, patrol_left, patrol_right (US007 ✓)
- `powerups`: Array of power-up locations (empty until US008)
- `pits`: Array of pit hazards with x, width (US006 ✓)
- `goal`: Level exit position (level_width - 200, 500)

**Usage:**
```bash
python3 tools/level_generator.py
```

### Complete Level JSON Generation (US009)
All 5 level JSON files have been successfully generated with complete, validated data.

**Generated Files:**
- `levels/level_1.json` - 2000x600, 1 powerup, 1 pit, 3 enemies, 9 platforms
- `levels/level_2.json` - 2500x600, 1 powerup, 2 pits, 4 enemies, 13 platforms
- `levels/level_3.json` - 3000x600, 2 powerups, 3 pits, 7 enemies, 18 platforms
- `levels/level_4.json` - 3500x600, 2 powerups, 5 pits, 8 enemies, 23 platforms
- `levels/level_5.json` - 4000x600, 3 powerups, 5 pits, 10 enemies, 26 platforms

**Validation Results:**
- ✓ All JSON files are valid and parseable with Python's `json.load()`
- ✓ Proper indentation (2 spaces) for readability
- ✓ All required sections present in each file
- ✓ Player spawn at {x: 100, y: 400} for all levels
- ✓ Goal at {x: level_width - 200, y: 500} for all levels
- ✓ Background color [135, 206, 235] (sky blue) for all levels
- ✓ Power-ups populated (not empty arrays)
- ✓ Pit widths within 100-200px range
- ✓ All coordinates within level bounds
- ✓ Levels theoretically completable (path exists from spawn to goal)

**Level Schema (Complete):**
```json
{
  "level_number": int,
  "width": int,
  "height": 600,
  "background_color": [135, 206, 235],
  "player_spawn": {"x": 100, "y": 400},
  "platforms": [{"type": str, "x": int, "y": int, "width": int, "height": int}],
  "enemies": [{"type": "polocho", "x": int, "y": int, "patrol_left": int, "patrol_right": int}],
  "powerups": [{"type": "arepa_dorada", "x": int, "y": int}],
  "pits": [{"x": int, "width": int}],
  "goal": {"x": int, "y": 500}
}
```

**Phase 2 Status:** COMPLETE - All 5 user stories (US005-US009) implemented and validated.

### Player Entity System (US010)
The Player class represents Sancho, the player character, with complete state management and rendering.

**Player Class (`src/entities/player.py`):**
- `__init__(x, y)`: Initializes player at spawn position with pygame.Vector2 for position/velocity
- Attributes:
  - `position`, `velocity`: pygame.Vector2 for smooth movement
  - `rect`: pygame.Rect for collision detection (40x60 pixels from constants)
  - `lives`: Integer starting at 3 (from PLAYER_LIVES constant)
  - `has_powerup`, `powerup_timer`: Power-up state tracking
  - `facing_direction`: "LEFT" or "RIGHT" for sprite orientation
  - `is_jumping`, `is_grounded`: Movement state flags
- Methods:
  - `update(dt, platforms)`: Updates player state, rect position, and powerup timer
  - `render(screen, camera)`: Draws player as COLOR_PLAYER (blue) rectangle with camera offset
  - `take_damage()`: Decrements lives when hit
  - `handle_input(keys)`, `jump()`, `apply_gravity(dt)`, `check_collision(platforms)`: Placeholder methods for future user stories

**Camera System (`src/camera.py`):**
- Simple placeholder class with x, y offset attributes
- Enables player rendering with camera offset (full implementation in US014)
- Initialized at (0, 0) in game.py

**Game Integration:**
- Player instantiated at spawn position (100, 400) in `Game.__init__()`
- `player.update(dt, [])` called every frame (empty platforms list until US015)
- `player.render(screen, camera)` draws player on screen
- Successfully tested - game runs without errors, player visible at spawn position

**Entity Package Organization:**
- `src/entities/__init__.py` exports Player class for clean imports
- Ready to add Enemy, PowerUp, and Projectile classes in future phases

### Physics and Gravity System (US011)
The gravity physics system enables realistic falling, jumping, and grounded detection for all game entities.

**Gravity Module (`src/physics/gravity.py`):**
- `apply_gravity(entity, dt)`: Applies gravity to entities not grounded
  - Adds GRAVITY constant (0.8 pixels/frame²) to vertical velocity each frame
  - Caps fall speed at MAX_FALL_SPEED (15 pixels/frame) for terminal velocity
  - Only applies when `entity.is_grounded` is False (no gravity when standing on platforms)
  - Frame-independent ready (dt parameter prepared for future use)

**Player Physics Integration:**
- `Player.update()` method enhanced to:
  1. Call `apply_gravity()` from physics module
  2. Update position based on velocity (`position += velocity`)
  3. Sync rect with position for collision detection
  4. Call `check_collision()` to handle platform interactions
- Physics applied every frame at 60 FPS
- Position updates use pygame.Vector2 for smooth sub-pixel movement

**Jump Mechanics (`Player.jump()`):**
- Sets vertical velocity to JUMP_STRENGTH (-15 pixels/frame) for upward motion
- Only allows jumping when `is_grounded` is True (prevents air jumping)
- Updates state flags: `is_jumping = True`, `is_grounded = False`
- Triggered by space bar input in game event handler

**Grounded Detection (`Player.check_collision()`):**
- Basic platform collision detection implemented for grounded state
- Checks each platform using pygame rect collision (`rect.colliderect()`)
- **Landing on platform** (falling down, velocity.y > 0):
  - Snaps player to platform top: `rect.bottom = platform.rect.top`
  - Resets vertical velocity to 0 (stops falling)
  - Sets `is_grounded = True`, `is_jumping = False`
- **Hitting platform from below** (moving up, velocity.y < 0):
  - Snaps player to platform bottom: `rect.top = platform.rect.bottom`
  - Resets vertical velocity to 0 (stops upward motion)
- Position synced with rect after collision resolution
- Full collision resolution (horizontal, edge cases) planned for US013

**Visual Validation (US011 Testing):**
- Test platforms added to `game.py` for physics validation:
  - Ground platform at y=550 (800x50 pixels)
  - Floating platforms at various heights
  - `TestPlatform` class with rect and render method
- Player spawns at (100, 200) in air to test falling
- Observable behaviors verified:
  - Player falls when spawned in air ✓
  - Fall speed accelerates over time ✓
  - Fall speed caps at 15 pixels/frame ✓
  - Space bar makes player jump ✓
  - Player lands on platforms and can jump again ✓

**Physics Constants (from `src/constants.py`):**
- `GRAVITY = 0.8` - Acceleration per frame (downward)
- `MAX_FALL_SPEED = 15` - Terminal velocity cap
- `JUMP_STRENGTH = -15` - Initial jump velocity (negative = upward)
- Y-axis increases downward (standard pygame convention)

**State Management:**
- `is_grounded`: Boolean flag indicating if player is standing on platform
- `is_jumping`: Boolean flag indicating if player is in jump state
- `velocity.y`: Vertical velocity component (positive = down, negative = up)
- Flags reset properly during collision resolution

### Player Movement and Controls (US012)
The complete input handling system enables smooth player control with keyboard input for horizontal movement and jumping.

**Input Handling (`Player.handle_input()` method):**
- Called every frame from `Player.update()` with `pygame.key.get_pressed()` result
- Processes all player controls in one unified method for smooth simultaneous actions
- Responsive controls with no input lag at 60 FPS

**Horizontal Movement:**
- **LEFT arrow / A key**: Sets `velocity.x = -PLAYER_SPEED` (-5 pixels/frame), updates `facing_direction = "LEFT"`
- **RIGHT arrow / D key**: Sets `velocity.x = PLAYER_SPEED` (5 pixels/frame), updates `facing_direction = "RIGHT"`
- **No keys pressed**: Resets `velocity.x = 0` (immediate stop)
- Movement works both on ground and in air (no restriction)
- Direction changes are immediate and smooth

**Direction Tracking:**
- `facing_direction` attribute tracks last movement direction ("LEFT" or "RIGHT")
- Updates only when movement keys are pressed
- Persists when not moving (remembers last direction)
- Will be used for sprite orientation in future phases

**Jump Control:**
- **SPACE key**: Triggers jump via `jump()` method
- **Jump requirements**: Only works when `is_grounded = True`
- **Key detection**: Uses `space_was_pressed` flag to detect key press vs hold
  - Compares current frame key state with previous frame
  - Only jumps on transition from not-pressed to pressed
  - Prevents "bunny hopping" (holding space for continuous jumps)
  - Requires key release and repress for next jump
- Jump state managed by `jump()` method (sets `velocity.y = JUMP_STRENGTH`, `is_jumping = True`, `is_grounded = False`)

**Control Flow (in `Player.update()`):**
1. Get keyboard state: `keys = pygame.key.get_pressed()`
2. Process input: `self.handle_input(keys)` (sets velocities, detects jump)
3. Apply physics: Gravity affects velocity.y
4. Update position: `position += velocity`
5. Resolve collisions: Check platforms, update grounded state

**Integration:**
- All controls work simultaneously (move + jump at the same time)
- Input processing happens before physics updates
- Smooth movement and responsive controls at 60 FPS
- No conflicts between horizontal movement and jumping

### Collision Detection System (US013)
The collision detection system provides AABB collision detection and comprehensive platform collision resolution for all game entities.

**Collision Module (`src/physics/collision.py`):**
- `check_aabb_collision(rect1, rect2)`: Simple AABB collision detection using pygame's `colliderect()`
  - Returns True if two rectangles overlap
  - Works with all pygame.Rect objects
  - Fast and efficient for rectangular collision checks

- `resolve_platform_collision(entity, platforms)`: Complete collision resolution system
  - **Overlap Calculation**: Determines smallest overlap on X and Y axes
  - **Collision Side Detection**: Identifies which side collided (top, bottom, left, right)
  - **Top Collision (Landing)**:
    - Triggers when entity falling (velocity.y > 0)
    - Snaps entity to platform top surface
    - Sets velocity.y = 0, is_grounded = True, is_jumping = False
    - Allows entity to walk on platform
  - **Bottom Collision (Head Bump)**:
    - Triggers when entity moving up (velocity.y < 0)
    - Snaps entity to platform bottom
    - Sets velocity.y = 0 (stops upward motion)
    - Entity begins falling after collision
  - **Side Collisions (Walls)**:
    - Triggers when horizontal overlap is smaller than vertical
    - Left collision: Snaps entity to platform left edge, velocity.x = 0
    - Right collision: Snaps entity to platform right edge, velocity.x = 0
    - Entity slides down if in air (gravity still applies)
  - **Position Syncing**: Updates entity.rect to match resolved position

**Platform Class (`src/level/tile.py`):**
- `__init__(x, y, width, height, platform_type)`: Constructor for platforms
  - Creates pygame.Rect at specified position
  - Stores platform type ("solid" or "floating")
- `render(screen, camera)`: Camera-relative rendering
  - Brown color (139, 69, 19) for "solid" platforms (ground)
  - Gray color (100, 100, 100) for "floating" platforms (air)
  - Draws relative to camera offset for scrolling levels

**Player Integration:**
- `Player.check_collision()` now delegates to `resolve_platform_collision()`
- Simplified collision handling in player class
- Consistent collision behavior across all game entities
- Maintains was_grounded state for jump detection

**Game Integration:**
- Replaced temporary `TestPlatform` class with proper `Platform` class
- Test platforms created as solid and floating types
- Platforms rendered with correct colors
- Full collision testing available in game

**Collision Algorithm:**
1. Check if entity rect overlaps platform rect (AABB test)
2. Calculate overlap on X-axis and Y-axis
3. Resolve smallest overlap (indicates collision direction):
   - If overlap_x < overlap_y: Side collision (left/right)
   - If overlap_y <= overlap_x: Top/bottom collision
4. Use velocity direction to determine specific collision type
5. Adjust entity position and velocity accordingly
6. Update collision state flags (is_grounded, is_jumping)

**Testing:**
- All modules compile without errors
- Game runs successfully with collision system
- Three test platforms: ground platform + two floating platforms
- Player can land on platforms, hit walls, and bump head on ceilings

### Camera/Viewport System (US014)
The camera system enables smooth scrolling levels that extend beyond the screen width, following the player while respecting level boundaries.

**Camera Class (`src/camera.py`):**
- `__init__(width, height)`: Initializes camera with viewport dimensions
  - `width`, `height`: Viewport size (SCREEN_WIDTH=800, SCREEN_HEIGHT=600)
  - `x`, `y`: Camera position in world coordinates (starts at 0, 0)
  - `level_width`: Maximum camera boundary for current level
- Methods:
  - `update(target_pos, level_width)`: Updates camera position every frame
    - Centers camera on target: `x = target_pos.x - width // 2`
    - Clamps to left boundary: `x = max(0, x)`
    - Clamps to right boundary: `x = min(x, level_width - width)` (if level > screen width)
    - Handles small levels: Camera stays at x=0 when level_width < SCREEN_WIDTH
    - Fixed vertical: y=0 (no vertical scrolling for 2D side-scroller)
  - `apply(world_pos)`: Transforms world coordinates to screen coordinates
    - Returns: `(world_pos.x - camera.x, world_pos.y - camera.y)`
    - Used by all render methods for camera-relative rendering
  - `is_visible(entity)`: Checks if entity is within viewport bounds
    - Returns True if `entity.rect.right > camera.x` AND `entity.rect.left < camera.x + width`
    - Useful for optimization (skip rendering off-screen entities)

**Game Integration:**
- Camera instantiated in `Game.__init__()`: `self.camera = Camera(SCREEN_WIDTH, SCREEN_HEIGHT)`
- Camera updated in `Game.update()`: `self.camera.update(self.player.position, self.level_width)`
- Camera passed to all render methods: `player.render(screen, camera)`, `platform.render(screen, camera)`
- Level width calculated from platform positions: `max(platform.rect.right for platform in platforms)`

**Test Level Configuration:**
- Extended test platforms from 800px to 2000px for camera validation
- 3 ground platform segments with gaps: 0-500, 600-1000, 1100-2000
- 6 floating platforms distributed across level width
- Level width: 2000px (calculated from rightmost platform edge)

**Camera Behavior:**
- **Following**: Camera centers on player horizontally, creating smooth scrolling effect
- **Left Boundary**: Camera stops at x=0, player can move to left edge of screen
- **Right Boundary**: Camera stops at `level_width - 800`, player can move to right edge
- **Small Levels**: If level < 800px, camera stays at x=0 (no scrolling needed)
- **Smooth Scrolling**: No jittering or jumping, 60 FPS updates

**Coordinate System:**
- World coordinates: Absolute positions in level (0 to level_width)
- Screen coordinates: Positions on display (0 to SCREEN_WIDTH)
- Transformation: `screen_x = world_x - camera.x`
- Example: Player at world x=1000, camera at x=600 → renders at screen x=400

**Benefits:**
- Enables levels larger than screen width (critical for Phase 4 level loading)
- Player stays centered for optimal visibility
- Smooth scrolling creates professional game feel
- Boundary clamping prevents showing empty space beyond level edges
- Viewport culling support ready for performance optimization

### Power-Up and Pit Placement (US008)
The level generator now includes complete power-up and pit placement systems with strategic positioning and validation.

**Power-Up Placement (`place_powerups()` method):**
- **Power-Up Counts**: L1-L2 (1), L3-L4 (2), L5 (2-3)
- **Distribution**: Power-ups divided across level segments for even spread
- **Positioning Strategy**:
  - Places power-ups 50-150 pixels above nearest platform (floating in air)
  - Finds nearest platform below target position using distance calculation
  - Ensures first power-up appears in first half of level
  - Coordinates kept within safe bounds (300px from edges)
- **JSON Format**: `{type: "arepa_dorada", x: int, y: int}`
- **Reachability**: All power-ups positioned to require jumping from platforms
- **Strategic Placement**: Power-ups near challenging sections and enemy locations

**Pit Placement Enhancement (`create_pits()` method):**
- **Pit Counts**: L1 (1-2), L2 (2-3), L3 (3-4), L4 (4-5), L5 (5-6)
- **Pit Dimensions**: 100-200 pixels wide (scales with difficulty)
- **Safe Zones**: 300px from spawn, 200px from goal (prevents unfair deaths)
- **Validation**:
  - Overlap detection ensures pits don't intersect
  - Segment-based placement prevents clustering
  - Ground platforms automatically split at pit locations (from US006)
- **JSON Format**: `{x: int, width: int}` sorted by x position
- **Crossability**: Floating platforms positioned to allow crossing all pits

**Risk/Reward Balance:**
- Power-ups strategically positioned near pits and enemies
- Level remains completable with all hazards in place
- Progressive difficulty maintained across all 5 levels

### Level Loader System (US015)
The level loader provides robust JSON file loading and comprehensive validation for all level data.

**LevelLoader Class (`src/level/level_loader.py`):**
- `__init__()`: Initializes loader with `levels_dir = "levels"` path
- Methods:
  - `load_level(filename)`: Loads JSON file from path, returns validated dict or None
  - `load_level_by_number(level_num)`: Convenience method for loading level_1.json through level_5.json
  - `validate_level(data)`: Comprehensive validation of level data structure

**Error Handling:**
- **FileNotFoundError**: Clear message with file path, returns None
- **JSONDecodeError**: Reports JSON parse errors with line/column, returns None
- **ValidationError**: Field-specific error messages, returns None
- All errors logged to console for debugging

**Validation Coverage:**
- **Required Fields**: Checks all 10 top-level fields (level_number, width, height, background_color, player_spawn, platforms, enemies, powerups, pits, goal)
- **Data Types**: Validates integers, lists, dicts, RGB arrays
- **Numeric Validation**: Ensures positive dimensions, 0-255 RGB values
- **Nested Objects**: Validates player_spawn.x/y and goal.x/y exist and are numeric
- **Array Elements**: Validates each platform/enemy/powerup/pit has required fields
- **Coordinate Bounds**: Ensures all x/y coordinates are within level width/height
- **Platform Validation**: type, x, y, width, height fields required
- **Enemy Validation**: type, x, y, patrol_left, patrol_right fields required
- **Powerup Validation**: type, x, y fields required
- **Pit Validation**: x, width fields required

**Path Handling:**
- Accepts relative paths: `"levels/level_1.json"`
- Accepts absolute paths
- Works from project root directory
- OS-independent path handling with `os.path.join()`

**Testing:**
- Successfully loads all 5 generated level JSON files (level_1 through level_5)
- Verified with comprehensive test script: `test_level_loader.py`
- Returns correct data structures matching JSON content
- Error handling tested with missing files and corrupted JSON

**Integration:**
- Exported from `src/level/__init__.py` for clean imports
- Ready for use in Level class (US016) and game loop integration (US017)
- Provides foundation for level progression system

### Level Class System (US016)
The Level class provides complete game management for loaded levels, converting JSON data into active game objects and managing all level entities.

**Level Class (`src/level/level.py`):**
- `__init__(level_data)`: Initializes level from LevelLoader parsed JSON data
  - **Attributes**:
    - `level_number`: Integer level identifier (1-5)
    - `width`, `height`: Level dimensions in pixels
    - `background_color`: RGB tuple for level background
    - `player_spawn`: Dict with x, y spawn coordinates
    - `goal`: Dict with x, y goal position
    - `pits`: List of pit zones (x, width dicts)
    - `platforms`: List of Platform objects (converted from JSON)
    - `enemies`: Empty list (placeholder for Phase 5)
    - `powerups`: Empty list (placeholder for Phase 6)

**Platform Object Creation:**
- Converts JSON platform data to Platform objects on initialization
- Each platform created with: `Platform(x, y, width, height, type)`
- Platform types preserved: "solid" (ground) and "floating" (air platforms)
- All platforms accessible via `get_platforms()` for collision detection

**Core Methods:**
- `update(dt, player)`: Updates all level entities each frame
  - Currently placeholder for enemy/powerup updates (Phase 5/6)
  - Receives delta time and player reference
  - Will manage entity AI and interactions in future phases

- `render(screen, camera)`: Draws all level elements with camera offset
  - Fills background with `background_color`
  - Renders all platforms via `platform.render(screen, camera)`
  - Draws goal indicator as green 50x50 rectangle
  - All rendering respects camera position for scrolling

- `check_goal(player)`: Detects level completion
  - Returns True if player within 50 pixels of goal x position
  - Uses distance calculation: `abs(player.position.x - goal['x']) < 50`

- `check_pits(player)`: Detects pit falls
  - Checks if player x position within any pit's x to x+width range
  - Triggers if player y position exceeds `height - 100` (falling threshold)
  - Returns True if player should lose a life

- `get_platforms()`: Returns list of Platform objects for collision
- `get_spawn_position()`: Returns (x, y) tuple for player spawning
- `reset()`: Placeholder for level reset (will reset enemies/powerups in future)

**Validation:**
- ✓ Successfully imports and compiles without errors
- ✓ Can be instantiated from loaded JSON data
- ✓ Platform objects created correctly from JSON
- ✓ All attributes accessible and match JSON data
- ✓ Methods callable and return expected types

**Integration:**
- Exported from `src/level/__init__.py` alongside LevelLoader and Platform
- Integrated into game loop (US017) ✓
- Provides foundation for enemy (Phase 5) and powerup (Phase 6) systems
- Works seamlessly with existing Camera and collision systems

### Game Loop Integration (US017)
The game loop has been fully integrated with the level loading system, enabling complete gameplay through all 5 levels.

**Game Class Enhancements (`src/game.py`):**
- **Level Management Attributes**:
  - `level_loader`: LevelLoader instance for loading JSON files
  - `current_level_number`: Tracks current level (1-5)
  - `current_level`: Active Level object containing all level data and entities

- **Level Loading Methods**:
  - `load_level(level_num)`: Loads specific level by number (1-5)
    - Calls `LevelLoader.load_level_by_number()`
    - Creates Level object from JSON data
    - Updates `current_level_number`
    - Prints loading status to console
    - Exits game if level fails to load
  - `load_next_level()`: Advances to next level
    - Increments level number
    - Loads next level (or ends game after Level 5)
    - Calls `respawn_player()` to reset player state
    - Prints completion messages
  - `respawn_player()`: Resets player at spawn point
    - Gets spawn position from current level
    - Resets position, velocity, and grounded state
    - Used for both level progression and pit respawns

- **Initialization Changes**:
  - Level 1 loaded on game startup
  - Player spawned at level's spawn position (not hardcoded)
  - Test platforms removed (levels manage platforms now)

- **Update Loop Integration** (`update()` method):
  - Calls `current_level.update(dt, player)` to update level state
  - Passes `current_level.get_platforms()` to player for collision
  - Uses `current_level.width` for camera boundary
  - **Win Condition**: Checks `current_level.check_goal(player)`
    - If True: Loads next level automatically
    - Progresses through all 5 levels sequentially
    - Exits game with "Game Complete!" after Level 5
  - **Lose Condition**: Checks `current_level.check_pits(player)`
    - If True: Decreases player lives via `player.take_damage()`
    - Lives > 0: Respawns player at spawn point
    - Lives = 0: Exits game with "Game Over!"

- **Render Integration** (`render()` method):
  - Calls `current_level.render(screen, camera)` first (background + platforms + goal)
  - Then calls `player.render(screen, camera)` on top
  - Correct Z-order maintained (level behind player)
  - All rendering respects camera offset for scrolling

**Gameplay Flow:**
1. Game starts → Level 1 loads → Player spawns at (100, 400)
2. Player navigates platforms using keyboard controls
3. Reach goal → Level complete → Load next level
4. Fall in pit → Lose 1 life → Respawn at spawn point
5. Lives = 0 → Game over
6. Complete Level 5 → Game complete

**Testing Results:**
- ✓ Level 1 loads successfully from JSON
- ✓ Player navigates level terrain with collision
- ✓ Reaching goal triggers level progression
- ✓ Successfully progressed Level 1 → 2 → 3 in testing
- ✓ Player respawns correctly at spawn point (100, 400)
- ✓ All level elements render correctly (background, platforms, goal, player)
- ✓ Camera follows player and respects level boundaries

**Phase 4 Status:** US017 COMPLETE - Game loop fully integrated with level system. All 5 levels are now playable in sequence.

---

## Implementation Notes

### Level System
- Levels will be stored as JSON files in `levels/` directory
- Level generator tool (`tools/level_generator.py`) will be created in Phase 2
- 5 levels planned with progressive difficulty scaling

### Assets
- Asset directories currently empty (placeholders)
- Initial implementation will use colored rectangles as placeholders
- Sprite/audio integration planned for later phases

### Module System
- All Python packages initialized with `__init__.py`
- Ready for entity classes and game systems to be added
