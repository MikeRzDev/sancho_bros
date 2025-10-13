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
   - [ ] `src/physics/gravity.py` exists
   - [ ] `apply_gravity(entity, dt)` function is defined

2. **Gravity Behavior**
   - [ ] Gravity adds GRAVITY constant to vertical velocity each frame
   - [ ] Velocity increases by 0.8 pixels/frame² (downward)
   - [ ] Vertical velocity is capped at MAX_FALL_SPEED (15)
   - [ ] Gravity only applies when entity is not grounded

3. **Player Physics Integration**
   - [ ] Player's `update()` method calls gravity system
   - [ ] Player falls when not on a platform
   - [ ] Player velocity accumulates correctly
   - [ ] Position updates based on velocity: `position += velocity * dt`

4. **Jump Mechanics**
   - [ ] `jump()` method sets velocity.y to JUMP_STRENGTH (-15)
   - [ ] Jump only works when `is_grounded` is True
   - [ ] Sets `is_jumping` to True
   - [ ] Sets `is_grounded` to False

5. **Grounded Detection**
   - [ ] Player is grounded when standing on a platform
   - [ ] `is_grounded` flag is set correctly
   - [ ] Vertical velocity resets to 0 when landing
   - [ ] `is_jumping` set to False when grounded

6. **Visual Validation**
   - [ ] Player falls when spawned in air
   - [ ] Player accelerates downward over time
   - [ ] Fall speed caps at MAX_FALL_SPEED
   - [ ] Pressing space makes player jump

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
