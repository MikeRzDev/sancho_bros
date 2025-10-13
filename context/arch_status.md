# ARCHITECTURE STATUS

**Last Updated:** 2025-10-13
**Current Development Phase:** Phase 2 - Level Generator (IN PROGRESS)

---

## Current Project Structure

```
sancho_bros/
   .gitignore                     # Python/macOS/IDE gitignore configuration
   README.md                      # Project overview and setup instructions
   requirements.txt               # Python dependencies (pygame>=2.0.0)
   CLAUDE.md                      # Project documentation and guidelines
   venv/                          # Python virtual environment (excluded from git)
   src/                           # Source code directory
      __init__.py
      main.py                    # Game entry point
      game.py                    # Main Game class with game loop
      constants.py               # Game configuration constants
      entities/                  # Player, enemies, power-ups, projectiles
         __init__.py
      level/                     # Level loading and management
         __init__.py
      physics/                   # Collision detection and gravity
         __init__.py
      ui/                        # Menus and HUD
         __init__.py
      utils/                     # Utility functions
          __init__.py
   tools/                         # Development tools
      level_generator.py         # Level generator tool
   levels/                        # JSON level files
      level_1.json               # Level 1 data (2000px, tutorial)
      level_2.json               # Level 2 data (2500px)
      level_3.json               # Level 3 data (3000px)
      level_4.json               # Level 4 data (3500px)
      level_5.json               # Level 5 data (4000px, maximum challenge)
   assets/                        # Game assets
      sprites/                   # Sprite images
         sancho/               # Player sprites
         polocho/              # Enemy sprites
         tiles/                # Platform/tile sprites
         items/                # Power-up sprites
      sounds/                    # Sound effects
      music/                     # Background music
   context/                       # Implementation documentation
       IMPLEMENTATION_PLAN.md    # User story tracking
       arch_status.md            # This file (technical state)
       game_implementation.md    # Detailed implementation guide
       problem_description.md    # Original requirements
       task_execution.md         # Execution workflow
       resumes/                  # User story completion summaries
       user_stories/             # Individual user story files
           phase_*_*/            # User stories organized by phase
```

---

## Development Environment

### Python Environment
- **Python Version:** 3.13.3
- **Virtual Environment:** `venv/` directory (excluded from version control)
- **Dependency Management:** `requirements.txt` with flexible versioning (`pygame>=2.0.0`)

### Installed Dependencies
- **Pygame:** 2.6.1 (SDL 2.28.4)
  - Verified compatible with Python 3.13.3
  - All core modules tested and functional (display, events, drawing, collision, clock, font)
  - Pre-built wheels available for macOS ARM64

---

## Architecture Overview

### Core Game Loop
The game uses a centralized Game class (`src/game.py`) that manages:
- **Initialization**: Pygame setup, window creation (800x600), display settings
- **Main Loop**: 60 FPS game loop using `pygame.time.Clock()`
- **Event Handling**: Input processing (ESC key, window close)
- **Update Cycle**: Frame-independent updates using delta time
- **Render Cycle**: Screen clearing and entity rendering

### Modular Package Structure
The codebase follows a clean separation of concerns:

- **src/main.py**: Entry point that instantiates and runs the Game
- **src/game.py**: Main Game class containing the game loop and state management
- **src/constants.py**: Centralized game configuration
- **src/entities/**: Game objects (Player, Enemy, PowerUp, Projectile classes)
- **src/level/**: Level loading system and JSON parsing
- **src/physics/**: Collision detection and gravity systems
- **src/ui/**: User interface components (menus, HUD)
- **src/utils/**: Shared utility functions

### Asset Organization
Assets are organized by type for easy management:
- **sprites/**: Visual assets with subdirectories per entity type
- **sounds/**: Sound effect files
- **music/**: Background music files

### Development Tools
- **tools/**: Contains level generator and other development utilities

---

## Technical Decisions

### Dependency Management
- Using Python virtual environments for isolation (PEP 668 compliance)
- Flexible pygame versioning (`>=2.0.0`) supports Python 3.8 through 3.13+
- README documents full setup process for developer onboarding

### Code Organization
- All Python packages have `__init__.py` for proper module imports
- Modular architecture enables independent development of game systems
- Clear separation between game logic, rendering, and data management

### Game Constants Configuration
The `src/constants.py` file centralizes all game configuration values:
- **Screen constants**: 800x600 resolution at 60 FPS
- **Physics constants**: Gravity (0.8), jump strength (-15), player speed (5), max fall speed (15)
- **Game rules**: 3 starting lives, 10-second laser duration, 0.5-second cooldown
- **Entity dimensions**: Player (40x60), Enemy (40x50), Platform (100x20 default), Power-up (30x30), Laser (10x4)
- **Color constants**: RGB tuples for placeholder graphics (player blue, enemy red, platforms brown/gray, power-up gold, laser cyan)
- **AI constants**: Enemy patrol speed (2 pixels/frame)

All constants follow UPPER_SNAKE_CASE naming convention and can be imported via `from src.constants import *`.

---

## Current State

### What Exists
- ✓ Complete directory structure
- ✓ Python virtual environment configured
- ✓ Pygame 2.6.1 installed and verified
- ✓ All package directories initialized
- ✓ Development documentation in place
- ✓ Game constants configuration (`src/constants.py`)
- ✓ Main game loop and window initialization (`src/main.py`, `src/game.py`)
- ✓ Basic game state management (running/stopped states)
- ✓ 60 FPS game loop with delta time calculation
- ✓ Event handling system (ESC key, window close)
- ✓ Level generator tool (`tools/level_generator.py`)
- ✓ 5 JSON level files with progressive difficulty (Phase 2 - US005)
- ✓ Platform generation logic with ground and floating platforms (Phase 2 - US006)
- ✓ Basic pit placement logic (Phase 2 - US006)

### What's Pending
- Enemy placement logic (Phase 2 - US007)
- Power-up placement enhancement (Phase 2 - US008)
- Level generation completion (Phase 2 - US009)
- Game entities (Player, Enemy, PowerUp, Projectile)
- Physics system (collision detection, gravity)
- Level loading system
- UI components (menus, HUD)

---

## System Requirements

### Minimum Requirements
- Python 3.8 or higher
- Pygame 2.0 or higher

### Current Development Environment
- Python 3.13.3
- Pygame 2.6.1 (SDL 2.28.4)
- macOS (Darwin 24.6.0)

---

## Implemented Systems

### Game Loop Architecture (US004)
The core game loop is implemented in `src/game.py` with the following structure:

**Game Class Methods:**
- `__init__()`: Initializes Pygame, creates 800x600 window with title "Sancho Bros", sets up clock and running state
- `run()`: Main game loop that maintains 60 FPS, calculates delta time, and calls handle_events/update/render
- `handle_events()`: Processes pygame events (QUIT event, ESC key for exit)
- `update(dt)`: Placeholder for game state updates (receives delta time in seconds)
- `render()`: Clears screen with background color, updates display

**Entry Point (`src/main.py`):**
- Simple entry point that imports Game class and calls `game.run()`
- Follows standard Python `if __name__ == "__main__"` pattern

**State Management:**
- Boolean `self.running` flag controls game loop execution
- Clean shutdown with `pygame.quit()` when loop exits

### Level Generator Tool (US005, US006)
The level generator tool creates all 5 JSON level files with progressive difficulty. Located at `tools/level_generator.py`.

**LevelGenerator Class:**
- `__init__()`: Initializes difficulty configurations for all 5 levels
- `generate_level(level_num)`: Creates complete level data structure with all required fields
- `place_platforms(level_data, difficulty)`: Platform generation with ground and floating platforms (US006 ✓)
- `place_enemies(level_data, difficulty)`: Enemy placement (to be implemented in US007)
- `place_powerups(level_data, difficulty)`: Power-up placement (to be implemented in US008)
- `create_pits(level_data, difficulty)`: Pit hazard generation (basic implementation in US006 ✓)
- `save_to_file(level_data, filename)`: Writes JSON with proper formatting
- `generate_all_levels()`: Generates all 5 levels at once

**Difficulty Configuration:**
- Level 1: 2000px wide, 2-3 enemies, 1 power-up, 1-2 pits (tutorial)
- Level 2: 2500px wide, 4-5 enemies, 1 power-up, 2-3 pits
- Level 3: 3000px wide, 6-7 enemies, 2 power-ups, 3-4 pits
- Level 4: 3500px wide, 8-9 enemies, 2 power-ups, 4-5 pits
- Level 5: 4000px wide, 10-12 enemies, 2-3 power-ups, 5-6 pits (maximum challenge)

**Platform Generation (US006):**
The `place_platforms()` method creates:
- **Ground platforms**: Solid platforms at y=550 with 50px height, split by pit gaps
- **Floating platforms**: Platforms at varying heights (200-500) with 20px height
  - Level 1: 5 floating platforms (120-150px wide) at heights 350-450
  - Level 2: 8 floating platforms (100-140px wide) at heights 300-480
  - Level 3: 12 floating platforms (80-130px wide) at heights 300-480
  - Level 4: 15 floating platforms (70-120px wide) at heights 200-500
  - Level 5: 18 floating platforms (60-110px wide) at heights 200-500
- **Progression platforms**: Special platforms near spawn (x=250) and goal to ensure completability
- **Distribution**: Platforms evenly distributed across level using segmentation
- **Validation**: No overlaps, reasonable spacing, completable paths

**Pit Generation (US006):**
The `create_pits()` method generates pit hazards:
- Pits placed in safe zones (500px from spawn, 500px from goal)
- Evenly distributed across level using segmentation
- Pit widths scale with difficulty: 80-150px (larger for higher levels)
- Ground platforms automatically split at pit locations

**JSON Output Structure:**
Each level file contains:
- `level_number`: Level identifier (1-5)
- `width`, `height`: Level dimensions (variable width, 600px height)
- `background_color`: RGB array [135, 206, 235] (sky blue)
- `player_spawn`: Starting position {x: 100, y: 400}
- `platforms`: Array of platform objects with type, x, y, width, height (US006 ✓)
- `enemies`: Array of enemy spawn points (empty until US007)
- `powerups`: Array of power-up locations (empty until US008)
- `pits`: Array of pit hazards with x, width (US006 ✓)
- `goal`: Level exit position (level_width - 200, 500)

**Usage:**
```bash
python3 tools/level_generator.py
```

---

## Implementation Notes

### Level System
- Levels will be stored as JSON files in `levels/` directory
- Level generator tool (`tools/level_generator.py`) will be created in Phase 2
- 5 levels planned with progressive difficulty scaling

### Assets
- Asset directories currently empty (placeholders)
- Initial implementation will use colored rectangles as placeholders
- Sprite/audio integration planned for later phases

### Module System
- All Python packages initialized with `__init__.py`
- Ready for entity classes and game systems to be added
