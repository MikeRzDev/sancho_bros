# US003: Create Game Constants Configuration

**As a** developer
**I want** to define all game constants in a centralized file
**So that** configuration values can be easily accessed and modified throughout the codebase

## Priority
High

## Story Points
1

## Acceptance Criteria

1. **Constants File Created**
   - [x] `src/constants.py` exists

2. **Screen Constants Defined**
   - [x] `SCREEN_WIDTH = 800`
   - [x] `SCREEN_HEIGHT = 600`
   - [x] `FPS = 60`

3. **Physics Constants Defined**
   - [x] `GRAVITY = 0.8`
   - [x] `MAX_FALL_SPEED = 15`
   - [x] `JUMP_STRENGTH = -15`
   - [x] `PLAYER_SPEED = 5`

4. **Game Rules Constants Defined**
   - [x] `PLAYER_LIVES = 3`
   - [x] `LASER_DURATION = 10` (seconds)
   - [x] `LASER_COOLDOWN = 0.5` (seconds between shots)

5. **Entity Size Constants**
   - [x] Player dimensions defined
   - [x] Enemy dimensions defined
   - [x] Platform dimensions defined

6. **Color Constants** (for placeholder graphics)
   - [x] Background color
   - [x] Player color
   - [x] Enemy color
   - [x] Platform colors
   - [x] Power-up color

7. **Validation**
   - [x] Constants can be imported successfully: `from src.constants import *`
   - [x] All constants match specifications in game_implementation.md Section 4.2

## Technical Notes

```python
# Example structure:
# Screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Physics
GRAVITY = 0.8
MAX_FALL_SPEED = 15
JUMP_STRENGTH = -15
PLAYER_SPEED = 5

# Game Rules
PLAYER_LIVES = 3
LASER_DURATION = 10
LASER_COOLDOWN = 0.5

# Colors (RGB tuples)
COLOR_BACKGROUND = (135, 206, 235)
COLOR_PLAYER = (0, 0, 255)
COLOR_ENEMY = (255, 0, 0)
COLOR_PLATFORM = (139, 69, 19)
COLOR_POWERUP = (255, 215, 0)
```

## Dependencies
- US001: Project structure must exist
