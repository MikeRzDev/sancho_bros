# US012: Implement Player Movement and Controls

**As a** developer
**I want** to implement player movement and keyboard controls
**So that** players can control Sancho's horizontal movement

## Priority
Critical

## Story Points
3

## Acceptance Criteria

1. **Horizontal Movement**
   - [x] LEFT arrow / A key: Move left at PLAYER_SPEED
   - [x] RIGHT arrow / D key: Move right at PLAYER_SPEED
   - [x] Velocity.x set to PLAYER_SPEED (5 pixels/frame) when moving
   - [x] Velocity.x set to 0 when no keys pressed
   - [x] Movement works while in air (not restricted to ground)

2. **Direction Tracking**
   - [x] `facing_direction` updates to "LEFT" when moving left
   - [x] `facing_direction` updates to "RIGHT" when moving right
   - [x] Direction persists when not moving (remembers last direction)

3. **Jump Control**
   - [x] SPACE key triggers jump
   - [x] Jump only works when grounded
   - [x] Jump cannot be held for continuous jumping
   - [x] Requires key release and repress for next jump

4. **Input Handling**
   - [x] `handle_input(keys)` method processes pygame key states
   - [x] Uses `pygame.key.get_pressed()` for continuous input
   - [x] Responsive controls (no input lag)

5. **Movement Smoothness**
   - [x] Movement is smooth and consistent
   - [x] No stuttering or jittering
   - [x] Direction changes are immediate
   - [x] Feels responsive at 60 FPS

6. **Integration**
   - [x] `handle_input()` called in player's `update()` method
   - [x] Controls work in game loop
   - [x] Player can move left, right, and jump simultaneously

## Technical Notes

```python
# In Player class:
def handle_input(self, keys):
    """Process keyboard input"""
    # Horizontal movement
    self.velocity.x = 0

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        self.velocity.x = -PLAYER_SPEED
        self.facing_direction = "LEFT"
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        self.velocity.x = PLAYER_SPEED
        self.facing_direction = "RIGHT"

    # Jump (handled via event in game.py to prevent holding)
    # OR check for key press separately:
    if keys[pygame.K_SPACE]:
        self.jump()

def update(self, dt, platforms):
    # Get input
    keys = pygame.key.get_pressed()
    self.handle_input(keys)

    # Apply physics and gravity
    # ... (from US011)
```

Alternative jump handling (in game.py event loop):
```python
for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            player.jump()
```

- Consider adding acceleration/deceleration for smoother feel (optional)
- Ensure movement works with both arrow keys and WASD
- Prevent "bunny hopping" by requiring key release

## Dependencies
- US010: Player class must exist
- US011: Physics system must work
