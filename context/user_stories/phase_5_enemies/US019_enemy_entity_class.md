# US019: Create Enemy Entity Class (Polocho)

**As a** developer
**I want** to create the Polocho enemy class with basic structure
**So that** enemies can exist in the game world

## Priority
High

## Story Points
5

## Acceptance Criteria

1. **Enemy Class Created**
   - [ ] `src/entities/enemy.py` exists
   - [ ] `Polocho` class is defined

2. **Enemy Attributes**
   - [ ] `position`: pygame.Vector2 (x, y)
   - [ ] `velocity`: pygame.Vector2 (vx, vy)
   - [ ] `rect`: pygame.Rect for collision
   - [ ] `width`, `height`: int (e.g., 32x40 pixels)
   - [ ] `patrol_left`: int (left boundary)
   - [ ] `patrol_right`: int (right boundary)
   - [ ] `facing_direction`: string ("LEFT" or "RIGHT")
   - [ ] `is_alive`: bool (starts True)
   - [ ] `speed`: int (e.g., 2 pixels/frame)

3. **Enemy Initialization**
   - [ ] `__init__(x, y, patrol_left, patrol_right)`: Create enemy
   - [ ] Position set correctly
   - [ ] Patrol boundaries stored
   - [ ] Initial direction set to "RIGHT"
   - [ ] Rect created for collision

4. **Enemy Methods Structure**
   - [ ] `update(dt, platforms)`: Update enemy state (placeholder)
   - [ ] `patrol()`: Handle patrol movement (placeholder)
   - [ ] `check_boundaries()`: Check patrol limits (placeholder)
   - [ ] `die()`: Handle enemy death
   - [ ] `render(screen, camera)`: Draw enemy

5. **Basic Rendering**
   - [ ] Enemy renders as colored rectangle (RED placeholder)
   - [ ] Uses COLOR_ENEMY from constants
   - [ ] Position respects camera offset
   - [ ] Visible when in viewport

6. **Death Handling**
   - [ ] `die()` method sets `is_alive = False`
   - [ ] Dead enemies don't render
   - [ ] Dead enemies don't update

7. **Integration with Level**
   - [ ] Enemy can be instantiated from level JSON data
   - [ ] Level creates enemy objects from JSON
   - [ ] Enemies stored in level.enemies list

8. **Validation**
   - [ ] Enemy class imports successfully
   - [ ] Enemy object can be created
   - [ ] Enemy renders at correct position
   - [ ] Multiple enemies can exist simultaneously

## Technical Notes

```python
# src/entities/enemy.py
import pygame
from src.constants import *

class Polocho:
    def __init__(self, x, y, patrol_left, patrol_right):
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.width = 32
        self.height = 40
        self.rect = pygame.Rect(x, y, self.width, self.height)

        self.patrol_left = patrol_left
        self.patrol_right = patrol_right
        self.speed = 2
        self.facing_direction = "RIGHT"
        self.is_alive = True

    def update(self, dt, platforms):
        """Update enemy state"""
        if not self.is_alive:
            return

        # Update rect
        self.rect.x = self.position.x
        self.rect.y = self.position.y

    def die(self):
        """Handle enemy death"""
        self.is_alive = False

    def render(self, screen, camera):
        """Draw enemy"""
        if not self.is_alive:
            return

        screen_x = self.position.x - camera.x
        screen_y = self.position.y - camera.y
        pygame.draw.rect(screen, COLOR_ENEMY,
                        (screen_x, screen_y, self.width, self.height))

# In Level class - add enemy creation:
def __init__(self, level_data):
    # ... existing code ...

    # Create enemy objects
    from src.entities.enemy import Polocho
    self.enemies = []
    for e_data in level_data['enemies']:
        enemy = Polocho(
            e_data['x'], e_data['y'],
            e_data['patrol_left'],
            e_data['patrol_right']
        )
        self.enemies.append(enemy)
```

## Dependencies
- US016: Level class must exist
- US003: Constants must be defined
