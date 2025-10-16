# US029: Implement Complete Game State Management

**As a** developer
**I want** to implement complete game state management
**So that** the game can properly handle menu, playing, paused, game over, and completion states

## Priority
High

## Story Points
5

## Acceptance Criteria

1. **Game States Defined**
   - [x] States enumerated or constants created:
     - MENU
     - PLAYING
     - PAUSED
     - GAME_OVER
     - LEVEL_COMPLETE
   - [x] Current state tracked in game class
   - [x] State transitions handled properly

2. **MENU State**
   - [x] Game starts in MENU state
   - [x] Main menu renders
   - [x] Game entities don't update in MENU
   - [x] Can transition to PLAYING

3. **PLAYING State**
   - [x] Normal gameplay active
   - [x] All entities update
   - [x] All rendering occurs
   - [x] Can transition to PAUSED, GAME_OVER, or LEVEL_COMPLETE

4. **PAUSED State**
   - [x] Game freezes when paused
   - [x] Entities don't update
   - [x] Pause menu renders over game
   - [x] Can unpause back to PLAYING

5. **GAME_OVER State**
   - [x] Triggered when lives reach 0
   - [x] Game stops updating
   - [x] Game over screen displays
   - [x] Can restart or return to menu

6. **LEVEL_COMPLETE State**
   - [x] Triggered when player reaches goal
   - [x] Brief pause or animation
   - [x] Can continue to next level
   - [x] Transitions back to PLAYING with new level

7. **State Transition Methods**
   - [x] `change_state(new_state)` method
   - [x] Validates state transitions
   - [x] Handles cleanup when changing states
   - [x] Logs state changes (for debugging)

8. **Pause Functionality**
   - [x] ESC or P key pauses game
   - [x] Cannot pause in MENU or GAME_OVER
   - [x] Pause toggles between PLAYING and PAUSED
   - [x] Game state preserved when paused

9. **Update Logic per State**
   - [x] Update method checks current state
   - [x] Only updates relevant entities for state
   - [x] Prevents updates in frozen states

10. **Render Logic per State**
    - [x] Renders appropriate screens per state
    - [x] MENU: Main menu
    - [x] PLAYING: Game world
    - [x] PAUSED: Game world + pause overlay
    - [x] GAME_OVER: Game over screen
    - [x] LEVEL_COMPLETE: Completion message

11. **Validation**
    - [x] Game starts in MENU
    - [x] Can start playing from menu
    - [x] Can pause and unpause
    - [x] Game over works correctly
    - [x] Level completion works correctly
    - [x] No crashes during state transitions

## Technical Notes

```python
# Add to constants.py or game.py:
class GameState:
    MENU = "MENU"
    PLAYING = "PLAYING"
    PAUSED = "PAUSED"
    GAME_OVER = "GAME_OVER"
    LEVEL_COMPLETE = "LEVEL_COMPLETE"

# In Game class:
def __init__(self):
    # ... existing code ...
    self.state = GameState.MENU

def change_state(self, new_state):
    """Change game state"""
    print(f"State change: {self.state} -> {new_state}")
    self.state = new_state

    # Handle state-specific logic
    if new_state == GameState.LEVEL_COMPLETE:
        # Start timer for level transition (optional)
        pass

def handle_events(self):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            self.running = False

        if event.type == pygame.KEYDOWN:
            # Pause toggle
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_p:
                if self.state == GameState.PLAYING:
                    self.change_state(GameState.PAUSED)
                elif self.state == GameState.PAUSED:
                    self.change_state(GameState.PLAYING)

            # State-specific input
            if self.state == GameState.MENU:
                if event.key == pygame.K_RETURN:  # Start game
                    self.change_state(GameState.PLAYING)

            elif self.state == GameState.PLAYING:
                if event.key == pygame.K_SPACE:
                    self.player.jump()
                # ... other game inputs ...

            elif self.state == GameState.GAME_OVER:
                if event.key == pygame.K_r:  # Restart
                    self.restart_game()
                if event.key == pygame.K_m:  # Menu
                    self.change_state(GameState.MENU)

def update(self, dt):
    """Update based on current state"""
    if self.state == GameState.PLAYING:
        # Normal gameplay update
        self.current_level.update(dt, self.player)
        self.player.update(dt, self.current_level.get_platforms())
        self.camera.update(self.player.position, self.current_level.width)

        # Update lasers
        for laser in self.lasers[:]:
            laser.update(dt, self.current_level.get_platforms(),
                        self.current_level.enemies)
            if not laser.is_active:
                self.lasers.remove(laser)

        # Check win/lose conditions
        if self.current_level.check_goal(self.player):
            self.change_state(GameState.LEVEL_COMPLETE)

        if self.player.lives <= 0:
            self.change_state(GameState.GAME_OVER)

    elif self.state == GameState.LEVEL_COMPLETE:
        # Handle level transition
        self.load_next_level()
        self.change_state(GameState.PLAYING)

    elif self.state == GameState.PAUSED:
        # Don't update game entities
        pass

    elif self.state == GameState.MENU:
        # Update menu animations (if any)
        pass

def render(self):
    """Render based on current state"""
    if self.state == GameState.PLAYING or self.state == GameState.PAUSED:
        # Render game world
        self.current_level.render(self.screen, self.camera)
        self.player.render(self.screen, self.camera)
        for laser in self.lasers:
            laser.render(self.screen, self.camera)

    if self.state == GameState.PAUSED:
        # Render pause overlay
        self.render_pause_overlay()

    elif self.state == GameState.MENU:
        # Render main menu
        self.render_main_menu()

    elif self.state == GameState.GAME_OVER:
        # Render game over screen
        self.render_game_over()

    elif self.state == GameState.LEVEL_COMPLETE:
        # Render level complete message
        self.render_level_complete()

    pygame.display.flip()

def restart_game(self):
    """Restart game from Level 1"""
    self.load_level(1)
    spawn = self.current_level.get_spawn_position()
    self.player = Player(spawn[0], spawn[1])
    self.lasers = []
    self.change_state(GameState.PLAYING)
```

## Dependencies
- US004: Game window and loop must exist
- US017: Level loading must be integrated
