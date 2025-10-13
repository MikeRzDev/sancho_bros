# US013: Implement Collision Detection System

**As a** developer
**I want** to create a collision detection system
**So that** the player can stand on platforms and not fall through them

## Priority
Critical

## Story Points
8

## Acceptance Criteria

1. **Collision Module Created**
   - [ ] `src/physics/collision.py` exists
   - [ ] Functions defined for collision checking:
     - `check_aabb_collision(rect1, rect2)`: AABB collision detection
     - `resolve_platform_collision(entity, platforms)`: Platform collision resolution

2. **AABB Collision Detection**
   - [ ] Returns True if two rectangles overlap
   - [ ] Checks all four edges correctly
   - [ ] Works with pygame.Rect objects

3. **Platform Collision Resolution**
   - [ ] Detects collision between player and platform
   - [ ] Determines collision side (top, bottom, left, right)
   - [ ] Resolves collision by adjusting player position
   - [ ] Sets appropriate flags (`is_grounded`, etc.)

4. **Top Collision (Landing)**
   - [ ] Player lands on platform when falling (velocity.y > 0)
   - [ ] Player positioned exactly on platform surface
   - [ ] Vertical velocity set to 0
   - [ ] `is_grounded` set to True
   - [ ] Player can walk on platform

5. **Bottom Collision (Head Bump)**
   - [ ] Player hits bottom of platform when jumping up
   - [ ] Vertical velocity set to 0 (stops upward movement)
   - [ ] Player starts falling after collision

6. **Side Collisions (Walls)**
   - [ ] Player stops when hitting left side of platform
   - [ ] Player stops when hitting right side of platform
   - [ ] Horizontal velocity set to 0 on wall collision
   - [ ] Player slides down wall if in air

7. **Platform Class Created**
   - [ ] `src/level/tile.py` exists
   - [ ] `Platform` class defined with:
     - `__init__(x, y, width, height, type)`
     - `rect`: pygame.Rect for collision
     - `render(screen, camera)`: Draw platform

8. **Integration with Player**
   - [ ] Player's `update()` calls collision resolution
   - [ ] Player receives list of platforms to check
   - [ ] Collision checked every frame
   - [ ] Works with multiple platforms

9. **Visual Validation**
   - [ ] Player stands on platform without falling through
   - [ ] Player stops at edges and walls
   - [ ] Player can jump from platform
   - [ ] Multiple platforms work correctly

## Technical Notes

```python
# src/physics/collision.py
import pygame

def check_aabb_collision(rect1, rect2):
    """Axis-Aligned Bounding Box collision"""
    return rect1.colliderect(rect2)

def resolve_platform_collision(entity, platforms):
    """Resolve collisions between entity and platforms"""
    entity.is_grounded = False

    for platform in platforms:
        if check_aabb_collision(entity.rect, platform.rect):
            # Calculate overlap on each axis
            overlap_x = min(entity.rect.right - platform.rect.left,
                           platform.rect.right - entity.rect.left)
            overlap_y = min(entity.rect.bottom - platform.rect.top,
                           platform.rect.bottom - entity.rect.top)

            # Resolve smallest overlap (most likely collision side)
            if overlap_x < overlap_y:
                # Side collision
                if entity.rect.centerx < platform.rect.centerx:
                    # Colliding from left
                    entity.position.x = platform.rect.left - entity.width
                    entity.velocity.x = 0
                else:
                    # Colliding from right
                    entity.position.x = platform.rect.right
                    entity.velocity.x = 0
            else:
                # Top/bottom collision
                if entity.velocity.y > 0:
                    # Landing on top
                    entity.position.y = platform.rect.top - entity.height
                    entity.velocity.y = 0
                    entity.is_grounded = True
                    entity.is_jumping = False
                elif entity.velocity.y < 0:
                    # Hitting bottom
                    entity.position.y = platform.rect.bottom
                    entity.velocity.y = 0

            # Update rect
            entity.rect.x = entity.position.x
            entity.rect.y = entity.position.y

# src/level/tile.py
class Platform:
    def __init__(self, x, y, width, height, platform_type):
        self.rect = pygame.Rect(x, y, width, height)
        self.type = platform_type  # "solid" or "floating"

    def render(self, screen, camera):
        screen_x = self.rect.x - camera.x
        screen_y = self.rect.y - camera.y
        color = (139, 69, 19) if self.type == "solid" else (100, 100, 100)
        pygame.draw.rect(screen, color, (screen_x, screen_y,
                        self.rect.width, self.rect.height))
```

## Dependencies
- US010: Player class must exist
- US011: Physics system must work
