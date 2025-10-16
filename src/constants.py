# SANCHO BROS - GAME CONSTANTS
# Centralized configuration for all game parameters

# ===== SCREEN CONSTANTS =====
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# ===== PHYSICS CONSTANTS =====
GRAVITY = 0.8              # Applied each frame (pixels/frame²)
MAX_FALL_SPEED = 15        # Terminal velocity
JUMP_STRENGTH = -16        # Initial upward velocity (negative = up) - reaches ~160px
PLAYER_SPEED = 5           # Horizontal pixels per frame

# ===== GAME RULES CONSTANTS =====
PLAYER_LIVES = 3           # Starting lives
LASER_DURATION = 10        # Seconds power-up lasts
LASER_COOLDOWN = 0.5       # Seconds between laser shots

# ===== ENTITY SIZE CONSTANTS =====
# Player (Sancho)
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60

# Enemy (Polocho)
ENEMY_WIDTH = 40
ENEMY_HEIGHT = 50

# Platform
PLATFORM_DEFAULT_WIDTH = 100
PLATFORM_DEFAULT_HEIGHT = 20

# Power-up (La Arepa Dorada)
POWERUP_WIDTH = 30
POWERUP_HEIGHT = 30

# Laser Projectile
LASER_WIDTH = 10
LASER_HEIGHT = 4
LASER_SPEED = 12           # Horizontal speed (pixels/frame)
LASER_LIFETIME = 2.0       # Seconds before auto-destruction

# ===== COLOR CONSTANTS (RGB tuples) =====
# Background and environment
COLOR_BACKGROUND = (135, 206, 235)      # Sky blue
COLOR_SKY = (135, 206, 235)

# Entities
COLOR_PLAYER = (0, 0, 255)              # Blue
COLOR_ENEMY = (255, 0, 0)               # Red

# Platforms
COLOR_PLATFORM_SOLID = (139, 69, 19)    # Saddle brown (ground)
COLOR_PLATFORM_FLOATING = (169, 169, 169)  # Dark gray (floating platforms)

# Power-ups and projectiles
COLOR_POWERUP = (255, 215, 0)           # Gold
COLOR_LASER = (0, 255, 255)             # Cyan

# UI
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_RED = (255, 0, 0)
COLOR_GREEN = (0, 255, 0)

# ===== ENEMY AI CONSTANTS =====
ENEMY_PATROL_SPEED = 2     # Horizontal pixels per frame

# ===== GAME STATE CONSTANTS =====
class GameState:
    """Game state constants for state management."""
    MENU = "MENU"
    PLAYING = "PLAYING"
    PAUSED = "PAUSED"
    GAME_OVER = "GAME_OVER"
    LEVEL_COMPLETE = "LEVEL_COMPLETE"
