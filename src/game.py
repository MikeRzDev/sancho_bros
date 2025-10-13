"""
SANCHO BROS - Main Game Class
Manages the game loop, state, and core systems.
"""

import pygame
from src.constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    FPS,
    COLOR_BACKGROUND
)


class Game:
    """
    Main game class that handles initialization, game loop, and high-level game state.
    """

    def __init__(self):
        """Initialize Pygame, create the game window, and set up game state."""
        # Initialize Pygame
        pygame.init()

        # Create the game window
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Sancho Bros")

        # Initialize clock for FPS control
        self.clock = pygame.time.Clock()

        # Game state
        self.running = True

    def run(self):
        """
        Main game loop. Runs at 60 FPS and handles events, updates, and rendering.
        """
        while self.running:
            # Calculate delta time (in seconds) for frame-independent movement
            dt = self.clock.tick(FPS) / 1000.0

            # Process input events
            self.handle_events()

            # Update game state
            self.update(dt)

            # Render the game
            self.render()

        # Clean up when game loop exits
        pygame.quit()

    def handle_events(self):
        """
        Process input events (keyboard, mouse, window events).
        """
        for event in pygame.event.get():
            # Handle window close button
            if event.type == pygame.QUIT:
                self.running = False

            # Handle keyboard events
            elif event.type == pygame.KEYDOWN:
                # ESC key exits the game
                if event.key == pygame.K_ESCAPE:
                    self.running = False

    def update(self, dt):
        """
        Update game state.

        Args:
            dt (float): Delta time in seconds since last frame
        """
        # Placeholder - game logic will be added in future user stories
        pass

    def render(self):
        """
        Render the game to the screen.
        """
        # Clear the screen with background color
        self.screen.fill(COLOR_BACKGROUND)

        # Placeholder - entities and UI will be rendered in future user stories

        # Update the display
        pygame.display.flip()
