# US024: Create Power-Up Entity Class (La Arepa Dorada)

**As a** developer
**I want** to create the PowerUp class for La Arepa Dorada
**So that** power-ups can exist and be collected in levels

## Priority
High

## Story Points
3

## Acceptance Criteria

1. **PowerUp Class Created**
   - [ ] `src/entities/powerup.py` exists
   - [ ] `PowerUp` class is defined

2. **PowerUp Attributes**
   - [ ] `position`: pygame.Vector2 (x, y)
   - [ ] `rect`: pygame.Rect for collision
   - [ ] `width`, `height`: int (e.g., 32x32 pixels)
   - [ ] `collected`: bool (starts False)
   - [ ] `type`: string ("arepa_dorada")
   - [ ] `animation_frame`: float (for animation)

3. **PowerUp Initialization**
   - [ ] `__init__(x, y, powerup_type)`: Create power-up
   - [ ] Position set correctly
   - [ ] Rect created for collision
   - [ ] Type stored

4. **PowerUp Methods**
   - [ ] `update(dt)`: Update animation
   - [ ] `check_collection(player)`: Detect player collision
   - [ ] `collect()`: Handle collection
   - [ ] `render(screen, camera)`: Draw power-up

5. **Basic Rendering**
   - [ ] Power-up renders as colored rectangle (YELLOW/GOLD placeholder)
   - [ ] Uses COLOR_POWERUP from constants
   - [ ] Position respects camera offset
   - [ ] Visible when in viewport
   - [ ] Not rendered when collected

6. **Simple Animation**
   - [ ] Power-up has bobbing animation (up/down motion)
   - [ ] Animation cycle: ~2 seconds
   - [ ] Uses sin wave or similar for smooth motion
   - [ ] Makes power-up noticeable

7. **Collection Detection**
   - [ ] `check_collection(player)` uses AABB collision
   - [ ] Returns True if player rect overlaps power-up rect
   - [ ] Only detects when not already collected

8. **Integration with Level**
   - [ ] Level creates power-up objects from JSON
   - [ ] Power-ups stored in level.powerups list
   - [ ] Power-up positions from JSON data

9. **Validation**
   - [ ] PowerUp class imports successfully
   - [ ] PowerUp object can be created
   - [ ] PowerUp renders at correct position
   - [ ] Multiple power-ups can exist
   - [ ] Power-ups visible in all levels

## Technical Notes

```python
# src/entities/powerup.py
import pygame
import math
from src.constants import *

class PowerUp:
    def __init__(self, x, y, powerup_type):
        self.position = pygame.Vector2(x, y)
        self.original_y = y  # For bobbing animation
        self.width = 32
        self.height = 32
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.type = powerup_type  # "arepa_dorada"
        self.collected = False
        self.animation_frame = 0.0

    def update(self, dt):
        """Update power-up animation"""
        if self.collected:
            return

        # Bobbing animation
        self.animation_frame += dt * 2  # Speed of bobbing
        offset = math.sin(self.animation_frame) * 10  # Amplitude
        self.position.y = self.original_y + offset

        # Update rect
        self.rect.x = self.position.x
        self.rect.y = self.position.y

    def check_collection(self, player):
        """Check if player collided with power-up"""
        if self.collected:
            return False

        from src.physics.collision import check_aabb_collision
        return check_aabb_collision(player.rect, self.rect)

    def collect(self):
        """Mark power-up as collected"""
        self.collected = True
        print(f"Power-up collected: {self.type}")

    def render(self, screen, camera):
        """Draw power-up"""
        if self.collected:
            return

        screen_x = self.position.x - camera.x
        screen_y = self.position.y - camera.y
        pygame.draw.rect(screen, COLOR_POWERUP,
                        (screen_x, screen_y, self.width, self.height))

# In Level class - add power-up creation:
def __init__(self, level_data):
    # ... existing code ...

    # Create power-up objects
    from src.entities.powerup import PowerUp
    self.powerups = []
    for p_data in level_data['powerups']:
        powerup = PowerUp(
            p_data['x'],
            p_data['y'],
            p_data['type']
        )
        self.powerups.append(powerup)

def update(self, dt, player):
    """Update all level entities"""
    # Update power-ups
    for powerup in self.powerups:
        powerup.update(dt)

def render(self, screen, camera):
    """Render all level elements"""
    # ... existing rendering ...

    # Render power-ups
    for powerup in self.powerups:
        powerup.render(screen, camera)
```

## Dependencies
- US016: Level class must exist
- US003: Constants must be defined
- US013: Collision system must exist
