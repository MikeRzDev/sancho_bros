"""
SANCHO BROS - Projectile Entity Class
Represents laser projectiles shot by the player when powered up.
"""

import pygame
from src.constants import DEBUG


class Laser:
    """
    Laser projectile class that moves horizontally and destroys enemies.
    Created when player shoots while powered up.
    """

    def __init__(self, x, y, direction):
        """
        Initialize a laser projectile.

        Args:
            x (float): Starting x-coordinate (player position)
            y (float): Starting y-coordinate (player position)
            direction (str): "LEFT" or "RIGHT" - direction laser travels
        """
        # Position and movement
        self.position = pygame.Vector2(x, y)
        self.direction = direction
        self.speed = 10  # Fast horizontal movement

        # Set velocity based on direction
        if direction == "RIGHT":
            self.velocity = pygame.Vector2(self.speed, 0)
        else:  # LEFT
            self.velocity = pygame.Vector2(-self.speed, 0)

        # Dimensions
        self.width = 16
        self.height = 4
        self.rect = pygame.Rect(x, y, self.width, self.height)

        # Lifetime management
        self.lifetime = 2.0  # Seconds before auto-destruction
        self.is_active = True

    def update(self, dt, platforms, enemies):
        """
        Update laser position and check collisions.

        Args:
            dt (float): Delta time in seconds since last frame
            platforms (list): List of platform objects
            enemies (list): List of enemy objects
        """
        if not self.is_active:
            return

        # Update lifetime
        self.lifetime -= dt
        if self.lifetime <= 0:
            self.destroy()
            return

        # Move laser
        self.position += self.velocity
        self.rect.x = int(self.position.x)
        self.rect.y = int(self.position.y)

        # Check collisions
        self.check_collisions(platforms, enemies)

    def check_collisions(self, platforms, enemies):
        """
        Check if laser hit platforms or enemies.

        Args:
            platforms (list): List of platform objects with rect attribute
            enemies (list): List of enemy objects with rect and is_alive attributes
        """
        from src.physics.collision import check_aabb_collision

        # Check platform collision - laser destroys on contact
        for platform in platforms:
            if check_aabb_collision(self.rect, platform.rect):
                self.destroy()
                return

        # Check enemy collision - laser destroys enemy and itself
        for enemy in enemies:
            if enemy.is_alive and check_aabb_collision(self.rect, enemy.rect):
                enemy.die()
                self.destroy()
                if DEBUG:
                    print(f"Laser hit enemy at ({enemy.position.x:.1f}, {enemy.position.y:.1f})")
                return

    def destroy(self):
        """Deactivate the laser (marks it for removal)."""
        self.is_active = False

    def render(self, screen, camera):
        """
        Draw the laser on screen relative to camera position.

        Args:
            screen: pygame.Surface to draw on
            camera: Camera object with x, y offset attributes
        """
        if not self.is_active:
            return

        # Calculate screen position relative to camera
        screen_x = self.position.x - camera.x
        screen_y = self.position.y - camera.y

        # Draw as bright cyan rectangle (clearly visible)
        pygame.draw.rect(
            screen,
            (0, 255, 255),  # Cyan
            (screen_x, screen_y, self.width, self.height)
        )
