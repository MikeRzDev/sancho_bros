# US032: Create Pause Menu and Game Over Screen

**As a** developer
**I want** to create pause and game over UI screens
**So that** players can pause gameplay and handle game over scenarios

## Priority
High

## Story Points
5

## Acceptance Criteria

### Pause Menu

1. **Pause Screen Display**
   - [x] Semi-transparent overlay over game world
   - [x] "PAUSED" title displayed prominently
   - [x] Menu options shown:
     - "Resume" (ENTER or ESC)
     - "Restart Level" (R)
     - "Main Menu" (M)
   - [x] Game world visible but dimmed behind overlay

2. **Pause Menu Functionality**
   - [x] ESC or P key pauses game
   - [x] ESC or ENTER resumes game
   - [x] R key restarts current level
   - [x] M key returns to main menu
   - [x] Cannot pause in MENU or GAME_OVER states

3. **Pause Overlay Rendering**
   - [x] Dark semi-transparent background (alpha ~128)
   - [x] White text for visibility
   - [x] Centered on screen
   - [x] Large, readable fonts

### Game Over Screen

4. **Game Over Display**
   - [x] "GAME OVER" title displayed
   - [x] Reason shown (if applicable)
   - [x] Final statistics:
     - Level reached
     - Enemies defeated (optional)
   - [x] Options:
     - "Retry" (R) - restart from Level 1
     - "Main Menu" (M)

5. **Game Over Trigger**
   - [x] Triggered when player.lives reaches 0
   - [x] State changes to GAME_OVER
   - [x] Game stops updating

6. **Game Over Functionality**
   - [x] R key restarts game from Level 1
   - [x] M key returns to main menu
   - [x] ESC also returns to menu
   - [x] Player lives reset on restart

7. **Visual Design**
   - [x] Clear indication of game over
   - [x] Not too harsh/jarring
   - [x] Professional appearance
   - [x] Easy to read options

### Integration

8. **Pause Integration**
   - [x] Pausing works at any time during gameplay
   - [x] Game state preserved when paused
   - [x] Resuming continues from exact state
   - [x] No game logic runs while paused

9. **Game Over Integration**
   - [x] Game over triggers on zero lives
   - [x] Restart functionality works correctly
   - [x] Player and level reset properly
   - [x] No errors during restart

10. **Validation**
    - [x] Can pause and unpause smoothly
    - [x] Pause menu options all work
    - [x] Game over screen appears correctly
    - [x] Retry starts fresh game
    - [x] Return to menu works from both screens

## Technical Notes

```python
# src/ui/screens.py
import pygame
from src.constants import *

class PauseMenu:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.title_font = pygame.font.Font(None, 72)
        self.option_font = pygame.font.Font(None, 36)

    def render(self, screen):
        """Render pause menu overlay"""
        # Semi-transparent overlay
        overlay = pygame.Surface((self.screen_width, self.screen_height))
        overlay.set_alpha(128)
        overlay.fill((0, 0, 0))
        screen.blit(overlay, (0, 0))

        # Title
        title = self.title_font.render("PAUSED", True, (255, 255, 255))
        title_rect = title.get_rect(center=(self.screen_width // 2, 200))
        screen.blit(title, title_rect)

        # Options
        options = [
            "ENTER / ESC: Resume",
            "R: Restart Level",
            "M: Main Menu"
        ]
        y_start = 300
        for i, text in enumerate(options):
            option = self.option_font.render(text, True, (200, 200, 200))
            option_rect = option.get_rect(center=(self.screen_width // 2, y_start + i * 50))
            screen.blit(option, option_rect)

class GameOverScreen:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.title_font = pygame.font.Font(None, 72)
        self.option_font = pygame.font.Font(None, 36)
        self.info_font = pygame.font.Font(None, 28)

    def render(self, screen, level_reached):
        """Render game over screen"""
        # Background
        screen.fill((20, 20, 20))

        # Title
        title = self.title_font.render("GAME OVER", True, (255, 50, 50))
        title_rect = title.get_rect(center=(self.screen_width // 2, 150))
        screen.blit(title, title_rect)

        # Info
        info_text = f"Reached Level {level_reached}"
        info = self.info_font.render(info_text, True, (200, 200, 200))
        info_rect = info.get_rect(center=(self.screen_width // 2, 250))
        screen.blit(info, info_rect)

        # Options
        options = [
            "R: Retry from Level 1",
            "M: Main Menu"
        ]
        y_start = 350
        for i, text in enumerate(options):
            option = self.option_font.render(text, True, (200, 200, 200))
            option_rect = option.get_rect(center=(self.screen_width // 2, y_start + i * 50))
            screen.blit(option, option_rect)

# In Game class:
def __init__(self):
    # ... existing code ...
    from src.ui.screens import PauseMenu, GameOverScreen
    self.pause_menu = PauseMenu(SCREEN_WIDTH, SCREEN_HEIGHT)
    self.game_over_screen = GameOverScreen(SCREEN_WIDTH, SCREEN_HEIGHT)

def render_pause_overlay(self):
    """Render pause menu"""
    self.pause_menu.render(self.screen)

def render_game_over(self):
    """Render game over screen"""
    self.game_over_screen.render(self.screen, self.current_level_number)

def handle_events(self):
    for event in pygame.event.get():
        # ... existing code ...

        if event.type == pygame.KEYDOWN:
            # Pause handling
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_p:
                if self.state == GameState.PLAYING:
                    self.change_state(GameState.PAUSED)
                elif self.state == GameState.PAUSED:
                    self.change_state(GameState.PLAYING)

            # Paused state inputs
            if self.state == GameState.PAUSED:
                if event.key == pygame.K_RETURN:
                    self.change_state(GameState.PLAYING)
                if event.key == pygame.K_r:
                    self.restart_level()
                if event.key == pygame.K_m:
                    self.change_state(GameState.MENU)

            # Game over state inputs
            if self.state == GameState.GAME_OVER:
                if event.key == pygame.K_r:
                    self.restart_game()
                if event.key == pygame.K_m or event.key == pygame.K_ESCAPE:
                    self.change_state(GameState.MENU)

def restart_level(self):
    """Restart current level"""
    self.load_level(self.current_level_number)
    spawn = self.current_level.get_spawn_position()
    self.player.position.x = spawn[0]
    self.player.position.y = spawn[1]
    self.player.velocity = pygame.Vector2(0, 0)
    self.lasers = []
    self.change_state(GameState.PLAYING)

def restart_game(self):
    """Restart game from Level 1"""
    self.load_level(1)
    spawn = self.current_level.get_spawn_position()
    self.player = Player(spawn[0], spawn[1])
    self.lasers = []
    self.change_state(GameState.PLAYING)
```

## Dependencies
- US029: Game state management must exist
- US004: Game window must exist
