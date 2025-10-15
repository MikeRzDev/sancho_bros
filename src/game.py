"""
SANCHO BROS - Main Game Class
Manages the game loop, state, and core systems.
"""

import pygame
from src.constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    FPS,
    COLOR_BACKGROUND,
    COLOR_PLATFORM_SOLID
)
from src.entities import Player
from src.camera import Camera
from src.level.tile import Platform


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

        # Initialize game entities
        self.player = Player(100, 200)  # Spawn in air to test falling

        # Initialize camera with viewport dimensions
        self.camera = Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

        # Create extended test platforms for camera system validation
        # Level extends to 2000px to test scrolling
        self.platforms = [
            # Ground platforms (solid)
            Platform(0, 550, 500, 50, "solid"),        # Left ground
            Platform(600, 550, 400, 50, "solid"),      # Middle ground (gap at 500-600)
            Platform(1100, 550, 900, 50, "solid"),     # Right ground

            # Floating platforms
            Platform(300, 400, 200, 20, "floating"),   # Early jump
            Platform(600, 300, 150, 20, "floating"),   # Over gap
            Platform(900, 350, 180, 20, "floating"),   # Mid level
            Platform(1200, 250, 120, 20, "floating"),  # High platform
            Platform(1500, 400, 200, 20, "floating"),  # Late game
            Platform(1800, 300, 150, 20, "floating"),  # Near end
        ]

        # Calculate level width from platforms
        self.level_width = max(platform.rect.right for platform in self.platforms)

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
        # Update player with test platforms
        self.player.update(dt, self.platforms)

        # Update camera to follow player
        self.camera.update(self.player.position, self.level_width)

    def render(self):
        """
        Render the game to the screen.
        """
        # Clear the screen with background color
        self.screen.fill(COLOR_BACKGROUND)

        # Render test platforms
        for platform in self.platforms:
            platform.render(self.screen, self.camera)

        # Render game entities
        self.player.render(self.screen, self.camera)

        # Update the display
        pygame.display.flip()
