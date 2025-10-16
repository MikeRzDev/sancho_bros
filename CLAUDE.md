# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Sancho Bros** is a 2D platformer game built with Python and Pygame. The game features Sancho, a Colombian coffee farmer, navigating through 5 levels of increasing difficulty while defeating Polocho enemies and collecting La Arepa Dorada power-ups.

**Key Features:**
- 5 externally-loaded JSON levels
- Platform physics with gravity and jumping
- Enemy AI with patrol behavior
- Stomp-on-head and laser combat mechanics
- Power-up system that grants temporary shooting ability

## Architecture

### Core Structure

The codebase follows a modular entity-component architecture:

- **src/main.py**: Entry point, initializes Pygame and starts game loop
- **src/game.py**: Main game loop with state management (MENU, PLAYING, PAUSED, GAME_OVER)
- **src/entities/**: Player, Enemy, PowerUp, and Projectile classes
- **src/level/**: Level loading system that reads JSON files
- **src/physics/**: Collision detection and gravity systems
- **src/camera.py**: Viewport system that follows the player
- **src/ui/**: Menu, HUD, and screen management

### Level System

Levels are stored as JSON files in `levels/` directory (level_1.json through level_5.json).

**JSON Structure:**
```json
{
  "level_number": 1,
  "width": 3200,
  "height": 600,
  "background_color": [135, 206, 235],
  "player_spawn": {"x": 100, "y": 400},
  "platforms": [
    {"type": "solid", "x": 0, "y": 550, "width": 800, "height": 50},
    {"type": "floating", "x": 300, "y": 400, "width": 100, "height": 20}
  ],
  "enemies": [
    {"type": "polocho", "x": 500, "y": 510, "patrol_left": 400, "patrol_right": 600}
  ],
  "powerups": [
    {"type": "arepa_dorada", "x": 1000, "y": 300}
  ],
  "pits": [
    {"x": 800, "width": 100}
  ],
  "goal": {"x": 3000, "y": 500}
}
```

**Level Elements:**
- `platforms`: Two types - "solid" (ground) and "floating" (air platforms)
- `enemies`: Polocho spawn points with patrol boundaries (patrol_left, patrol_right)
- `powerups`: La Arepa Dorada collectibles
- `pits`: Fall zones that kill player
- `goal`: Level exit trigger position

The level loader (`level/level_loader.py`) parses these files and instantiates game objects. The Level class (`level/level.py`) manages all entities and checks win/lose conditions.

### Game Loop

60 FPS game loop:
1. Handle input events
2. Update all entities (player, enemies, projectiles)
3. Check collisions (platforms, enemies, power-ups, pits)
4. Update camera to follow player
5. Render everything relative to camera position

### Physics System

- Gravity constant: 0.8 pixels/frame²
- Collision uses AABB (Axis-Aligned Bounding Box)
- Player can stomp enemies by landing on their heads (detected via vertical velocity + top collision)
- Pits check if player Y coordinate exceeds level height

## Project Status

**Current Version**: 1.0 - All core features complete
**Last Updated**: October 2025
**Status**: Feature-complete, polished, ready for distribution

### Known Issues
- Debug commands (K, L, I, T, 1-5) available during gameplay (low priority - useful for testing)
- No audio/sound effects (expected - out of scope for v1.0)

See `docs/KNOWN_ISSUES.md` for complete list.

## Development Commands

### Debug Mode
Set `DEBUG = True` in `src/constants.py` to enable debug print statements throughout the codebase. When False (default), the game runs silently except for error messages.

This affects print statements in:
- game.py (state changes, level loading, player respawn, collision events)
- player.py (damage, power-up collection, laser shooting)
- entities (projectile hits, power-up collection)
- level_loader.py (successful level loads)

### Initial Setup (IMPORTANT)

### Initial Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Generate level files (run once, must be done before first game run)
python tools/level_generator.py
```

### Running the Game
```bash
# Run from project root
python src/main.py
```

### Level Generation
```bash
# Regenerate all 5 levels
python tools/level_generator.py

# The generator creates levels with progressive difficulty:
# - Level 1: 2000px, 2-3 enemies, 1 power-up, 1-2 pits (tutorial)
# - Level 2: 2500px, 4-5 enemies, 1 power-up, 2-3 pits
# - Level 3: 3000px, 6-7 enemies, 2 power-ups, 3-4 pits
# - Level 4: 3500px, 8-9 enemies, 2 power-ups, 4-5 pits
# - Level 5: 4000px, 10-12 enemies, 2-3 power-ups, 5-6 pits (maximum challenge)
```

## Game Constants Reference

Located in `src/constants.py`:

```python
# Screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Physics
GRAVITY = 0.8              # Applied each frame
MAX_FALL_SPEED = 15        # Terminal velocity
JUMP_STRENGTH = -15        # Initial upward velocity
PLAYER_SPEED = 5           # Horizontal pixels per frame

# Game Rules
PLAYER_LIVES = 3           # Starting lives
LASER_DURATION = 10        # Seconds power-up lasts
LASER_COOLDOWN = 0.5       # Seconds between laser shots
```

## Key Conventions

### Code Style
- Class names: PascalCase (Player, Polocho, LevelLoader)
- Functions/methods: snake_case (update, handle_input, check_collision)
- Constants: UPPER_SNAKE_CASE (SCREEN_WIDTH, GRAVITY, FPS)

### Entity Update Pattern
All game entities follow this pattern:
```python
def update(self, dt, *args):
    # 1. Update internal state
    # 2. Apply physics (gravity, movement)
    # 3. Check collisions
    # 4. Update animation state
```

### Coordinate System
- Origin (0,0) is top-left of level
- X increases rightward
- Y increases downward
- Camera transforms world coordinates to screen coordinates

### Collision Detection
- Player collides with platforms from all sides
- Enemies only detect platform edges for patrol turning
- Stomp detection requires: player moving down + player bottom touching enemy top
- Laser collision checks bounding box overlap with enemies

### File Organization
- Keep game logic separate from rendering
- Entity classes handle their own collision and update logic
- Level loader only parses files, Level class manages game objects
- UI components are self-contained and state-aware
- Test files organized in `tests/` directory
- Documentation in `docs/` directory (TESTING.md, KNOWN_ISSUES.md, FUTURE_IMPROVEMENTS.md)

## Development Roadmap

The game is implemented in 7 phases (see context/game_implementation.md for full details):

1. **Phase 1: Setup** - Project structure, Pygame initialization, constants
2. **Phase 2: Level Generator** - Build tools/level_generator.py, generate 5 JSON levels
3. **Phase 3: Core Mechanics** - Player movement, gravity, jumping, camera
4. **Phase 4: Level Loading** - JSON parser, platform rendering, level progression
5. **Phase 5: Enemies** - Polocho AI, patrol behavior, stomp mechanics
6. **Phase 6: Power-Ups** - Arepa Dorada collection, laser shooting system
7. **Phase 7: UI & Polish** - Menus, HUD, game states, testing

**Critical Path:** The level generator (Phase 2) must be completed before the game can run, as all 5 level JSON files are required.

## Entity Behaviors

### Player (Sancho)
- **Controls**: Arrow keys/WASD for movement, Space to jump, X/Ctrl to shoot laser
- **Physics**: 5 px/frame speed, -15 jump strength, 0.8 gravity per frame
- **Lives**: Starts with 3, loses one on enemy contact or pit fall
- **States**: IDLE, WALK, JUMP, SHOOT (for animation)

### Enemy (Polocho)
- **AI**: Patrol between left/right boundaries, turn at edges
- **Defeat**: Jump on head (stomp) or hit with laser
- **Collision**: Damages player on contact (unless being stomped)

### Power-Up (La Arepa Dorada)
- **Duration**: 10 seconds of laser ability
- **Cooldown**: 0.5 seconds between laser shots
- **Effect**: Enables shooting projectiles horizontally

### Laser Projectile
- **Lifetime**: 2 seconds before auto-destruction
- **Collision**: Destroys on hitting enemy or platform
- **Movement**: Horizontal only, high speed

## Asset Notes

Initial implementation uses colored rectangles as placeholder graphics:
- Player: Blue rectangle
- Enemy: Red rectangle
- Platform: Brown/gray rectangles
- Power-up: Yellow/gold rectangle
- Laser: Bright line/small rectangle

Sprites should be in `assets/sprites/` with subdirectories for each entity type. Sound effects in `assets/sounds/`, music in `assets/music/`.
