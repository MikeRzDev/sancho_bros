# SANCHO BROS - GAME IMPLEMENTATION SPECIFICATION

## 1. PROJECT OVERVIEW

**Sancho Bros** is a 2D platformer game inspired by classic platformers, featuring Colombian cultural elements. The player controls Sancho, a coffee farmer, navigating through 5 levels of increasing difficulty while defeating enemies and avoiding hazards.

## 2. TECHNOLOGY STACK

- **Language**: Python 3.8+
- **Game Framework**: Pygame 2.x
- **Level Format**: JSON
- **Asset Formats**: PNG (sprites), WAV/OGG (audio)

## 3. PROJECT STRUCTURE

```
sancho_bros/
├── src/
│   ├── main.py                 # Entry point
│   ├── game.py                 # Main game loop and state management
│   ├── constants.py            # Game constants and configuration
│   ├── entities/
│   │   ├── player.py           # Sancho player class
│   │   ├── enemy.py            # Polocho enemy class
│   │   ├── powerup.py          # La Arepa Dorada power-up
│   │   └── projectile.py       # Laser beam projectile
│   ├── level/
│   │   ├── level_loader.py     # Level file parser
│   │   ├── level.py            # Level class and management
│   │   └── tile.py             # Platform and block classes
│   ├── physics/
│   │   ├── collision.py        # Collision detection system
│   │   └── gravity.py          # Gravity and physics engine
│   ├── camera.py               # Camera/viewport system
│   ├── ui/
│   │   ├── menu.py             # Main menu and pause menu
│   │   ├── hud.py              # Heads-up display
│   │   └── screens.py          # Game over, level complete screens
│   └── utils/
│       ├── sprite_loader.py    # Asset loading utilities
│       └── animation.py        # Animation system
├── tools/
│   └── level_generator.py      # Level generation tool
├── levels/
│   ├── level_1.json
│   ├── level_2.json
│   ├── level_3.json
│   ├── level_4.json
│   └── level_5.json
├── assets/
│   ├── sprites/
│   │   ├── sancho/             # Player sprites and animations
│   │   ├── polocho/            # Enemy sprites
│   │   ├── tiles/              # Platform and block tiles
│   │   └── items/              # Power-up sprites
│   ├── sounds/
│   │   └── ...                 # Sound effects
│   └── music/
│       └── ...                 # Background music
├── requirements.txt
├── README.md
├── CLAUDE.md
└── game_implementation.md      # This file
```

## 4. CORE GAME ARCHITECTURE

### 4.1 Game Loop (game.py)

```python
class Game:
    States: MENU, PLAYING, PAUSED, GAME_OVER, LEVEL_COMPLETE

    Methods:
    - __init__(): Initialize pygame, load resources
    - run(): Main game loop (60 FPS)
    - handle_events(): Process input
    - update(dt): Update game state
    - render(): Draw everything
    - change_state(new_state): State transitions
```

### 4.2 Constants (constants.py)

```python
# Screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Physics
GRAVITY = 0.8
MAX_FALL_SPEED = 15
JUMP_STRENGTH = -15
PLAYER_SPEED = 5

# Game Rules
PLAYER_LIVES = 3
LASER_DURATION = 10  # seconds
LASER_COOLDOWN = 0.5  # seconds between shots
```

## 5. LEVEL FILE FORMAT

### 5.1 JSON Structure

```json
{
  "level_number": 1,
  "width": 3200,
  "height": 600,
  "background_color": [135, 206, 235],
  "player_spawn": {
    "x": 100,
    "y": 400
  },
  "platforms": [
    {
      "type": "solid",
      "x": 0,
      "y": 550,
      "width": 800,
      "height": 50
    },
    {
      "type": "floating",
      "x": 300,
      "y": 400,
      "width": 100,
      "height": 20
    }
  ],
  "enemies": [
    {
      "type": "polocho",
      "x": 500,
      "y": 510,
      "patrol_left": 400,
      "patrol_right": 600
    }
  ],
  "powerups": [
    {
      "type": "arepa_dorada",
      "x": 1000,
      "y": 300
    }
  ],
  "pits": [
    {
      "x": 800,
      "width": 100
    }
  ],
  "goal": {
    "x": 3000,
    "y": 500
  }
}
```

### 5.2 Level Elements

- **platforms**: Solid ground or floating platforms
  - `solid`: Ground blocks that can be stood on and jumped through from below
  - `floating`: Platforms in the air
- **enemies**: Polocho spawn points with patrol ranges
- **powerups**: Collectible items (La Arepa Dorada)
- **pits**: Fall zones (death if player falls in)
- **goal**: Level exit point

## 6. LEVEL GENERATOR SPECIFICATION

### 6.1 Purpose

Generate 5 JSON level files with progressive difficulty:
- Level 1: Tutorial-style, few enemies, simple jumps
- Level 2: More enemies, wider gaps
- Level 3: Multiple floating platforms, more pits
- Level 4: Longer level, complex enemy patterns
- Level 5: Maximum challenge, tight jumps, many enemies

### 6.2 Generation Rules

**Level 1:**
- Length: 2000 pixels
- 2-3 Polochos
- 1 Arepa Dorada power-up
- Simple platform layout
- 1-2 small pits

**Level 2:**
- Length: 2500 pixels
- 4-5 Polochos
- 1 Arepa Dorada
- More floating platforms
- 2-3 pits

**Level 3:**
- Length: 3000 pixels
- 6-7 Polochos
- 2 Arepa Doradas
- Complex platform arrangements
- 3-4 pits

**Level 4:**
- Length: 3500 pixels
- 8-9 Polochos
- 2 Arepa Doradas
- Long jumps required
- 4-5 pits

**Level 5:**
- Length: 4000 pixels
- 10-12 Polochos
- 2-3 Arepa Doradas
- Maximum difficulty platforming
- 5-6 pits

### 6.3 Generator Implementation (tools/level_generator.py)

```python
class LevelGenerator:
    Methods:
    - generate_level(level_num): Create level data
    - place_platforms(difficulty): Generate platform layout
    - place_enemies(difficulty): Spawn enemy positions
    - place_powerups(level_length): Position power-ups
    - create_pits(difficulty): Generate pit hazards
    - save_to_file(level_data, filename): Write JSON file
    - generate_all_levels(): Create all 5 levels
```

## 7. ENTITY SPECIFICATIONS

### 7.1 Player (Sancho)

**Class: Player**

**Attributes:**
- `position`: (x, y) coordinates
- `velocity`: (vx, vy) movement vector
- `lives`: Remaining lives (starts at 3)
- `has_powerup`: Boolean for Arepa Dorada state
- `powerup_timer`: Countdown for laser ability
- `facing_direction`: LEFT or RIGHT
- `is_jumping`: Boolean
- `is_grounded`: Boolean
- `animation_state`: IDLE, WALK, JUMP, SHOOT

**Methods:**
- `update(dt)`: Update position, apply gravity, check collisions
- `handle_input(keys)`: Process keyboard input
- `jump()`: Initiate jump if grounded
- `shoot_laser()`: Fire projectile if has_powerup
- `take_damage()`: Lose life, respawn or game over
- `collect_powerup()`: Activate Arepa Dorada effect
- `render(screen, camera)`: Draw sprite

**Controls:**
- Arrow Keys / WASD: Movement
- Space: Jump
- X / Left Ctrl: Shoot laser (when powered up)

**Physics:**
- Speed: 5 pixels/frame
- Jump strength: -15 pixels/frame
- Affected by gravity: 0.8 pixels/frame²

### 7.2 Enemy (Polocho)

**Class: Polocho**

**Attributes:**
- `position`: (x, y) coordinates
- `velocity`: (vx, vy)
- `patrol_left`: Left boundary
- `patrol_right`: Right boundary
- `facing_direction`: LEFT or RIGHT
- `is_alive`: Boolean

**Behavior:**
- Walk back and forth between patrol boundaries
- Turn around at edges or walls
- Defeated by: stomp (player jumps on head) or laser

**Methods:**
- `update(dt, platforms)`: Move and check boundaries
- `check_stomp(player)`: Detect if player landed on top
- `die()`: Death animation and removal
- `render(screen, camera)`: Draw sprite

### 7.3 Power-Up (La Arepa Dorada)

**Class: PowerUp**

**Attributes:**
- `position`: (x, y)
- `collected`: Boolean
- `animation_frame`: Float sprite animation

**Effects:**
- Grants laser shooting ability for 10 seconds
- Player can shoot projectiles

**Methods:**
- `update(dt)`: Animate sprite
- `check_collection(player)`: Detect player collision
- `render(screen, camera)`: Draw sprite

### 7.4 Projectile (Laser Beam)

**Class: Laser**

**Attributes:**
- `position`: (x, y)
- `velocity`: (vx, 0) - horizontal only
- `direction`: LEFT or RIGHT
- `lifetime`: Timer before auto-destruction

**Behavior:**
- Travel horizontally at high speed
- Destroy on contact with enemy or wall
- Auto-destroy after 2 seconds

**Methods:**
- `update(dt)`: Move and check lifetime
- `check_collision(enemies, platforms)`: Detect hits
- `render(screen, camera)`: Draw sprite

## 8. LEVEL SYSTEM

### 8.1 Level Loader (level/level_loader.py)

**Class: LevelLoader**

**Methods:**
- `load_level(filename)`: Parse JSON file
- `validate_level(data)`: Check format correctness
- `create_entities(level_data)`: Instantiate objects

### 8.2 Level Class (level/level.py)

**Class: Level**

**Attributes:**
- `level_number`: Current level
- `width`, `height`: Level dimensions
- `platforms`: List of platform objects
- `enemies`: List of enemy objects
- `powerups`: List of power-up objects
- `pits`: List of pit zones
- `player_spawn`: Starting position
- `goal`: Exit position
- `background_color`: RGB tuple

**Methods:**
- `update(dt, player)`: Update all entities
- `check_goal(player)`: Detect level completion
- `check_pits(player)`: Detect fall deaths
- `render(screen, camera)`: Draw level
- `reset()`: Restart level

## 9. PHYSICS SYSTEM

### 9.1 Collision Detection (physics/collision.py)

**Functions:**
- `check_aabb_collision(rect1, rect2)`: Axis-aligned bounding box
- `resolve_platform_collision(entity, platforms)`: Stop entities at platform surfaces
- `check_stomp(player, enemy)`: Verify jump-on-head attack
- `check_pit_fall(player, pits)`: Detect pit entry

### 9.2 Gravity (physics/gravity.py)

**Function:**
- `apply_gravity(entity, dt)`: Add downward acceleration
  - Increase vertical velocity by GRAVITY constant
  - Cap at MAX_FALL_SPEED

## 10. CAMERA SYSTEM (camera.py)

**Class: Camera**

**Attributes:**
- `x`, `y`: Camera position
- `width`, `height`: Viewport dimensions
- `target`: Player object to follow
- `level_bounds`: Maximum camera position

**Methods:**
- `update(target_pos, level_width)`: Follow player smoothly
- `apply(entity_pos)`: Transform world coordinates to screen coordinates
- `is_visible(entity)`: Check if entity is in viewport

**Behavior:**
- Follow player horizontally
- Don't scroll past level boundaries
- Keep player centered unless near edges

## 11. UI SYSTEM

### 11.1 HUD (ui/hud.py)

**Display:**
- Lives remaining (3 hearts/icons)
- Current level number
- Power-up timer (when active)

### 11.2 Menus (ui/menu.py)

**Main Menu:**
- Start Game
- Quit

**Pause Menu:**
- Resume
- Restart Level
- Main Menu

**Game Over Screen:**
- Retry
- Main Menu

**Level Complete Screen:**
- Next Level
- Main Menu

## 12. DEVELOPMENT PHASES

### Phase 1: Setup (Day 1)
1. Create project structure
2. Install Pygame
3. Set up main.py with basic window
4. Implement constants.py

### Phase 2: Level Generator (Day 1-2)
1. Implement level_generator.py
2. Define level format precisely
3. Generate all 5 level files
4. Validate JSON output

### Phase 3: Core Mechanics (Day 2-3)
1. Implement Player class
2. Add gravity and jumping
3. Create basic collision detection
4. Implement camera system

### Phase 4: Level Loading (Day 3-4)
1. Create level loader
2. Parse JSON levels
3. Render platforms
4. Test level progression

### Phase 5: Enemies (Day 4-5)
1. Implement Polocho class
2. Add patrol AI
3. Implement stomp mechanics
4. Add player damage system

### Phase 6: Power-Ups (Day 5-6)
1. Create PowerUp class
2. Implement collection
3. Add Laser projectile class
4. Implement shooting mechanics

### Phase 7: UI & Polish (Day 6-7)
1. Create all menus
2. Implement HUD
3. Add game state management
4. Add placeholder graphics/sounds
5. Final testing and bug fixes

## 13. ASSET REQUIREMENTS

### 13.1 Sprites Needed
- Sancho: idle, walk (4 frames), jump, shoot
- Polocho: walk (2 frames), squashed
- Platform tiles: ground, floating platform
- Arepa Dorada: animated (4 frames)
- Laser beam: single sprite
- Background: solid colors or simple texture

### 13.2 Sound Effects
- Jump
- Land
- Enemy defeat (stomp)
- Laser shoot
- Power-up collect
- Player hurt
- Level complete

### 13.3 Music
- Menu theme
- Level background music (1-2 tracks)

**Note**: Initial implementation can use colored rectangles and basic shapes as placeholders.

## 14. TESTING CHECKLIST

- [ ] Player movement and jumping feels responsive
- [ ] Collision detection is accurate
- [ ] Enemies patrol correctly and turn at boundaries
- [ ] Stomping enemies works reliably
- [ ] Power-up collection triggers laser mode
- [ ] Laser projectiles hit enemies and walls
- [ ] Pits cause player death
- [ ] Lives system works correctly
- [ ] Level progression flows smoothly
- [ ] All 5 levels are completable
- [ ] Camera follows player correctly
- [ ] Menus navigate properly
- [ ] Game can be paused and resumed

## 15. RUNNING THE GAME

```bash
# Install dependencies
pip install -r requirements.txt

# Generate levels (run once)
python tools/level_generator.py

# Run game
python src/main.py
```

## 16. FUTURE ENHANCEMENTS (Post-MVP)

- Score system
- High score tracking
- Additional enemy types
- More power-ups
- Level editor
- Sound/music toggle
- Gamepad support
- Multiple difficulty modes
