"""
SANCHO BROS - Platform/Tile Class
Represents platforms and tiles in the game world.
"""

import pygame


class Platform:
    """
    Platform class for solid and floating platforms.
    Used for collision detection and rendering.
    """

    def __init__(self, x, y, width, height, platform_type):
        """
        Initialize a platform at the given position.

        Args:
            x (int): X-coordinate of platform top-left corner
            y (int): Y-coordinate of platform top-left corner
            width (int): Platform width in pixels
            height (int): Platform height in pixels
            platform_type (str): Type of platform - "solid" or "floating"
        """
        self.rect = pygame.Rect(x, y, width, height)
        self.type = platform_type

    def render(self, screen, camera):
        """
        Draw the platform on screen relative to camera position.

        Args:
            screen: pygame.Surface to draw on
            camera: Camera object with x, y offset attributes
        """
        # Calculate screen position relative to camera
        screen_x = self.rect.x - camera.x
        screen_y = self.rect.y - camera.y

        # Choose color based on platform type
        if self.type == "solid":
            color = (139, 69, 19)  # Brown for ground platforms
        else:  # "floating"
            color = (100, 100, 100)  # Gray for floating platforms

        # Draw platform as a colored rectangle
        pygame.draw.rect(
            screen,
            color,
            (screen_x, screen_y, self.rect.width, self.rect.height)
        )
