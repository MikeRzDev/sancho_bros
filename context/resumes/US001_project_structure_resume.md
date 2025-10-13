# US001: Project Directory Structure - Resume

**User Story ID:** US001
**User Story Name:** Set Up Project Directory Structure
**Phase:** Phase 1 - Setup
**Completion Date:** 2025-10-13
**Story Points:** 2

---

## Changes Made

Successfully created the complete project directory structure for Sancho Bros, a 2D platformer game built with Python and Pygame. This establishes the foundational organization for all future development work, with proper separation of concerns across source code, assets, tools, levels, and documentation.

---

## Files Modified/Created

### Root Level Files

**`requirements.txt`** (Created)
- Python dependencies file
- Contains pygame==2.5.2 as the primary game engine dependency
- Used by pip to install all project requirements

**`README.md`** (Created)
- Project overview and description
- Installation and setup instructions
- Game controls reference
- Project structure documentation
- Technical stack information

**`.gitignore`** (Already Existed)
- Git ignore rules for Python projects
- Includes Python bytecode, virtual environments, IDE files, macOS system files
- Properly configured for Python/Pygame development

---

### Directory Structure Created

**`src/`** - Main source code directory
- Contains all Python game code
- Organized into modular subdirectories
- All subdirectories initialized as Python packages with `__init__.py`

**`src/entities/`**
- Will contain Player, Enemy (Polocho), PowerUp (La Arepa Dorada), and Projectile classes
- Entity-specific game logic and behaviors

**`src/level/`**
- Will contain Level class and LevelLoader
- JSON level file parser
- Level state management

**`src/physics/`**
- Will contain collision detection system
- Gravity and physics calculations
- AABB collision helpers

**`src/ui/`**
- Will contain Menu, HUD, and screen management classes
- Game state UI components (main menu, pause, game over)

**`src/utils/`**
- Will contain utility functions and helpers
- Shared code across modules

**`tools/`**
- Development and build tools directory
- Will contain level_generator.py in Phase 2

**`levels/`**
- Storage for JSON level files (level_1.json through level_5.json)
- Will be populated by level generator tool

**`assets/`** - Game assets organized by type

**`assets/sprites/`** - All sprite images
- `sancho/` - Player character sprites
- `polocho/` - Enemy character sprites
- `tiles/` - Platform and tile sprites
- `items/` - Power-up and collectible sprites

**`assets/sounds/`** - Sound effects

**`assets/music/`** - Background music files

---

## Rationale

### Why This Structure Matters

**Modular Architecture:**
The directory structure follows a modular entity-component architecture that separates concerns:
- **Entities** are self-contained game objects with their own update/render logic
- **Level** system manages game state and entity collections
- **Physics** is decoupled and reusable across different entity types
- **UI** components are independent of game logic

**Scalability:**
This structure allows the game to scale easily:
- New entity types can be added to `src/entities/` without affecting existing code
- Additional levels are just new JSON files in `levels/`
- Asset organization makes it easy to swap sprites/sounds without code changes

**Python Package Structure:**
Using `__init__.py` files in each source directory:
- Enables proper Python module imports (e.g., `from entities.player import Player`)
- Follows Python best practices
- Makes the codebase more maintainable

**External Level Data:**
Separating levels into JSON files (`levels/` directory):
- Allows level design without code changes
- Enables non-programmers to create/modify levels
- Makes it easy to add more levels in the future
- Supports a level generation tool (Phase 2)

**Asset Organization:**
Organizing assets by type and entity:
- Makes it easy to find and replace specific sprites
- Supports future sprite sheet implementations
- Allows different asset sets (themes) to be swapped easily

---

## Technical Decisions

1. **pygame 2.5.2**: Latest stable version with good performance and cross-platform support

2. **JSON for Levels**: Human-readable format that's easy to parse, edit, and version control

3. **Separation of Tools**: `tools/` directory keeps development utilities separate from game code

4. **Context Directory**: Maintains all implementation documentation and tracking in one place

---

## Current System State

**Python Packages Initialized:**
- src
- src.entities
- src.level
- src.physics
- src.ui
- src.utils

**Ready for Development:**
- All directories are accessible with proper permissions
- Python package structure is complete
- Git repository is properly configured with .gitignore
- Documentation is in place

**Pending Work:**
- Level JSON files need to be generated (Phase 2)
- Asset directories are empty placeholders
- No source code files yet (starting in US002+)

---

## Next Steps

**Immediate Next User Story:** US002 - Install Pygame and Dependencies

**Dependencies:** None - US002 can proceed independently

**Phase 1 Remaining Stories:**
1. US002: Install Pygame and Dependencies (verify installation works)
2. US003: Create Game Constants Configuration (define all game constants)
3. US004: Create Basic Game Window and Main Loop (minimal runnable game)

**Critical Path:** The level generator must be completed in Phase 2 before the game can fully run, as all 5 level JSON files are required by the level loading system.

---

## Integration Notes for Future LLM Context

When continuing this project:
1. All source code should go in `src/` subdirectories, never in the root
2. Follow the import pattern: `from entities.player import Player`
3. Asset paths should use the `assets/` directory structure
4. Level files must be in `levels/` and follow the JSON schema defined in CLAUDE.md
5. Use constants from `src/constants.py` (to be created in US003)
6. The game entry point will be `src/main.py` (to be created in US004)

**Architecture Pattern:** Entity-component design where each entity manages its own state, rendering, and collision logic. The Level class orchestrates all entities and checks win/lose conditions.
