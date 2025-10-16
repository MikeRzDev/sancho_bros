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
        self.is_grounded = False
        self.is_jumping = False  # Enemies don't jump, but collision system expects this

    def update(self, dt, platforms):
        """
        Update enemy state with patrol AI, physics, and collision detection.

        Args:
            dt (float): Delta time in seconds
            platforms (list): List of platform objects for collision
        """
        if not self.is_alive:
            return

        # Patrol movement with edge detection (sets velocity.x)
        self.patrol(platforms)

        # Apply gravity
        from src.physics.gravity import apply_gravity
        self.is_grounded = False  # Reset before collision detection
        apply_gravity(self, dt)

        # Update position based on velocity
        self.position.x += self.velocity.x
        self.position.y += self.velocity.y

        # Check collisions with platforms
        from src.physics.collision import resolve_platform_collision
        resolve_platform_collision(self, platforms)

        # Update rect to match resolved position
        self.rect.x = int(self.position.x)
        self.rect.y = int(self.position.y)

    def patrol(self, platforms=None):
        """
        Handle patrol movement between boundaries.

        Enemies move horizontally at constant speed, reversing direction
        when they reach patrol_left or patrol_right boundaries.

        Args:
            platforms (list, optional): List of platforms for edge detection
        """
        # Move based on current direction
        if self.facing_direction == "RIGHT":
            self.velocity.x = self.speed

            # Check right boundary
            if self.position.x >= self.patrol_right:
                self.facing_direction = "LEFT"
                self.position.x = self.patrol_right  # Snap to boundary
            # Check for platform edge (optional safety check)
            elif platforms and not self.is_platform_ahead(platforms):
                self.facing_direction = "LEFT"

        elif self.facing_direction == "LEFT":
            self.velocity.x = -self.speed

            # Check left boundary
            if self.position.x <= self.patrol_left:
                self.facing_direction = "RIGHT"
                self.position.x = self.patrol_left  # Snap to boundary
            # Check for platform edge (optional safety check)
            elif platforms and not self.is_platform_ahead(platforms):
                self.facing_direction = "RIGHT"

    def is_platform_ahead(self, platforms):
        """
        Check if there's a platform in front of the enemy to prevent falling off edges.

        Args:
            platforms (list): List of platform objects

        Returns:
            bool: True if platform detected ahead, False otherwise
        """
        # Check distance slightly ahead of enemy
        check_distance = self.width + 5

        if self.facing_direction == "RIGHT":
            check_x = self.position.x + check_distance
        else:
            check_x = self.position.x - check_distance

        # Check slightly below enemy's feet
        check_y = self.position.y + self.height + 5

        # Look for platform at check position
        for platform in platforms:
            if platform.rect.collidepoint(check_x, check_y):
                return True

        return False

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
