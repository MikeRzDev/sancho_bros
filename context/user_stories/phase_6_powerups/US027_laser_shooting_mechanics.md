# US027: Implement Laser Shooting Mechanics

**As a** developer
**I want** to implement the laser shooting mechanic
**So that** players can shoot lasers when powered up

## Priority
High

## Story Points
5

## Acceptance Criteria

1. **Shoot Input Handling**
   - [ ] X key triggers laser shooting
   - [ ] Left Ctrl key also triggers laser shooting
   - [ ] Input handled via event or key press
   - [ ] Works while player is moving

2. **Shooting Conditions**
   - [ ] Can only shoot when `has_powerup` is True
   - [ ] Cannot shoot during cooldown
   - [ ] Shooting respects LASER_COOLDOWN (0.5 seconds)
   - [ ] Clear feedback when unable to shoot

3. **Laser Creation**
   - [ ] `shoot_laser()` method in Player class
   - [ ] Creates new Laser object
   - [ ] Laser spawns at player position (slightly ahead)
   - [ ] Laser direction matches player's `facing_direction`
   - [ ] Laser added to game's laser list

4. **Shooting Cooldown**
   - [ ] `laser_cooldown` timer prevents rapid firing
   - [ ] Cooldown set to LASER_COOLDOWN after each shot
   - [ ] Cooldown decreases each frame (dt)
   - [ ] Can shoot again when cooldown <= 0

5. **Laser Positioning**
   - [ ] Laser spawns slightly in front of player
   - [ ] Vertical position centered on player
   - [ ] Doesn't spawn inside player
   - [ ] Position calculation:
     - x: player.x + player.width (RIGHT) or player.x - laser.width (LEFT)
     - y: player.y + player.height/2 - laser.height/2

6. **Multiple Laser Management**
   - [ ] Multiple lasers can exist simultaneously
   - [ ] Each laser tracked independently
   - [ ] Inactive lasers removed from list
   - [ ] No limit on active laser count (respects cooldown)

7. **Visual Feedback**
   - [ ] Muzzle flash or indicator when shooting (optional)
   - [ ] Laser visible immediately after shooting
   - [ ] Direction clearly visible
   - [ ] Prepared for sound effect (Phase 7)

8. **Integration with Power-Up**
   - [ ] Shooting only available when powered
   - [ ] Shooting disabled when power-up expires
   - [ ] Can shoot immediately after collection
   - [ ] Timer doesn't interfere with cooldown

9. **Validation**
   - [ ] Pressing X while powered shoots laser
   - [ ] Laser travels in correct direction
   - [ ] Cooldown prevents rapid fire
   - [ ] Cannot shoot without power-up
   - [ ] Can shoot multiple lasers with cooldown
   - [ ] Lasers defeat enemies on hit

## Technical Notes

```python
# In Player class:
def shoot_laser(self):
    """Shoot a laser projectile"""
    # Check conditions
    if not self.has_powerup:
        return None

    if self.laser_cooldown > 0:
        return None

    # Calculate spawn position
    if self.facing_direction == "RIGHT":
        laser_x = self.position.x + self.width
    else:
        laser_x = self.position.x - 16  # Laser width

    laser_y = self.position.y + self.height // 2 - 2  # Center vertically

    # Create laser
    from src.entities.projectile import Laser
    laser = Laser(laser_x, laser_y, self.facing_direction)

    # Set cooldown
    self.laser_cooldown = LASER_COOLDOWN

    print(f"Laser fired {self.facing_direction}")
    return laser

# In Game class handle_events (or update):
def handle_events(self):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            self.running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.player.jump()

            # Laser shooting
            if event.key == pygame.K_x or event.key == pygame.K_LCTRL:
                laser = self.player.shoot_laser()
                if laser:
                    self.lasers.append(laser)

# Alternative - continuous fire (in update, using get_pressed):
def update(self, dt):
    # ... existing updates ...

    keys = pygame.key.get_pressed()
    if keys[pygame.K_x] or keys[pygame.K_LCTRL]:
        laser = self.player.shoot_laser()
        if laser:
            self.lasers.append(laser)
```

**Optional - Muzzle Flash Effect:**
```python
# In Player class:
def __init__(self, x, y):
    # ... existing code ...
    self.muzzle_flash_timer = 0.0

def update(self, dt, platforms):
    # ... existing code ...

    # Update muzzle flash
    if self.muzzle_flash_timer > 0:
        self.muzzle_flash_timer -= dt

def shoot_laser(self):
    # ... existing shoot code ...

    if laser:
        self.muzzle_flash_timer = 0.1  # Brief flash
        return laser

def render(self, screen, camera):
    # ... existing render code ...

    # Draw muzzle flash
    if self.muzzle_flash_timer > 0:
        flash_x = self.position.x + self.width - camera.x
        flash_y = self.position.y + self.height // 2 - camera.y
        if self.facing_direction == "LEFT":
            flash_x = self.position.x - camera.x - 10

        pygame.draw.circle(screen, (255, 255, 255), (int(flash_x), int(flash_y)), 5)
```

## Dependencies
- US026: Laser class must exist
- US025: Power-up collection must work
- US010: Player class must exist
- US003: Constants (LASER_COOLDOWN) must be defined
