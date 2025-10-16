"""
SANCHO BROS - Enemy Entity Module

Defines the Polocho enemy class with patrol AI and basic behaviors.
"""

import pygame
from src.constants import COLOR_ENEMY, ENEMY_PATROL_SPEED, ENEMY_WIDTH, ENEMY_HEIGHT


class Polocho:
    """
    Polocho enemy class - the main antagonist in Sancho Bros.

    Enemies patrol between boundaries, can be defeated by stomping or lasers,
    and damage the player on contact.
    """

    def __init__(self, x, y, patrol_left, patrol_right):
        """
        Initialize a Polocho enemy.

        Args:
            x (int): Initial x position
            y (int): Initial y position
            patrol_left (int): Left boundary for patrol movement
            patrol_right (int): Right boundary for patrol movement
        """
        # Position and movement
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)

        # Size and collision
        self.width = ENEMY_WIDTH
        self.height = ENEMY_HEIGHT
        self.rect = pygame.Rect(x, y, self.width, self.height)

        # Patrol AI
        self.patrol_left = patrol_left
        self.patrol_right = patrol_right
        self.speed = ENEMY_PATROL_SPEED
        self.facing_direction = "RIGHT"

        # State
        self.is_alive = True

    def update(self, dt, platforms):
        """
        Update enemy state (placeholder for Phase 5).

        Args:
            dt (float): Delta time in seconds
            platforms (list): List of platform objects for collision
        """
        if not self.is_alive:
            return

        # Update rect position to match logical position
        self.rect.x = int(self.position.x)
        self.rect.y = int(self.position.y)

    def patrol(self):
        """
        Handle patrol movement between boundaries (placeholder for US020).

        Will be implemented in US020: Implement Enemy Patrol AI
        """
        pass

    def check_boundaries(self):
        """
        Check patrol boundaries and turn around if needed (placeholder for US020).

        Will be implemented in US020: Implement Enemy Patrol AI
        """
        pass

    def die(self):
        """
        Handle enemy death.

        Called when enemy is defeated by stomp or laser.
        Sets is_alive to False to stop updates and rendering.
        """
        self.is_alive = False

    def render(self, screen, camera):
        """
        Draw the enemy on screen.

        Args:
            screen (pygame.Surface): Surface to draw on
            camera: Camera object with x, y offset attributes
        """
        if not self.is_alive:
            return

        # Calculate screen position relative to camera
        screen_x = self.position.x - camera.x
        screen_y = self.position.y - camera.y

        # Draw as red rectangle (placeholder graphics)
        pygame.draw.rect(screen, COLOR_ENEMY,
                        (screen_x, screen_y, self.width, self.height))
