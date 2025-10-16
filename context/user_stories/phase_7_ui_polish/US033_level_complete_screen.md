# US033: Create Level Complete Screen and Transitions

**As a** developer
**I want** to create a level completion screen
**So that** players get feedback when completing a level and can proceed to the next

## Priority
Medium

## Story Points
3

## Acceptance Criteria

1. **Level Complete Detection**
   - [x] Triggered when player reaches goal
   - [x] State changes to LEVEL_COMPLETE
   - [x] Game pauses briefly (1-2 seconds) or waits for input

2. **Level Complete Display**
   - [x] "LEVEL COMPLETE!" message shown
   - [x] Current level number displayed
   - [ ] Optional statistics:
     - Time taken
     - Enemies defeated
   - [x] Continue prompt: "Press ENTER to continue"

3. **Completion Screen Rendering**
   - [x] Overlay or full screen
   - [x] Large, celebratory font
   - [x] Positive colors (green, gold)
   - [x] Clear and readable

4. **Auto-Transition (Optional)**
   - [ ] Brief delay (2 seconds) before auto-advancing
   - [x] OR wait for player input (ENTER)
   - [x] Smooth transition to next level

5. **Next Level Loading**
   - [x] Increments level number
   - [x] Loads next level JSON
   - [x] Resets player position
   - [x] Clears lasers and temporary state
   - [x] Returns to PLAYING state

6. **Final Level Completion**
   - [x] Level 5 completion shows "GAME COMPLETE!"
   - [x] Different message/screen
   - [x] Congratulations message
   - [x] Option to return to menu

7. **Player State Persistence**
   - [x] Lives carry over between levels
   - [x] Power-up state does NOT carry over (resets)
   - [ ] Score carries over (if implemented)

8. **Visual Feedback**
   - [x] Celebratory feel
   - [x] Not jarring or abrupt
   - [ ] Optional: simple animation (fade, sparkles)
   - [x] Clear indication of progression

9. **Game Complete Screen**
   - [x] Special screen for completing all 5 levels
   - [x] "CONGRATULATIONS!" message
   - [x] "You saved the coffee harvest!"
   - [x] Return to menu option

10. **Validation**
    - [x] Reaching goal triggers completion
    - [x] Level complete screen displays
    - [x] Can advance to next level
    - [x] Level 5 completion shows game complete
    - [x] Can return to menu after game complete

## Technical Notes

```python
# Add to src/ui/screens.py:
class LevelCompleteScreen:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.title_font = pygame.font.Font(None, 64)
        self.info_font = pygame.font.Font(None, 36)

    def render(self, screen, level_number):
        """Render level complete screen"""
        # Semi-transparent overlay
        overlay = pygame.Surface((self.screen_width, self.screen_height))
        overlay.set_alpha(180)
        overlay.fill((0, 50, 0))  # Dark green
        screen.blit(overlay, (0, 0))

        # Title
        title = self.title_font.render("LEVEL COMPLETE!", True, (255, 215, 0))
        title_rect = title.get_rect(center=(self.screen_width // 2, 200))
        screen.blit(title, title_rect)

        # Level info
        info_text = f"Level {level_number} Cleared!"
        info = self.info_font.render(info_text, True, (255, 255, 255))
        info_rect = info.get_rect(center=(self.screen_width // 2, 300))
        screen.blit(info, info_rect)

        # Continue prompt
        continue_text = "Press ENTER to continue"
        continue_surface = self.info_font.render(continue_text, True, (200, 200, 200))
        continue_rect = continue_surface.get_rect(center=(self.screen_width // 2, 400))
        screen.blit(continue_surface, continue_rect)

class GameCompleteScreen:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.title_font = pygame.font.Font(None, 72)
        self.text_font = pygame.font.Font(None, 36)

    def render(self, screen):
        """Render game complete screen"""
        # Background
        screen.fill((20, 50, 20))

        # Title
        title = self.title_font.render("CONGRATULATIONS!", True, (255, 215, 0))
        title_rect = title.get_rect(center=(self.screen_width // 2, 150))
        screen.blit(title, title_rect)

        # Message
        messages = [
            "You saved the coffee harvest!",
            "Sancho is a hero!",
            "",
            "Press M to return to menu"
        ]
        y_start = 280
        for i, text in enumerate(messages):
            message = self.text_font.render(text, True, (255, 255, 255))
            message_rect = message.get_rect(center=(self.screen_width // 2, y_start + i * 50))
            screen.blit(message, message_rect)

# In Game class:
def __init__(self):
    # ... existing code ...
    from src.ui.screens import LevelCompleteScreen, GameCompleteScreen
    self.level_complete_screen = LevelCompleteScreen(SCREEN_WIDTH, SCREEN_HEIGHT)
    self.game_complete_screen = GameCompleteScreen(SCREEN_WIDTH, SCREEN_HEIGHT)

def render_level_complete(self):
    """Render level complete screen"""
    # Render game world underneath
    self.current_level.render(self.screen, self.camera)
    self.player.render(self.screen, self.camera)

    # Overlay complete screen
    self.level_complete_screen.render(self.screen, self.current_level_number)

def render_game_complete(self):
    """Render game complete screen"""
    self.game_complete_screen.render(self.screen)

def update(self, dt):
    """Update based on current state"""
    if self.state == GameState.PLAYING:
        # ... existing update code ...

        # Check win condition
        if self.current_level.check_goal(self.player):
            self.change_state(GameState.LEVEL_COMPLETE)

    elif self.state == GameState.LEVEL_COMPLETE:
        # Wait for input (no auto-advance)
        pass

    # ... other states ...

def handle_events(self):
    for event in pygame.event.get():
        # ... existing code ...

        if event.type == pygame.KEYDOWN:
            # Level complete state
            if self.state == GameState.LEVEL_COMPLETE:
                if event.key == pygame.K_RETURN:
                    self.advance_to_next_level()

            # Game complete state
            if self.state == GameState.GAME_COMPLETE:
                if event.key == pygame.K_m or event.key == pygame.K_ESCAPE:
                    self.change_state(GameState.MENU)

def advance_to_next_level(self):
    """Advance to next level"""
    next_level = self.current_level_number + 1

    if next_level <= 5:
        # Load next level
        self.load_level(next_level)

        # Reset player position
        spawn = self.current_level.get_spawn_position()
        self.player.position.x = spawn[0]
        self.player.position.y = spawn[1]
        self.player.velocity = pygame.Vector2(0, 0)

        # Reset power-up state
        self.player.has_powerup = False
        self.player.powerup_timer = 0.0

        # Clear lasers
        self.lasers = []

        # Return to playing
        self.change_state(GameState.PLAYING)
    else:
        # Game complete!
        self.change_state(GameState.GAME_COMPLETE)

# Update GameState enum:
class GameState:
    MENU = "MENU"
    PLAYING = "PLAYING"
    PAUSED = "PAUSED"
    GAME_OVER = "GAME_OVER"
    LEVEL_COMPLETE = "LEVEL_COMPLETE"
    GAME_COMPLETE = "GAME_COMPLETE"

# Update render method:
def render(self):
    # ... existing states ...

    elif self.state == GameState.LEVEL_COMPLETE:
        self.render_level_complete()

    elif self.state == GameState.GAME_COMPLETE:
        self.render_game_complete()

    pygame.display.flip()
```

## Dependencies
- US029: Game state management must exist
- US017: Level loading must work
- US004: Game window must exist
