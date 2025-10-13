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

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Generate Levels (Required before first run)
```bash
python tools/level_generator.py
```

### Run the Game
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

- Arrow Keys / WASD: Move left/right
- Space: Jump
- X / Ctrl: Shoot laser (when power-up is active)

## Technical Stack

- Python 3.x
- Pygame 2.5.2

## License

MIT License
