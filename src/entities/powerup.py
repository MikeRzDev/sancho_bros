# SANCHO BROS - PowerUp Entity
# La Arepa Dorada power-up that grants temporary laser shooting ability

import pygame
import math
from src.constants import COLOR_POWERUP, POWERUP_WIDTH, POWERUP_HEIGHT


class PowerUp:
    """
    PowerUp entity class representing La Arepa Dorada collectible.
    Provides visual feedback through bobbing animation and collision detection.
    """

    def __init__(self, x, y, powerup_type):
        """
        Initialize a PowerUp entity.

        Args:
            x (float): X position in world coordinates
            y (float): Y position in world coordinates
            powerup_type (str): Type of power-up (e.g., "arepa_dorada")
        """
        self.position = pygame.Vector2(x, y)
        self.original_y = y  # Store for bobbing animation reference
        self.width = POWERUP_WIDTH
        self.height = POWERUP_HEIGHT
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.type = powerup_type
        self.collected = False
        self.animation_frame = 0.0

    def update(self, dt):
        """
        Update power-up state and animation.

        Args:
            dt (float): Delta time in seconds
        """
        if self.collected:
            return

        # Bobbing animation using sine wave
        # Speed of 2 creates ~2 second cycle, amplitude of 10 pixels
        self.animation_frame += dt * 2
        offset = math.sin(self.animation_frame) * 10
        self.position.y = self.original_y + offset

        # Update collision rect to match animated position
        self.rect.x = self.position.x
        self.rect.y = self.position.y

    def check_collection(self, player):
        """
        Check if player has collided with this power-up.

        Args:
            player: Player entity object with a rect attribute

        Returns:
            bool: True if player is colliding and power-up not yet collected
        """
        if self.collected:
            return False

        # AABB collision detection
        from src.physics.collision import check_aabb_collision
        return check_aabb_collision(player.rect, self.rect)

    def collect(self):
        """
        Mark power-up as collected and provide feedback.
        """
        self.collected = True
        print(f"Power-up collected: {self.type}")

    def render(self, screen, camera):
        """
        Draw power-up on screen.

        Args:
            screen: Pygame surface to draw on
            camera: Camera object with x, y offset attributes
        """
        if self.collected:
            return

        # Transform world coordinates to screen coordinates
        screen_x = self.position.x - camera.x
        screen_y = self.position.y - camera.y

        # Draw as colored rectangle (placeholder graphics)
        pygame.draw.rect(screen, COLOR_POWERUP,
                        (screen_x, screen_y, self.width, self.height))
