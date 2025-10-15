# US010: Create Player Entity Class (Sancho)

**As a** developer
**I want** to create the Player class with basic structure
**So that** Sancho can exist in the game world

## Priority
Critical

## Story Points
5

## Acceptance Criteria

1. **Player Class Created**
   - [x] `src/entities/player.py` exists
   - [x] `Player` class is defined with proper initialization

2. **Player Attributes**
   - [x] `position`: pygame.Vector2 (x, y coordinates)
   - [x] `velocity`: pygame.Vector2 (vx, vy movement)
   - [x] `rect`: pygame.Rect for collision detection
   - [x] `lives`: int (starts at 3)
   - [x] `has_powerup`: bool (starts False)
   - [x] `powerup_timer`: float (0.0)
   - [x] `facing_direction`: string ("LEFT" or "RIGHT")
   - [x] `is_jumping`: bool
   - [x] `is_grounded`: bool
   - [x] `width`, `height`: int (e.g., 32x48 pixels)

3. **Player Methods Structure**
   - [x] `__init__(x, y)`: Initialize player at position
   - [x] `update(dt, platforms)`: Update player state (placeholder)
   - [x] `handle_input(keys)`: Process keyboard input (placeholder)
   - [x] `jump()`: Initiate jump (placeholder)
   - [x] `apply_gravity(dt)`: Apply gravity to velocity
   - [x] `check_collision(platforms)`: Check platform collisions (placeholder)
   - [x] `take_damage()`: Handle player damage
   - [x] `render(screen, camera)`: Draw player

4. **Basic Rendering**
   - [x] Player renders as a colored rectangle (placeholder sprite)
   - [x] Uses COLOR_PLAYER from constants
   - [x] Position respects camera offset
   - [x] Visible when player is in viewport

5. **Integration with Game**
   - [x] Player can be instantiated in game.py
   - [x] Player appears in game window
   - [x] No errors when rendering

6. **Validation**
   - [x] Player class imports successfully
   - [x] Player object can be created with: `player = Player(100, 400)`
   - [x] Player renders at correct screen position

## Technical Notes

```python
import pygame
from src.constants import *

class Player:
    def __init__(self, x, y):
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.width = 32
        self.height = 48
        self.rect = pygame.Rect(x, y, self.width, self.height)

        self.lives = PLAYER_LIVES
        self.has_powerup = False
        self.powerup_timer = 0.0
        self.facing_direction = "RIGHT"
        self.is_jumping = False
        self.is_grounded = False

    def update(self, dt, platforms):
        # Update rect position
        self.rect.x = self.position.x
        self.rect.y = self.position.y

    def render(self, screen, camera):
        # Draw player relative to camera
        screen_x = self.position.x - camera.x
        screen_y = self.position.y - camera.y
        pygame.draw.rect(screen, COLOR_PLAYER,
                        (screen_x, screen_y, self.width, self.height))
```

## Dependencies
- US003: Constants must be defined
- US004: Game window must exist
