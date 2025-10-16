"""
SANCHO BROS - Collision Detection System
Provides AABB collision detection and platform collision resolution.
"""

import pygame


def check_aabb_collision(rect1, rect2):
    """
    Axis-Aligned Bounding Box (AABB) collision detection.

    Args:
        rect1 (pygame.Rect): First rectangle
        rect2 (pygame.Rect): Second rectangle

    Returns:
        bool: True if rectangles overlap, False otherwise
    """
    return rect1.colliderect(rect2)


def resolve_platform_collision(entity, platforms):
    """
    Resolve collisions between entity and platforms.
    Handles top, bottom, and side collisions with proper physics response.

    Args:
        entity: Game entity with rect, position, velocity, width, height attributes
        platforms (list): List of platform objects with rect attribute
    """
    # Assume not grounded initially (will be set to True if landing on platform)
    entity.is_grounded = False

    for platform in platforms:
        if check_aabb_collision(entity.rect, platform.rect):
            # Calculate overlap on each axis
            overlap_x = min(
                entity.rect.right - platform.rect.left,
                platform.rect.right - entity.rect.left
            )
            overlap_y = min(
                entity.rect.bottom - platform.rect.top,
                platform.rect.bottom - entity.rect.top
            )

            # Resolve smallest overlap (most likely collision side)
            if overlap_x < overlap_y:
                # Side collision (left or right)
                if entity.rect.centerx < platform.rect.centerx:
                    # Colliding from left side
                    entity.position.x = platform.rect.left - entity.width
                    entity.velocity.x = 0
                else:
                    # Colliding from right side
                    entity.position.x = platform.rect.right
                    entity.velocity.x = 0
            else:
                # Top/bottom collision
                if entity.velocity.y > 0:
                    # Landing on top of platform (falling down)
                    entity.position.y = platform.rect.top - entity.height
                    entity.velocity.y = 0
                    entity.is_grounded = True
                    entity.is_jumping = False
                elif entity.velocity.y < 0:
                    # Hitting bottom of platform (moving up)
                    entity.position.y = platform.rect.bottom
                    entity.velocity.y = 0

            # Update rect to match resolved position
            entity.rect.x = int(entity.position.x)
            entity.rect.y = int(entity.position.y)


def check_enemy_collision(player, enemies):
    """
    Check collision between player and enemies.

    Args:
        player: Player entity with rect attribute
        enemies (list): List of enemy entities with rect and is_alive attributes

    Returns:
        Enemy object if collision detected, None otherwise
    """
    for enemy in enemies:
        if enemy.is_alive and check_aabb_collision(player.rect, enemy.rect):
            return enemy
    return None


def check_stomp(player, enemy):
    """
    Check if player is stomping on enemy from above.

    Stomp requirements:
    - Enemy must be alive
    - Player must be falling (velocity.y > 0)
    - Player's bottom must hit enemy's top half
    - Horizontal overlap must exist

    Args:
        player: Player entity with rect and velocity attributes
        enemy: Enemy entity with rect and is_alive attributes

    Returns:
        bool: True if valid stomp, False otherwise
    """
    # Enemy must be alive
    if not enemy.is_alive:
        return False

    # Player must be falling
    if player.velocity.y <= 0:
        return False

    # Check if player's bottom is hitting enemy's top half
    # Player bottom should be between enemy top and enemy center
    if player.rect.bottom >= enemy.rect.top and player.rect.bottom <= enemy.rect.centery:
        # Check horizontal overlap
        if check_aabb_collision(player.rect, enemy.rect):
            return True

    return False
