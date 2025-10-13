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
   - [ ] LEFT arrow / A key: Move left at PLAYER_SPEED
   - [ ] RIGHT arrow / D key: Move right at PLAYER_SPEED
   - [ ] Velocity.x set to PLAYER_SPEED (5 pixels/frame) when moving
   - [ ] Velocity.x set to 0 when no keys pressed
   - [ ] Movement works while in air (not restricted to ground)

2. **Direction Tracking**
   - [ ] `facing_direction` updates to "LEFT" when moving left
   - [ ] `facing_direction` updates to "RIGHT" when moving right
   - [ ] Direction persists when not moving (remembers last direction)

3. **Jump Control**
   - [ ] SPACE key triggers jump
   - [ ] Jump only works when grounded
   - [ ] Jump cannot be held for continuous jumping
   - [ ] Requires key release and repress for next jump

4. **Input Handling**
   - [ ] `handle_input(keys)` method processes pygame key states
   - [ ] Uses `pygame.key.get_pressed()` for continuous input
   - [ ] Responsive controls (no input lag)

5. **Movement Smoothness**
   - [ ] Movement is smooth and consistent
   - [ ] No stuttering or jittering
   - [ ] Direction changes are immediate
   - [ ] Feels responsive at 60 FPS

6. **Integration**
   - [ ] `handle_input()` called in player's `update()` method
   - [ ] Controls work in game loop
   - [ ] Player can move left, right, and jump simultaneously

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
