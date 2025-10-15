"""
SANCHO BROS - Gravity Physics System
Handles gravity application for all entities in the game.
"""

from src.constants import GRAVITY, MAX_FALL_SPEED


def apply_gravity(entity, dt):
    """
    Apply gravity to an entity's vertical velocity.

    Gravity only applies when the entity is not grounded (in the air).
    The vertical velocity is capped at MAX_FALL_SPEED to prevent
    excessive falling speeds.

    Args:
        entity: Game entity with velocity, is_grounded attributes
        dt (float): Delta time in seconds (not currently used, kept for future frame-independent physics)

    Technical Notes:
        - Gravity constant: 0.8 pixels/frame²
        - Max fall speed: 15 pixels/frame (terminal velocity)
        - Y-axis increases downward (pygame convention)
    """
    if not entity.is_grounded:
        # Apply gravity acceleration to vertical velocity
        entity.velocity.y += GRAVITY

        # Cap fall speed at terminal velocity
        if entity.velocity.y > MAX_FALL_SPEED:
            entity.velocity.y = MAX_FALL_SPEED
