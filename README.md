# Sancho Bros

A 2D platformer game featuring Sancho, a Colombian coffee farmer on an adventure to collect La Arepa Dorada power-ups while defeating Polocho enemies.

## Overview

Sancho Bros is a Python and Pygame-based platformer with 5 levels of increasing difficulty. Navigate through platforms, avoid pits, stomp on enemies, and use power-ups to shoot lasers.

## Key Features

- 5 externally-loaded JSON levels
- Platform physics with gravity and jumping
- Enemy AI with patrol behavior
- Stomp-on-head and laser combat mechanics
- Power-up system that grants temporary shooting ability

## Setup

### 1. Create Virtual Environment
```bash
python3 -m venv venv
```

### 2. Activate Virtual Environment
```bash
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Generate Levels (Required before first run)
```bash
python tools/level_generator.py
```

### 5. Run the Game
```bash
python src/main.py
```

## Project Structure

```
sancho_bros/
├── src/              # Source code
│   ├── entities/     # Player, enemies, power-ups, projectiles
│   ├── level/        # Level loading and management
│   ├── physics/      # Collision detection and gravity
│   ├── ui/           # Menus and HUD
│   └── utils/        # Utility functions
├── tools/            # Level generator and other tools
├── levels/           # Generated JSON level files
├── assets/           # Game assets (sprites, sounds, music)
└── context/          # Implementation documentation
```

## Game Controls

### Movement
- **Arrow Keys / WASD**: Move left/right
- **Space**: Jump

### Combat
- **X / Left CTRL**: Shoot laser (when powered up with La Arepa Dorada)

### Menus & Pause
- **ENTER**: Start game / Select menu option / Advance to next level
- **ESC / P**: Pause/Unpause game
- **M**: Return to main menu (from pause or game over)
- **R**: Restart current level (from pause) or restart game (from game over)
- **Q**: Quit game (from main menu)

## Game Rules

- **Lives**: Start with 3 lives
- **Defeating Enemies**: Jump on Polocho enemies' heads to stomp them, or shoot them with lasers
- **Power-Ups**: Collect La Arepa Dorada for 10 seconds of laser shooting ability
- **Pits**: Avoid falling into pits - instant death!
- **Goal**: Reach the goal marker at the end of each level to advance
- **Invincibility**: After taking damage, you get 2 seconds of invincibility (player flashes)

## System Requirements

- **Python**: 3.8 or higher
- **Pygame**: 2.6.1
- **OS**: Windows, macOS, or Linux
- **Memory**: 512 MB RAM minimum
- **Display**: 800x600 minimum resolution

## Technical Stack

- Python 3.8+ (tested with Python 3.13.3)
- Pygame 2.6.1

## Development

For development documentation, see:
- `CLAUDE.md` - Development guidance and architecture
- `context/IMPLEMENTATION_PLAN.md` - User story implementation roadmap
- `docs/` - Additional documentation

### Debug Mode

To enable debug output, set `DEBUG = True` in `src/constants.py`

## Troubleshooting

**Game won't start**:
- Ensure you ran `python tools/level_generator.py` before first run
- Check that all 5 level files exist in `levels/` directory

**Import errors**:
- Make sure you're running from the project root directory
- Verify virtual environment is activated
- Reinstall dependencies: `pip install -r requirements.txt`

**Performance issues**:
- Game targets 60 FPS - check system meets minimum requirements
- Close other applications to free up resources

## Credits

Developed as a Pygame learning project.
Inspired by classic platformers like Super Mario Bros.

## License

MIT License
