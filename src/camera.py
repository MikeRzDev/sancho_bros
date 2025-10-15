"""
SANCHO BROS - Camera System
Manages viewport and camera following for scrolling levels.
"""

import pygame
from src.constants import SCREEN_WIDTH, SCREEN_HEIGHT


class Camera:
    """
    Camera class for viewport management and player following.
    Handles smooth scrolling and level boundary clamping.
    """

    def __init__(self, width, height):
        """
        Initialize the camera with viewport dimensions.

        Args:
            width (int): Viewport width (typically SCREEN_WIDTH)
            height (int): Viewport height (typically SCREEN_HEIGHT)
        """
        self.width = width
        self.height = height
        self.x = 0
        self.y = 0
        self.level_width = 0

    def update(self, target_pos, level_width):
        """
        Update camera position to follow target smoothly.
        Camera centers on target horizontally while respecting level boundaries.

        Args:
            target_pos (pygame.Vector2): Position of the entity to follow
            level_width (int): Total width of the current level
        """
        self.level_width = level_width

        # Center camera on target horizontally
        self.x = target_pos.x - self.width // 2

        # Clamp to level boundaries
        # Left boundary: don't show area left of level
        self.x = max(0, self.x)

        # Right boundary: don't show area right of level
        # If level is smaller than screen, camera stays at 0
        if level_width > self.width:
            self.x = min(self.x, level_width - self.width)
        else:
            self.x = 0

        # Keep camera at y=0 for 2D side-scroller (no vertical scrolling)
        self.y = 0

    def apply(self, world_pos):
        """
        Transform world coordinates to screen coordinates.
        Subtracts camera offset from world position to get screen position.

        Args:
            world_pos (pygame.Vector2): World coordinates

        Returns:
            tuple: (screen_x, screen_y) coordinates for rendering
        """
        return world_pos.x - self.x, world_pos.y - self.y

    def is_visible(self, entity):
        """
        Check if an entity is visible within the current viewport.
        Useful for optimization (don't render off-screen entities).

        Args:
            entity: Game entity with a rect attribute

        Returns:
            bool: True if entity is visible in viewport, False otherwise
        """
        return (entity.rect.right > self.x and
                entity.rect.left < self.x + self.width)
