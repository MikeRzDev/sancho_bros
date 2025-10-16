# US030: Create Main Menu UI

**As a** developer
**I want** to create a main menu screen
**So that** players can start the game or quit

## Priority
High

## Story Points
3

## Acceptance Criteria

1. **Menu Class Created**
   - [x] `src/ui/menu.py` exists
   - [x] `MainMenu` class is defined

2. **Menu Display**
   - [x] Title displayed: "SANCHO BROS"
   - [x] Options displayed:
     - "Start Game" (ENTER to select)
     - "Quit" (Q to select)
   - [x] Instructions shown (basic controls)
   - [x] Clean, readable layout

3. **Menu Rendering**
   - [x] Background color/pattern
   - [x] Title in large font
   - [x] Menu options in readable font
   - [x] Centered on screen
   - [x] Professional appearance

4. **Menu Navigation**
   - [x] ENTER key starts game
   - [x] Q key quits game
   - [x] ESC key also quits
   - [x] Clear feedback on selection (optional hover effect)

5. **Start Game Transition**
   - [x] Pressing ENTER changes state to PLAYING
   - [x] Game initializes properly
   - [x] Level 1 loads
   - [x] Player spawns correctly

6. **Quit Functionality**
   - [x] Q key exits application
   - [x] Clean shutdown
   - [x] No errors on exit

7. **Visual Polish**
   - [x] Readable fonts (size 36-72 for title)
   - [x] Good contrast (text vs background)
   - [x] Aligned text
   - [x] Optional: Simple animations (title pulse, etc.)

8. **Controls Display**
   - [x] Shows basic controls:
     - "Arrow Keys / WASD: Move"
     - "SPACE: Jump"
     - "X / CTRL: Shoot (when powered)"
     - "ESC: Pause"

9. **Validation**
   - [x] Menu displays on game start
   - [x] ENTER starts game
   - [x] Q quits application
   - [x] Menu looks clean and professional

## Technical Notes

```python
# src/ui/menu.py
import pygame
from src.constants import *

class MainMenu:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height

        # Fonts
        self.title_font = pygame.font.Font(None, 72)
        self.option_font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)

    def render(self, screen):
        """Render main menu"""
        # Background
        screen.fill((50, 50, 100))  # Dark blue

        # Title
        title = self.title_font.render("SANCHO BROS", True, (255, 215, 0))
        title_rect = title.get_rect(center=(self.screen_width // 2, 150))
        screen.blit(title, title_rect)

        # Start option
        start_text = self.option_font.render("Press ENTER to Start", True, (255, 255, 255))
        start_rect = start_text.get_rect(center=(self.screen_width // 2, 300))
        screen.blit(start_text, start_rect)

        # Quit option
        quit_text = self.option_font.render("Press Q to Quit", True, (200, 200, 200))
        quit_rect = quit_text.get_rect(center=(self.screen_width // 2, 350))
        screen.blit(quit_text, quit_rect)

        # Controls
        y_pos = 450
        controls = [
            "CONTROLS:",
            "Arrow Keys / WASD: Move",
            "SPACE: Jump",
            "X / CTRL: Shoot (when powered)",
            "ESC: Pause"
        ]
        for i, text in enumerate(controls):
            control_text = self.small_font.render(text, True, (150, 150, 150))
            control_rect = control_text.get_rect(center=(self.screen_width // 2, y_pos + i * 25))
            screen.blit(control_text, control_rect)

# In Game class:
def __init__(self):
    # ... existing code ...
    from src.ui.menu import MainMenu
    self.main_menu = MainMenu(SCREEN_WIDTH, SCREEN_HEIGHT)

def render_main_menu(self):
    """Render main menu"""
    self.main_menu.render(self.screen)

def handle_events(self):
    for event in pygame.event.get():
        # ... existing code ...

        if event.type == pygame.KEYDOWN:
            if self.state == GameState.MENU:
                if event.key == pygame.K_RETURN:
                    self.change_state(GameState.PLAYING)
                if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    self.running = False
```

**Optional - Animated Title:**
```python
class MainMenu:
    def __init__(self, screen_width, screen_height):
        # ... existing code ...
        self.animation_timer = 0.0

    def update(self, dt):
        """Update menu animations"""
        self.animation_timer += dt

    def render(self, screen):
        # ... existing background ...

        # Animated title (pulse effect)
        scale = 1.0 + 0.05 * math.sin(self.animation_timer * 2)
        font_size = int(72 * scale)
        title_font = pygame.font.Font(None, font_size)
        title = title_font.render("SANCHO BROS", True, (255, 215, 0))
        title_rect = title.get_rect(center=(self.screen_width // 2, 150))
        screen.blit(title, title_rect)

        # ... rest of rendering ...
```

## Dependencies
- US029: Game state management must exist
- US004: Game window must exist
