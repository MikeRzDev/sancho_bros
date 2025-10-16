# US031: Create HUD (Heads-Up Display)

**As a** developer
**I want** to create a HUD that displays game information
**So that** players can see lives, level number, and power-up status

## Priority
High

## Story Points
3

## Acceptance Criteria

1. **HUD Class Created**
   - [x] `src/ui/hud.py` exists
   - [x] `HUD` class is defined

2. **Lives Display**
   - [x] Shows remaining lives (1-3)
   - [x] Displays as hearts or numeric counter
   - [x] Updates in real-time
   - [x] Positioned in top-left corner

3. **Level Number Display**
   - [x] Shows current level (1-5)
   - [x] Format: "Level 1" or "LVL 1"
   - [x] Positioned in top-center or top-right
   - [x] Updates on level change

4. **Power-Up Timer Display**
   - [x] Shows remaining power-up time
   - [x] Only visible when player has power-up
   - [x] Format: "POWER: 10s" or progress bar
   - [x] Updates each second
   - [x] Positioned near lives display

5. **HUD Rendering**
   - [x] Renders over game world (always visible)
   - [x] Not affected by camera position
   - [x] Clear and readable fonts
   - [x] Good contrast against background

6. **HUD Update**
   - [x] `render(player, level)` method (note: uses render, not update)
   - [x] Pulls current data from player and level
   - [x] Updates displays accordingly

7. **Visual Design**
   - [x] Clean, minimal design
   - [x] Doesn't obscure gameplay
   - [x] Uses consistent colors
   - [x] Readable at 800x600 resolution

8. **Hearts Display (Optional)**
   - [ ] Shows 3 heart icons for lives
   - [ ] Filled hearts for remaining lives
   - [ ] Empty/grayed hearts for lost lives
   - [ ] Icons ~24x24 pixels

9. **Integration with Game**
   - [x] HUD updated in game loop
   - [x] HUD rendered in PLAYING state
   - [x] Also rendered in PAUSED state
   - [x] Not rendered in MENU or GAME_OVER

10. **Validation**
    - [x] Lives display shows correct count
    - [x] Lives update when player takes damage
    - [x] Level number correct for each level
    - [x] Power-up timer shows and counts down
    - [x] HUD visible during gameplay

## Technical Notes

```python
# src/ui/hud.py
import pygame
from src.constants import *

class HUD:
    def __init__(self):
        self.font = pygame.font.Font(None, 32)
        self.small_font = pygame.font.Font(None, 24)

    def render(self, screen, player, level):
        """Render HUD elements"""
        # Lives display
        lives_text = f"Lives: {player.lives}"
        lives_surface = self.font.render(lives_text, True, (255, 255, 255))
        screen.blit(lives_surface, (10, 10))

        # Level number
        level_text = f"Level {level.level_number}"
        level_surface = self.font.render(level_text, True, (255, 255, 255))
        level_rect = level_surface.get_rect(topright=(SCREEN_WIDTH - 10, 10))
        screen.blit(level_surface, level_rect)

        # Power-up timer (if active)
        if player.has_powerup:
            timer = int(player.powerup_timer)
            power_text = f"POWER: {timer}s"
            power_surface = self.font.render(power_text, True, (255, 215, 0))
            screen.blit(power_surface, (10, 50))

# In Game class:
def __init__(self):
    # ... existing code ...
    from src.ui.hud import HUD
    self.hud = HUD()

def render(self):
    """Render based on current state"""
    if self.state == GameState.PLAYING or self.state == GameState.PAUSED:
        # Render game world
        self.current_level.render(self.screen, self.camera)
        self.player.render(self.screen, self.camera)
        for laser in self.lasers:
            laser.render(self.screen, self.camera)

        # Render HUD on top
        self.hud.render(self.screen, self.player, self.current_level)

    # ... rest of rendering ...
```

**Optional - Hearts Display:**
```python
class HUD:
    def __init__(self):
        self.font = pygame.font.Font(None, 32)
        self.heart_size = 24

    def render_hearts(self, screen, lives):
        """Render hearts for lives"""
        for i in range(3):
            x = 10 + i * (self.heart_size + 5)
            y = 10

            if i < lives:
                # Filled heart (red)
                color = (255, 0, 0)
            else:
                # Empty heart (gray)
                color = (100, 100, 100)

            # Draw simple heart shape (or use sprite)
            pygame.draw.circle(screen, color, (x + 6, y + 8), 8)
            pygame.draw.circle(screen, color, (x + 18, y + 8), 8)
            pygame.draw.polygon(screen, color, [
                (x, y + 10),
                (x + 12, y + 22),
                (x + 24, y + 10)
            ])

    def render(self, screen, player, level):
        # Render hearts instead of text
        self.render_hearts(screen, player.lives)

        # ... rest of HUD ...
```

**Optional - Power-Up Progress Bar:**
```python
def render_power_bar(self, screen, player):
    """Render power-up progress bar"""
    if not player.has_powerup:
        return

    bar_width = 150
    bar_height = 20
    x, y = 10, 50

    # Background
    pygame.draw.rect(screen, (50, 50, 50), (x, y, bar_width, bar_height))

    # Foreground (filled portion)
    filled_width = int(bar_width * (player.powerup_timer / LASER_DURATION))
    pygame.draw.rect(screen, (255, 215, 0), (x, y, filled_width, bar_height))

    # Border
    pygame.draw.rect(screen, (255, 255, 255), (x, y, bar_width, bar_height), 2)

    # Text
    timer_text = f"POWER: {int(player.powerup_timer)}s"
    text_surface = self.small_font.render(timer_text, True, (255, 255, 255))
    screen.blit(text_surface, (x, y + bar_height + 5))
```

## Dependencies
- US010: Player class must exist
- US016: Level class must exist
- US029: Game state management must exist
