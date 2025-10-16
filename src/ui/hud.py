"""
SANCHO BROS - HUD (Heads-Up Display)
Displays game information: lives, level number, and power-up status.
"""

import pygame
from src.constants import SCREEN_WIDTH


class HUD:
    """
    HUD class that displays game information overlay.
    Renders lives, level number, and power-up timer in screen space.
    """

    def __init__(self):
        """Initialize HUD with fonts."""
        self.font = pygame.font.Font(None, 32)
        self.small_font = pygame.font.Font(None, 24)

    def render(self, screen, player, level):
        """
        Render HUD elements on screen.

        Args:
            screen: pygame.Surface to draw on
            player: Player object with lives, has_powerup, powerup_timer
            level: Level object with level_number
        """
        # Lives display (top-left corner)
        lives_text = f"Lives: {player.lives}"
        lives_surface = self.font.render(lives_text, True, (255, 255, 255))
        screen.blit(lives_surface, (10, 10))

        # Level number (top-right corner)
        level_text = f"Level {level.level_number}"
        level_surface = self.font.render(level_text, True, (255, 255, 255))
        level_rect = level_surface.get_rect(topright=(SCREEN_WIDTH - 10, 10))
        screen.blit(level_surface, level_rect)

        # Power-up timer (below lives, only when active)
        if player.has_powerup:
            timer = int(player.powerup_timer)
            power_text = f"POWER: {timer}s"
            power_surface = self.font.render(power_text, True, (255, 215, 0))  # Gold color
            screen.blit(power_surface, (10, 50))
