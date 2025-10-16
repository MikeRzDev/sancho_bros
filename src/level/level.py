"""
SANCHO BROS - Level Class
Manages all level entities, platforms, enemies, powerups, and game logic.
"""

import pygame
from src.level.tile import Platform


class Level:
    """
    Level class that manages all level entities and game logic.
    Handles platforms, enemies, powerups, pits, and goal detection.
    """

    def __init__(self, level_data):
        """
        Initialize a level from parsed JSON data.

        Args:
            level_data (dict): Parsed JSON level data from level_loader
        """
        # Basic level information
        self.level_number = level_data['level_number']
        self.width = level_data['width']
        self.height = level_data['height']
        self.background_color = tuple(level_data['background_color'])

        # Player spawn and goal positions
        self.player_spawn = level_data['player_spawn']
        self.goal = level_data['goal']
        self.pits = level_data['pits']

        # Create platform objects from JSON data
        self.platforms = []
        for p_data in level_data['platforms']:
            platform = Platform(
                p_data['x'], p_data['y'],
                p_data['width'], p_data['height'],
                p_data['type']
            )
            self.platforms.append(platform)

        # Placeholders for Phase 5 & 6
        self.enemies = []
        self.powerups = []

    def update(self, dt, player):
        """
        Update all level entities.

        Args:
            dt (float): Delta time in seconds
            player: Player object
        """
        # Update enemies (Phase 5)
        # Update powerups (Phase 6)
        pass

    def render(self, screen, camera):
        """
        Render all level elements relative to camera.

        Args:
            screen: pygame.Surface to draw on
            camera: Camera object with x, y offset attributes
        """
        # Fill background
        screen.fill(self.background_color)

        # Render all platforms
        for platform in self.platforms:
            platform.render(screen, camera)

        # Render goal (placeholder - green rectangle)
        goal_screen_x = self.goal['x'] - camera.x
        goal_screen_y = self.goal['y'] - camera.y
        pygame.draw.rect(screen, (0, 255, 0),
                        (goal_screen_x, goal_screen_y, 50, 50))

    def check_goal(self, player):
        """
        Check if player has reached the level goal.

        Args:
            player: Player object

        Returns:
            bool: True if player is within 50 pixels of goal
        """
        distance = abs(player.position.x - self.goal['x'])
        return distance < 50

    def check_pits(self, player):
        """
        Check if player has fallen into a pit.

        Args:
            player: Player object

        Returns:
            bool: True if player is in a pit zone
        """
        for pit in self.pits:
            if (player.position.x >= pit['x'] and
                player.position.x <= pit['x'] + pit['width'] and
                player.position.y > self.height - 100):
                return True
        return False

    def get_platforms(self):
        """
        Get list of all platforms in the level.

        Returns:
            list: List of Platform objects
        """
        return self.platforms

    def get_spawn_position(self):
        """
        Get player spawn position for this level.

        Returns:
            tuple: (x, y) spawn coordinates
        """
        return (self.player_spawn['x'], self.player_spawn['y'])

    def reset(self):
        """
        Reset level state for retrying.
        Resets enemies, powerups, and other dynamic entities.
        """
        # Reset enemies (Phase 5)
        # Reset powerups (Phase 6)
        pass
