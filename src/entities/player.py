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
    PLAYER_SPEED
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

        # Movement state
        self.facing_direction = "RIGHT"
        self.is_jumping = False
        self.is_grounded = False

    def update(self, dt, platforms):
        """
        Update player state each frame.

        Args:
            dt (float): Delta time in seconds since last frame
            platforms (list): List of platform objects for collision detection
        """
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

    def handle_input(self, keys):
        """
        Process keyboard input for player controls.

        Args:
            keys: pygame.key.get_pressed() result
        """
        # Placeholder - full implementation in US012
        pass

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
        Check and resolve collisions with platforms.
        Handles grounded detection for physics system (US011).
        Full collision resolution will be implemented in US013.

        Args:
            platforms (list): List of platform objects with rect attribute
        """
        # Assume not grounded initially
        self.is_grounded = False

        # Check collision with each platform
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                # Vertical collision (landing on or hitting platform from below)
                if self.velocity.y > 0:  # Falling down
                    # Landing on top of platform
                    if self.rect.bottom >= platform.rect.top:
                        self.rect.bottom = platform.rect.top
                        self.position.y = self.rect.y
                        self.velocity.y = 0
                        self.is_grounded = True
                        self.is_jumping = False
                elif self.velocity.y < 0:  # Moving up
                    # Hitting platform from below
                    if self.rect.top <= platform.rect.bottom:
                        self.rect.top = platform.rect.bottom
                        self.position.y = self.rect.y
                        self.velocity.y = 0

    def take_damage(self):
        """
        Handle player taking damage (lose a life).
        """
        if self.lives > 0:
            self.lives -= 1
            # Additional damage handling (invincibility, respawn) in future user stories

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

        # Draw player as a colored rectangle (placeholder for sprite)
        pygame.draw.rect(
            screen,
            COLOR_PLAYER,
            (screen_x, screen_y, self.width, self.height)
        )
