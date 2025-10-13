# US025: Implement Power-Up Collection System

**As a** developer
**I want** to implement power-up collection mechanics
**So that** players can collect La Arepa Dorada and gain abilities

## Priority
High

## Story Points
5

## Acceptance Criteria

1. **Collection Detection**
   - [ ] Game checks for power-up collision each frame
   - [ ] Uses `check_collection(player)` method
   - [ ] Checks all power-ups in current level

2. **Collection Effect on Player**
   - [ ] Player's `has_powerup` flag set to True
   - [ ] Player's `powerup_timer` set to LASER_DURATION (10 seconds)
   - [ ] Collection triggers `collect_powerup()` method on player

3. **Player Power-Up State**
   - [ ] `collect_powerup()` method in Player class
   - [ ] Activates laser ability
   - [ ] Sets timer for duration
   - [ ] Enables shooting (prepared for US026)

4. **Timer Countdown**
   - [ ] `powerup_timer` decreases each frame (dt)
   - [ ] When timer reaches 0: `has_powerup` = False
   - [ ] Power-up deactivates automatically
   - [ ] Timer updated in player's `update()` method

5. **Collection Feedback**
   - [ ] Power-up disappears when collected
   - [ ] Visual indication player has power (placeholder)
   - [ ] Print message confirming collection
   - [ ] Prepared for sound effect (Phase 7)

6. **Re-Collection Prevention**
   - [ ] Collected power-ups stay collected
   - [ ] Same power-up can't be collected twice
   - [ ] Collected power-ups don't render
   - [ ] Collected power-ups don't check collision

7. **Multiple Power-Ups**
   - [ ] Can collect multiple power-ups in one level
   - [ ] Each collection resets timer to full duration
   - [ ] Timer doesn't stack (resets to 10s, not adds)

8. **Visual Timer Indicator**
   - [ ] Player color changes when powered (optional placeholder)
   - [ ] OR text indicator shown (temporary)
   - [ ] Clear indication of powered state

9. **Validation**
   - [ ] Walking through power-up collects it
   - [ ] Power-up disappears after collection
   - [ ] Timer counts down correctly
   - [ ] Power-up expires after 10 seconds
   - [ ] Multiple power-ups work correctly

## Technical Notes

```python
# In Player class:
def __init__(self, x, y):
    # ... existing code ...
    self.has_powerup = False
    self.powerup_timer = 0.0
    self.laser_cooldown = 0.0

def update(self, dt, platforms):
    # ... existing update code ...

    # Update power-up timer
    if self.has_powerup:
        self.powerup_timer -= dt
        if self.powerup_timer <= 0:
            self.has_powerup = False
            self.powerup_timer = 0.0
            print("Power-up expired")

    # Update laser cooldown
    if self.laser_cooldown > 0:
        self.laser_cooldown -= dt

def collect_powerup(self):
    """Activate power-up effect"""
    self.has_powerup = True
    self.powerup_timer = LASER_DURATION
    print(f"Power-up activated! Duration: {LASER_DURATION}s")

def render(self, screen, camera):
    """Draw player"""
    screen_x = self.position.x - camera.x
    screen_y = self.position.y - camera.y

    # Change color if powered (optional)
    color = (255, 255, 0) if self.has_powerup else COLOR_PLAYER

    pygame.draw.rect(screen, color,
                    (screen_x, screen_y, self.width, self.height))

# In Level or Game update:
def update(self, dt):
    # ... existing updates ...

    # Check power-up collection
    for powerup in self.current_level.powerups:
        if powerup.check_collection(self.player):
            powerup.collect()
            self.player.collect_powerup()

# Optional - Timer display (temporary):
def render(self):
    # ... existing rendering ...

    # Display power-up timer
    if self.player.has_powerup:
        font = pygame.font.Font(None, 36)
        timer_text = f"POWER: {int(self.player.powerup_timer)}s"
        text_surface = font.render(timer_text, True, (255, 255, 0))
        self.screen.blit(text_surface, (10, 10))
```

**Advanced - Visual Glow Effect (Optional):**
```python
def render(self, screen, camera):
    """Draw player with glow if powered"""
    screen_x = self.position.x - camera.x
    screen_y = self.position.y - camera.y

    # Draw glow if powered
    if self.has_powerup:
        glow_rect = pygame.Rect(
            screen_x - 5, screen_y - 5,
            self.width + 10, self.height + 10
        )
        pygame.draw.rect(screen, (255, 255, 0), glow_rect, 3)

    # Draw player
    pygame.draw.rect(screen, COLOR_PLAYER,
                    (screen_x, screen_y, self.width, self.height))
```

## Dependencies
- US024: PowerUp class must exist
- US010: Player class must exist
- US003: Constants must be defined (LASER_DURATION)
