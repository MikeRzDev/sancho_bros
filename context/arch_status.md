# ARCHITECTURE STATUS

**Last Updated:** 2025-10-13
**Current Development Phase:** Phase 1 - Setup

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
   levels/                        # JSON level files (to be generated)
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

### Modular Package Structure
The codebase follows a clean separation of concerns:

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

### What's Pending
- Main game loop and window initialization
- All game entities and systems (to be implemented in subsequent phases)

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
