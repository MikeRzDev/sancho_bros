# US004: Basic Game Window and Main Loop - Implementation Resume

**Completed:** 2025-10-13
**Story Points:** 3
**Phase:** Phase 1 - Setup

---

## Changes Made

Implemented the foundational game loop and window system for Sancho Bros. Created the main entry point and Game class that initializes Pygame, opens an 800x600 game window, and runs at 60 FPS. The system handles user input (ESC key and window close button) and provides placeholder methods for future game logic implementation.

---

## Files Created

### `src/main.py`
**Purpose:** Game entry point
**What it does:**
- Imports the Game class from `src.game`
- Defines a `main()` function that instantiates and runs the game
- Uses standard Python `if __name__ == "__main__"` pattern for direct execution
- Simple, clean entry point following best practices

### `src/game.py`
**Purpose:** Main Game class with core game loop
**What it does:**
- **`__init__()` method**: Initializes Pygame, creates 800x600 window with "Sancho Bros" title, sets up FPS clock, initializes running state
- **`run()` method**: Main game loop that runs at 60 FPS, calculates delta time for frame-independent movement, calls event handling/update/render in sequence, performs clean shutdown with `pygame.quit()`
- **`handle_events()` method**: Processes pygame events including window close (QUIT event) and ESC key press to exit game
- **`update(dt)` method**: Placeholder for future game state updates, receives delta time in seconds
- **`render()` method**: Clears screen with background color from constants, updates display with `pygame.display.flip()`

---

## Rationale

### Why This Matters
This user story establishes the **core foundation** of the entire game. Without a functioning game loop and window, no other game systems (player movement, enemies, levels, etc.) can be developed or tested. The Game class provides the backbone that will orchestrate all future game systems.

### Architecture Decisions

1. **Centralized Game Class**: All game state and loop logic lives in a single `Game` class, making it easy to extend with additional systems (level management, state machines, entity management) in future user stories.

2. **Delta Time for Frame Independence**: The loop calculates delta time (`dt`) in seconds and passes it to the update method. This ensures game logic can be frame-independent, meaning movement and physics will work consistently regardless of actual FPS variations.

3. **Separation of Concerns**: The game loop is divided into three clear phases:
   - **handle_events()**: Input processing
   - **update(dt)**: Game logic
   - **render()**: Display output

   This separation makes the codebase easier to maintain and extend.

4. **Clean Shutdown**: The game properly calls `pygame.quit()` when the loop exits, preventing resource leaks and ensuring a clean exit.

### How It Fits Into Overall Architecture
- **src/main.py** → **src/game.py** → Future systems (entities, physics, level loading)
- The Game class will eventually manage:
  - Game state machines (MENU, PLAYING, PAUSED, GAME_OVER)
  - Level instances and transitions
  - Entity collections (player, enemies, projectiles)
  - Camera/viewport system
  - UI rendering (HUD, menus)

---

## Technical Implementation Details

### Game Loop Pattern
The implementation uses the classic game loop pattern:
```
Initialize → Loop (Events → Update → Render) → Cleanup
```

### FPS Control
- Uses `pygame.time.Clock()` to maintain consistent 60 FPS
- Delta time calculated as `self.clock.tick(FPS) / 1000.0` (converts milliseconds to seconds)
- This ensures smooth, predictable gameplay

### Event Handling
Currently handles two events:
- `pygame.QUIT`: Triggered when user clicks window close button
- `pygame.K_ESCAPE`: Triggered when user presses ESC key

Both events set `self.running = False`, which exits the game loop cleanly.

---

## Testing & Validation

### Verification Performed
- ✓ Code compiles without syntax errors
- ✓ All imports resolve correctly (pygame, constants)
- ✓ Game class can be instantiated successfully
- ✓ Structure follows pygame best practices

### How to Test
To verify the implementation works:
```bash
# Activate virtual environment and run
venv/bin/python3 src/main.py
```

**Expected behavior:**
- Window opens with title "Sancho Bros" at 800x600 resolution
- Window displays sky blue background (COLOR_BACKGROUND from constants)
- Window runs at 60 FPS
- Pressing ESC or clicking window close button exits cleanly
- No errors in console

---

## Dependencies

### Completed User Stories Required
- **US001**: Project directory structure must exist
- **US002**: Pygame must be installed in virtual environment
- **US003**: Constants file must define SCREEN_WIDTH, SCREEN_HEIGHT, FPS, COLOR_BACKGROUND

### External Dependencies
- Pygame 2.6.1 (verified installed and working)
- Python 3.13.3

---

## Next Steps

### Immediate Next User Story
**US005: Create Level Generator Tool Structure**
- Located at: `context/user_stories/phase_2_level_generator/US005_level_generator_structure.md`
- Phase: Phase 2 - Level Generator
- Story Points: 3
- What it involves: Creating the `tools/level_generator.py` script structure that will generate the 5 JSON level files

### Why US005 Comes Next
According to CLAUDE.md, the level generator is on the **critical path**. The game cannot run without level JSON files, so Phase 2 must be completed before implementing player mechanics, enemies, or any gameplay features.

### Future Enhancements to Game Loop
The Game class will be extended in future user stories to include:
- Game state management (US029: MENU, PLAYING, PAUSED, GAME_OVER states)
- Level instance management (US016: current level, level transitions)
- Entity management (US010, US019, US024: player, enemies, power-ups)
- Camera system integration (US014: viewport following player)
- UI rendering (US030-US033: menus, HUD, screens)

---

## Phase 1 Status

With US004 complete, **Phase 1 (Setup) is now 100% complete** (4/4 user stories):
- ✅ US001: Project Structure
- ✅ US002: Install Pygame
- ✅ US003: Game Constants
- ✅ US004: Basic Game Window

**Next Phase:** Phase 2 - Level Generator (5 user stories, 19 story points)
