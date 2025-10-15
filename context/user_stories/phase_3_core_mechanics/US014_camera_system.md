# US014: Implement Camera/Viewport System

**As a** developer
**I want** to create a camera that follows the player
**So that** levels larger than the screen can be navigated

## Priority
High

## Story Points
5

## Acceptance Criteria

1. **Camera Class Created**
   - [x] `src/camera.py` exists
   - [x] `Camera` class is defined

2. **Camera Attributes**
   - [x] `x`, `y`: Camera position in world coordinates
   - [x] `width`, `height`: Viewport dimensions (SCREEN_WIDTH, SCREEN_HEIGHT)
   - [x] `target`: Reference to player object
   - [x] `level_width`: Maximum camera boundary

3. **Camera Methods**
   - [x] `__init__(width, height)`: Initialize camera
   - [x] `update(target_pos, level_width)`: Follow target smoothly
   - [x] `apply(world_pos)`: Transform world coords to screen coords
   - [x] `is_visible(entity)`: Check if entity is in viewport

4. **Camera Following Behavior**
   - [x] Camera centers on player horizontally
   - [x] Camera follows player smoothly (no jittering)
   - [x] Camera doesn't move beyond level boundaries:
     - Left boundary: camera.x >= 0
     - Right boundary: camera.x <= level_width - SCREEN_WIDTH
   - [x] Camera keeps player visible at all times

5. **Boundary Handling**
   - [x] When level_width < SCREEN_WIDTH: camera stays at x=0
   - [x] Camera stops at left edge (x=0)
   - [x] Camera stops at right edge (level_width - SCREEN_WIDTH)
   - [x] Smooth behavior at boundaries (no jumping)

6. **Coordinate Transformation**
   - [x] `apply()` returns screen coordinates from world coordinates
   - [x] Formula: screen_x = world_x - camera.x
   - [x] All entities render using camera.apply()

7. **Integration**
   - [x] Camera updates in game loop before rendering
   - [x] Camera passed to all render() methods
   - [x] Player stays centered (or near center) in viewport
   - [x] Platforms scroll smoothly with camera

8. **Validation**
   - [x] Player remains visible during all movement
   - [x] Level scrolls smoothly left and right
   - [x] No tearing or stuttering
   - [x] Camera stops at level edges correctly

## Technical Notes

```python
# src/camera.py
import pygame
from src.constants import SCREEN_WIDTH, SCREEN_HEIGHT

class Camera:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.x = 0
        self.y = 0
        self.target = None
        self.level_width = 0

    def update(self, target_pos, level_width):
        """Update camera to follow target"""
        self.level_width = level_width

        # Center camera on target horizontally
        self.x = target_pos.x - self.width // 2

        # Clamp to level boundaries
        self.x = max(0, self.x)  # Left boundary
        self.x = min(self.x, level_width - self.width)  # Right boundary

        # Keep camera at y=0 for 2D side-scroller
        self.y = 0

    def apply(self, world_pos):
        """Transform world coordinates to screen coordinates"""
        return world_pos.x - self.x, world_pos.y - self.y

    def is_visible(self, entity):
        """Check if entity is visible in viewport"""
        return (entity.rect.right > self.x and
                entity.rect.left < self.x + self.width)

# In Game class:
def __init__(self):
    # ...
    self.camera = Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

def update(self, dt):
    # Update player
    self.player.update(dt, platforms)

    # Update camera to follow player
    self.camera.update(self.player.position, level_width)

def render(self):
    # All rendering uses camera
    self.player.render(self.screen, self.camera)
    for platform in platforms:
        platform.render(self.screen, self.camera)
```

## Dependencies
- US010: Player class must exist
- US004: Game window must exist
