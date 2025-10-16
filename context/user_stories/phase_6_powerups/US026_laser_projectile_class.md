# US026: Create Laser Projectile Class

**As a** developer
**I want** to create a Laser projectile class
**So that** players can shoot laser beams when powered up

## Priority
High

## Story Points
5

## Acceptance Criteria

1. **Laser Class Created**
   - [x] `src/entities/projectile.py` exists
   - [x] `Laser` class is defined

2. **Laser Attributes**
   - [x] `position`: pygame.Vector2 (x, y)
   - [x] `velocity`: pygame.Vector2 (vx, 0) - horizontal only
   - [x] `rect`: pygame.Rect for collision
   - [x] `width`, `height`: int (e.g., 16x4 pixels)
   - [x] `direction`: string ("LEFT" or "RIGHT")
   - [x] `speed`: int (e.g., 10 pixels/frame)
   - [x] `lifetime`: float (starts at 2.0 seconds)
   - [x] `is_active`: bool (starts True)

3. **Laser Initialization**
   - [x] `__init__(x, y, direction)`: Create laser
   - [x] Position set to player position
   - [x] Direction determines velocity sign
   - [x] Speed constant and fast

4. **Laser Methods**
   - [x] `update(dt, platforms, enemies)`: Update position and check collisions
   - [x] `check_collisions(platforms, enemies)`: Detect hits
   - [x] `destroy()`: Deactivate laser
   - [x] `render(screen, camera)`: Draw laser

5. **Laser Movement**
   - [x] Moves horizontally at high speed
   - [x] Direction matches player facing direction
   - [x] Velocity constant (no acceleration)
   - [x] Updates position each frame

6. **Lifetime System**
   - [x] Lifetime decreases each frame (dt)
   - [x] Laser destroys when lifetime <= 0
   - [x] Auto-destruction after 2 seconds
   - [x] Prevents lasers from lingering forever

7. **Collision Detection**
   - [x] Detects collision with platforms
   - [x] Detects collision with enemies
   - [x] Destroys on contact with either
   - [x] Uses AABB collision

8. **Enemy Hit Detection**
   - [x] Checks collision with all alive enemies
   - [x] Returns hit enemy or None
   - [x] Laser destroys after hitting enemy
   - [x] Enemy dies from laser hit

9. **Platform Hit Detection**
   - [x] Checks collision with all platforms
   - [x] Laser destroys on platform contact
   - [x] Prevents lasers from going through walls

10. **Rendering**
    - [x] Laser renders as colored line/rectangle
    - [x] Bright color (white, yellow, or cyan)
    - [x] Clearly visible against background
    - [x] Only renders when active

11. **Validation**
    - [x] Laser can be created
    - [x] Laser moves in correct direction
    - [x] Laser destroys after 2 seconds
    - [x] Laser destroys on collision
    - [x] Multiple lasers can exist

## Technical Notes

```python
# src/entities/projectile.py
import pygame
from src.constants import *

class Laser:
    def __init__(self, x, y, direction):
        self.position = pygame.Vector2(x, y)
        self.direction = direction
        self.speed = 10

        # Set velocity based on direction
        if direction == "RIGHT":
            self.velocity = pygame.Vector2(self.speed, 0)
        else:
            self.velocity = pygame.Vector2(-self.speed, 0)

        self.width = 16
        self.height = 4
        self.rect = pygame.Rect(x, y, self.width, self.height)

        self.lifetime = 2.0  # Seconds
        self.is_active = True

    def update(self, dt, platforms, enemies):
        """Update laser position and check collisions"""
        if not self.is_active:
            return

        # Update lifetime
        self.lifetime -= dt
        if self.lifetime <= 0:
            self.destroy()
            return

        # Move laser
        self.position += self.velocity
        self.rect.x = self.position.x
        self.rect.y = self.position.y

        # Check collisions
        self.check_collisions(platforms, enemies)

    def check_collisions(self, platforms, enemies):
        """Check if laser hit anything"""
        from src.physics.collision import check_aabb_collision

        # Check platform collision
        for platform in platforms:
            if check_aabb_collision(self.rect, platform.rect):
                self.destroy()
                return

        # Check enemy collision
        for enemy in enemies:
            if enemy.is_alive and check_aabb_collision(self.rect, enemy.rect):
                enemy.die()
                self.destroy()
                print("Laser hit enemy!")
                return

    def destroy(self):
        """Deactivate laser"""
        self.is_active = False

    def render(self, screen, camera):
        """Draw laser"""
        if not self.is_active:
            return

        screen_x = self.position.x - camera.x
        screen_y = self.position.y - camera.y

        # Draw as bright line
        pygame.draw.rect(screen, (0, 255, 255),  # Cyan
                        (screen_x, screen_y, self.width, self.height))
```

**Integration with Game:**
```python
# In Game class:
def __init__(self):
    # ... existing code ...
    self.lasers = []  # List of active lasers

def update(self, dt):
    # ... existing updates ...

    # Update lasers
    for laser in self.lasers[:]:  # Copy list to allow removal
        laser.update(dt,
                    self.current_level.get_platforms(),
                    self.current_level.enemies)
        if not laser.is_active:
            self.lasers.remove(laser)

def render(self):
    # ... existing rendering ...

    # Render lasers
    for laser in self.lasers:
        laser.render(self.screen, self.camera)
```

## Dependencies
- US019: Enemy class must exist
- US013: Collision system and Platform class must exist
- US003: Constants must be defined
