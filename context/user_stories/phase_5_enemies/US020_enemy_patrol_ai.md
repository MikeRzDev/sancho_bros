# US020: Implement Enemy Patrol AI

**As a** developer
**I want** to implement patrol AI for Polocho enemies
**So that** enemies move back and forth between boundaries

## Priority
High

## Story Points
5

## Acceptance Criteria

1. **Basic Patrol Movement**
   - [ ] Enemy moves horizontally at constant speed (2 px/frame)
   - [ ] Movement direction alternates between LEFT and RIGHT
   - [ ] Velocity.x set based on facing direction
   - [ ] Position updates each frame

2. **Boundary Detection**
   - [ ] Enemy turns around at `patrol_left` boundary
   - [ ] Enemy turns around at `patrol_right` boundary
   - [ ] Direction changes when boundary reached
   - [ ] Velocity reverses at boundaries

3. **Direction Tracking**
   - [ ] `facing_direction` updates to "LEFT" when moving left
   - [ ] `facing_direction` updates to "RIGHT" when moving right
   - [ ] Direction changes smoothly (no stuttering)

4. **Edge Detection**
   - [ ] Enemy detects platform edges
   - [ ] Enemy turns around before falling off platform
   - [ ] Uses raycast or position check for edge detection
   - [ ] Works with both solid and floating platforms

5. **Gravity Application**
   - [ ] Enemy affected by gravity when not on platform
   - [ ] Enemy falls if platform ends
   - [ ] Enemy lands on platforms below
   - [ ] Vertical velocity capped at MAX_FALL_SPEED

6. **Collision with Platforms**
   - [ ] Enemy detects platform collisions
   - [ ] Enemy stays on top of platforms
   - [ ] Enemy doesn't fall through platforms
   - [ ] Uses collision system from US013

7. **Patrol Behavior**
   - [ ] Continuous back-and-forth movement
   - [ ] No pausing at boundaries
   - [ ] Smooth turnaround animation/behavior
   - [ ] Predictable and consistent

8. **Visual Validation**
   - [ ] All enemies patrol correctly in Level 1
   - [ ] Enemies don't fall off platforms
   - [ ] Enemies turn at correct boundaries
   - [ ] Multiple enemies patrol independently

## Technical Notes

```python
# In Polocho class:
def update(self, dt, platforms):
    """Update enemy state"""
    if not self.is_alive:
        return

    # Patrol movement
    self.patrol()

    # Apply gravity
    from src.physics.gravity import apply_gravity
    self.is_grounded = False
    apply_gravity(self, dt)

    # Update position
    self.position.x += self.velocity.x
    self.position.y += self.velocity.y

    # Check collisions with platforms
    from src.physics.collision import resolve_platform_collision
    resolve_platform_collision(self, platforms)

    # Update rect
    self.rect.x = self.position.x
    self.rect.y = self.position.y

def patrol(self):
    """Handle patrol movement"""
    # Move in current direction
    if self.facing_direction == "RIGHT":
        self.velocity.x = self.speed

        # Check right boundary
        if self.position.x >= self.patrol_right:
            self.facing_direction = "LEFT"
            self.position.x = self.patrol_right  # Snap to boundary

    elif self.facing_direction == "LEFT":
        self.velocity.x = -self.speed

        # Check left boundary
        if self.position.x <= self.patrol_left:
            self.facing_direction = "RIGHT"
            self.position.x = self.patrol_left  # Snap to boundary

def check_edge(self, platforms):
    """Check if enemy is about to fall off platform (optional)"""
    # Check if there's ground ahead
    # If no platform ahead, turn around
    pass  # Implement if needed for safety
```

**Advanced Edge Detection (Optional):**
```python
def is_platform_ahead(self, platforms):
    """Check if there's a platform in front of enemy"""
    check_distance = self.width + 5
    check_x = (self.position.x + check_distance if self.facing_direction == "RIGHT"
               else self.position.x - check_distance)
    check_y = self.position.y + self.height + 5

    for platform in platforms:
        if platform.rect.collidepoint(check_x, check_y):
            return True
    return False
```

## Dependencies
- US019: Enemy class must exist
- US011: Gravity system must exist
- US013: Collision system must work
