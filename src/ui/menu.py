"""
SANCHO BROS - Main Menu UI
Displays the main menu screen with title, options, and controls.
"""

import pygame
import math
from src.constants import SCREEN_WIDTH, SCREEN_HEIGHT


class MainMenu:
    """Main menu screen with title, options, and controls display."""

    def __init__(self, screen_width, screen_height):
        """
        Initialize the main menu.

        Args:
            screen_width (int): Width of the screen
            screen_height (int): Height of the screen
        """
        self.screen_width = screen_width
        self.screen_height = screen_height

        # Fonts
        self.title_font = pygame.font.Font(None, 72)
        self.option_font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)

        # Animation timer for title pulse effect
        self.animation_timer = 0.0

    def update(self, dt):
        """
        Update menu animations.

        Args:
            dt (float): Delta time in seconds
        """
        self.animation_timer += dt

    def render(self, screen):
        """
        Render the main menu to the screen.

        Args:
            screen (pygame.Surface): The screen to render to
        """
        # Background - dark blue
        screen.fill((50, 50, 100))

        # Animated title with pulse effect
        scale = 1.0 + 0.05 * math.sin(self.animation_timer * 2)
        font_size = int(72 * scale)
        title_font = pygame.font.Font(None, font_size)
        title = title_font.render("SANCHO BROS", True, (255, 215, 0))  # Gold
        title_rect = title.get_rect(center=(self.screen_width // 2, 150))
        screen.blit(title, title_rect)

        # Start option
        start_text = self.option_font.render("Press ENTER to Start", True, (255, 255, 255))
        start_rect = start_text.get_rect(center=(self.screen_width // 2, 300))
        screen.blit(start_text, start_rect)

        # Quit option
        quit_text = self.option_font.render("Press Q or ESC to Quit", True, (200, 200, 200))
        quit_rect = quit_text.get_rect(center=(self.screen_width // 2, 350))
        screen.blit(quit_text, quit_rect)

        # Controls display
        y_pos = 450
        controls = [
            "CONTROLS:",
            "Arrow Keys / WASD: Move",
            "SPACE: Jump",
            "X / CTRL: Shoot (when powered)",
            "ESC: Pause"
        ]

        for i, text in enumerate(controls):
            control_text = self.small_font.render(text, True, (150, 150, 150))
            control_rect = control_text.get_rect(center=(self.screen_width // 2, y_pos + i * 25))
            screen.blit(control_text, control_rect)
