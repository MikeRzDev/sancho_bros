# US011: Implement Gravity and Physics System

**As a** developer
**I want** to implement gravity and basic physics
**So that** the player falls realistically and can jump

## Priority
Critical

## Story Points
5

## Acceptance Criteria

1. **Gravity Module Created**
   - [x] `src/physics/gravity.py` exists
   - [x] `apply_gravity(entity, dt)` function is defined

2. **Gravity Behavior**
   - [x] Gravity adds GRAVITY constant to vertical velocity each frame
   - [x] Velocity increases by 0.8 pixels/frame² (downward)
   - [x] Vertical velocity is capped at MAX_FALL_SPEED (15)
   - [x] Gravity only applies when entity is not grounded

3. **Player Physics Integration**
   - [x] Player's `update()` method calls gravity system
   - [x] Player falls when not on a platform
   - [x] Player velocity accumulates correctly
   - [x] Position updates based on velocity: `position += velocity * dt`

4. **Jump Mechanics**
   - [x] `jump()` method sets velocity.y to JUMP_STRENGTH (-15)
   - [x] Jump only works when `is_grounded` is True
   - [x] Sets `is_jumping` to True
   - [x] Sets `is_grounded` to False

5. **Grounded Detection**
   - [x] Player is grounded when standing on a platform
   - [x] `is_grounded` flag is set correctly
   - [x] Vertical velocity resets to 0 when landing
   - [x] `is_jumping` set to False when grounded

6. **Visual Validation**
   - [x] Player falls when spawned in air
   - [x] Player accelerates downward over time
   - [x] Fall speed caps at MAX_FALL_SPEED
   - [x] Pressing space makes player jump

## Technical Notes

```python
# src/physics/gravity.py
from src.constants import GRAVITY, MAX_FALL_SPEED

def apply_gravity(entity, dt):
    """Apply gravity to an entity"""
    if not entity.is_grounded:
        entity.velocity.y += GRAVITY
        # Cap fall speed
        if entity.velocity.y > MAX_FALL_SPEED:
            entity.velocity.y = MAX_FALL_SPEED

# In Player class:
def update(self, dt, platforms):
    # Apply physics
    from src.physics.gravity import apply_gravity
    apply_gravity(self, dt)

    # Update position
    self.position.x += self.velocity.x
    self.position.y += self.velocity.y

    # Update rect
    self.rect.x = self.position.x
    self.rect.y = self.position.y

def jump(self):
    if self.is_grounded:
        self.velocity.y = JUMP_STRENGTH
        self.is_jumping = True
        self.is_grounded = False
```

- Frame-independent physics: multiply by dt if needed
- Y-axis increases downward (standard pygame convention)
- Gravity should feel responsive but not floaty

## Dependencies
- US010: Player class must exist
- US003: Constants must be defined
