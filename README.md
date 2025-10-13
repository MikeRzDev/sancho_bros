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

- Arrow Keys / WASD: Move left/right
- Space: Jump
- X / Ctrl: Shoot laser (when power-up is active)

## Technical Stack

- Python 3.8+ (tested with Python 3.13.3)
- Pygame 2.6.1

## License

MIT License
