# US004: Create Basic Game Window and Main Loop

**As a** developer
**I want** to create a basic Pygame window with a main game loop
**So that** I have a foundation to build the game upon

## Priority
High

## Story Points
3

## Acceptance Criteria

1. **Main Entry Point Created**
   - [ ] `src/main.py` exists
   - [ ] Running `python src/main.py` opens a game window
   - [ ] Window dimensions are SCREEN_WIDTH x SCREEN_HEIGHT (800x600)

2. **Game Class Structure**
   - [ ] `src/game.py` exists
   - [ ] `Game` class is defined with the following methods:
     - `__init__()`: Initialize pygame and create window
     - `run()`: Main game loop
     - `handle_events()`: Process input events
     - `update(dt)`: Update game state (placeholder)
     - `render()`: Draw to screen (placeholder)

3. **Game Loop Functionality**
   - [ ] Game loop runs at 60 FPS
   - [ ] Window displays with a solid background color
   - [ ] Window title is "Sancho Bros"
   - [ ] ESC key or window close button exits the game cleanly

4. **Basic State Management**
   - [ ] Game state variable initialized (e.g., `RUNNING`)
   - [ ] Game loop continues while in running state

5. **Validation**
   - [ ] Window opens without errors
   - [ ] FPS is maintained at ~60
   - [ ] No memory leaks when running for 30 seconds
   - [ ] Clean exit without errors

## Technical Notes

```python
# main.py structure:
from src.game import Game

def main():
    game = Game()
    game.run()

if __name__ == "__main__":
    main()

# game.py structure:
import pygame
from src.constants import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Sancho Bros")
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        while self.running:
            dt = self.clock.tick(FPS) / 1000.0
            self.handle_events()
            self.update(dt)
            self.render()
        pygame.quit()
```

- Use pygame.time.Clock() for FPS control
- Delta time (dt) should be passed to update for frame-independent movement

## Dependencies
- US002: Pygame must be installed
- US003: Constants must be defined
