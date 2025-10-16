"""
SANCHO BROS - Player Entity Class
Represents Sancho, the player character.
"""

import pygame
from src.constants import (
    PLAYER_WIDTH,
    PLAYER_HEIGHT,
    PLAYER_LIVES,
    COLOR_PLAYER,
    GRAVITY,
    JUMP_STRENGTH,
    PLAYER_SPEED,
    LASER_DURATION
)


class Player:
    """
    Player entity class representing Sancho, the coffee farmer protagonist.
    Handles player state, movement, collision, and rendering.
    """

    def __init__(self, x, y):
        """
        Initialize the player at the given position.

        Args:
            x (int): Initial x-coordinate
            y (int): Initial y-coordinate
        """
        # Position and movement
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)

        # Dimensions
        self.width = PLAYER_WIDTH
        self.height = PLAYER_HEIGHT
        self.rect = pygame.Rect(x, y, self.width, self.height)

        # Game state
        self.lives = PLAYER_LIVES
        self.has_powerup = False
        self.powerup_timer = 0.0
        self.laser_cooldown = 0.0

        # Invincibility system
        self.is_invincible = False
        self.invincibility_timer = 0.0
        self.invincibility_duration = 2.0  # 2 seconds of invincibility after taking damage

        # Movement state
        self.facing_direction = "RIGHT"
        self.is_jumping = False
        self.is_grounded = False
        self.was_grounded = False  # Track previous frame's grounded state

        # Input tracking (to prevent holding jump key)
        self.space_was_pressed = False

    def update(self, dt, platforms):
        """
        Update player state each frame.

        Args:
            dt (float): Delta time in seconds since last frame
            platforms (list): List of platform objects for collision detection
        """
        # Get keyboard input and process controls
        keys = pygame.key.get_pressed()
        self.handle_input(keys)

        # Apply physics - gravity system
        from src.physics.gravity import apply_gravity
        apply_gravity(self, dt)

        # Update position based on velocity
        self.position.x += self.velocity.x
        self.position.y += self.velocity.y

        # Update rect position to match current position
        self.rect.x = int(self.position.x)
        self.rect.y = int(self.position.y)

        # Check collisions with platforms (handles grounded detection)
        self.check_collision(platforms)

        # Update powerup timer if active
        if self.has_powerup and self.powerup_timer > 0:
            self.powerup_timer -= dt
            if self.powerup_timer <= 0:
                self.has_powerup = False
                self.powerup_timer = 0.0

        # Update invincibility timer if active
        if self.is_invincible and self.invincibility_timer > 0:
            self.invincibility_timer -= dt
            if self.invincibility_timer <= 0:
                self.is_invincible = False
                self.invincibility_timer = 0.0

        # Update laser cooldown if active
        if self.laser_cooldown > 0:
            self.laser_cooldown -= dt

    def handle_input(self, keys):
        """
        Process keyboard input for player controls.

        Args:
            keys: pygame.key.get_pressed() result
        """
        # Reset horizontal velocity
        self.velocity.x = 0

        # Horizontal movement (LEFT arrow or A key)
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.velocity.x = -PLAYER_SPEED
            self.facing_direction = "LEFT"
        # Horizontal movement (RIGHT arrow or D key)
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.velocity.x = PLAYER_SPEED
            self.facing_direction = "RIGHT"

        # Jump control (SPACE key)
        # Allow jump if: space is pressed AND (player just landed OR space wasn't pressed before)
        space_is_pressed = keys[pygame.K_SPACE]
        just_landed = self.is_grounded and not self.was_grounded

        if space_is_pressed and (just_landed or not self.space_was_pressed):
            self.jump()

        self.space_was_pressed = space_is_pressed

    def jump(self):
        """
        Initiate a jump if the player is grounded.
        Sets vertical velocity to JUMP_STRENGTH and updates jump state flags.
        """
        if self.is_grounded:
            self.velocity.y = JUMP_STRENGTH
            self.is_jumping = True
            self.is_grounded = False

    def apply_gravity(self, dt):
        """
        Apply gravity to the player's vertical velocity.

        Args:
            dt (float): Delta time in seconds since last frame
        """
        # Placeholder - full implementation in US011
        pass

    def check_collision(self, platforms):
        """
        Check and resolve collisions with platforms using the collision system.
        Uses the dedicated collision module for proper AABB collision resolution.

        Args:
            platforms (list): List of platform objects with rect attribute
        """
        # Save previous grounded state
        self.was_grounded = self.is_grounded

        # Use collision module for full collision resolution
        from src.physics.collision import resolve_platform_collision
        resolve_platform_collision(self, platforms)

    def take_damage(self):
        """
        Handle player taking damage (lose a life).
        Only applies damage if player is not currently invincible.
        Activates invincibility period after taking damage.

        Returns:
            bool: True if damage was applied, False if player was invincible
        """
        # Don't take damage if invincible
        if self.is_invincible:
            return False

        # Apply damage
        self.lives -= 1
        print(f"Player hit! Lives remaining: {self.lives}")

        # Activate invincibility
        self.is_invincible = True
        self.invincibility_timer = self.invincibility_duration

        return True

    def apply_knockback(self, direction, strength=5):
        """
        Apply knockback force to player (pushes player away from enemy).

        Args:
            direction (str): "LEFT" or "RIGHT" - direction to push player
            strength (int): Knockback force strength (default 5)
        """
        if direction == "LEFT":
            self.velocity.x = -strength
        elif direction == "RIGHT":
            self.velocity.x = strength

    def collect_powerup(self):
        """
        Activate power-up effect when La Arepa Dorada is collected.
        Grants temporary laser shooting ability.
        """
        self.has_powerup = True
        self.powerup_timer = LASER_DURATION
        print(f"Power-up activated! Duration: {LASER_DURATION}s")

    def shoot(self):
        """
        Shoot a laser projectile in the direction player is facing.
        Only works when powered up and cooldown is ready.

        Returns:
            Laser or None: New Laser instance if shot is successful, None otherwise
        """
        # Can only shoot if powered up and cooldown is ready
        if not self.has_powerup or self.laser_cooldown > 0:
            return None

        # Import here to avoid circular dependency
        from src.entities.projectile import Laser

        # Create laser at player position (centered vertically)
        laser_x = self.position.x + self.width if self.facing_direction == "RIGHT" else self.position.x
        laser_y = self.position.y + self.height // 2 - 2  # Center vertically (laser is 4px tall)

        # Reset cooldown
        from src.constants import LASER_COOLDOWN
        self.laser_cooldown = LASER_COOLDOWN

        print(f"Player shot laser! Direction: {self.facing_direction}")
        return Laser(laser_x, laser_y, self.facing_direction)

    def render(self, screen, camera):
        """
        Draw the player on screen relative to camera position.

        Args:
            screen: pygame.Surface to draw on
            camera: Camera object with x, y offset attributes
        """
        # Calculate screen position relative to camera
        screen_x = self.position.x - camera.x
        screen_y = self.position.y - camera.y

        # Change color if powered (yellow indicates power-up is active)
        color = (255, 255, 0) if self.has_powerup else COLOR_PLAYER

        # Draw player as a colored rectangle (placeholder for sprite)
        pygame.draw.rect(
            screen,
            color,
            (screen_x, screen_y, self.width, self.height)
        )
