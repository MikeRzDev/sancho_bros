"""
SANCHO BROS - UI Screens Module
Contains PauseMenu and GameOverScreen classes for game UI.
"""

import pygame
from src.constants import SCREEN_WIDTH, SCREEN_HEIGHT


class PauseMenu:
    """
    Pause menu overlay that appears when the game is paused.
    Displays pause title and menu options.
    """

    def __init__(self, screen_width, screen_height):
        """
        Initialize pause menu.

        Args:
            screen_width (int): Width of the game screen
            screen_height (int): Height of the game screen
        """
        self.screen_width = screen_width
        self.screen_height = screen_height

        # Initialize fonts
        self.title_font = pygame.font.Font(None, 72)
        self.option_font = pygame.font.Font(None, 36)

    def render(self, screen):
        """
        Render pause menu overlay with semi-transparent background.

        Args:
            screen (pygame.Surface): The game screen to render on
        """
        # Create semi-transparent dark overlay
        overlay = pygame.Surface((self.screen_width, self.screen_height))
        overlay.set_alpha(128)  # 50% transparency
        overlay.fill((0, 0, 0))
        screen.blit(overlay, (0, 0))

        # Render "PAUSED" title
        title = self.title_font.render("PAUSED", True, (255, 255, 255))
        title_rect = title.get_rect(center=(self.screen_width // 2, 200))
        screen.blit(title, title_rect)

        # Render menu options
        options = [
            "ENTER / ESC: Resume",
            "R: Restart Level",
            "M: Main Menu"
        ]

        y_start = 300
        for i, text in enumerate(options):
            option = self.option_font.render(text, True, (200, 200, 200))
            option_rect = option.get_rect(center=(self.screen_width // 2, y_start + i * 50))
            screen.blit(option, option_rect)


class GameOverScreen:
    """
    Game over screen that appears when the player runs out of lives.
    Displays game over message, statistics, and menu options.
    """

    def __init__(self, screen_width, screen_height):
        """
        Initialize game over screen.

        Args:
            screen_width (int): Width of the game screen
            screen_height (int): Height of the game screen
        """
        self.screen_width = screen_width
        self.screen_height = screen_height

        # Initialize fonts
        self.title_font = pygame.font.Font(None, 72)
        self.option_font = pygame.font.Font(None, 36)
        self.info_font = pygame.font.Font(None, 28)

    def render(self, screen, level_reached):
        """
        Render game over screen with statistics and options.

        Args:
            screen (pygame.Surface): The game screen to render on
            level_reached (int): The level number the player reached before game over
        """
        # Fill background with dark color
        screen.fill((20, 20, 20))

        # Render "GAME OVER" title in red
        title = self.title_font.render("GAME OVER", True, (255, 50, 50))
        title_rect = title.get_rect(center=(self.screen_width // 2, 150))
        screen.blit(title, title_rect)

        # Render level reached information
        info_text = f"Reached Level {level_reached}"
        info = self.info_font.render(info_text, True, (200, 200, 200))
        info_rect = info.get_rect(center=(self.screen_width // 2, 250))
        screen.blit(info, info_rect)

        # Render menu options
        options = [
            "R: Retry from Level 1",
            "M / ESC: Main Menu"
        ]

        y_start = 350
        for i, text in enumerate(options):
            option = self.option_font.render(text, True, (200, 200, 200))
            option_rect = option.get_rect(center=(self.screen_width // 2, y_start + i * 50))
            screen.blit(option, option_rect)
