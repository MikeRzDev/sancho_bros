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


# Simple test platform class for US011 physics validation
class TestPlatform:
    """Temporary platform class for testing physics system."""
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = COLOR_PLATFORM_SOLID

    def render(self, screen, camera):
        screen_x = self.rect.x - camera.x
        screen_y = self.rect.y - camera.y
        pygame.draw.rect(screen, self.color, (screen_x, screen_y, self.rect.width, self.rect.height))


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

        # Initialize camera
        self.camera = Camera(0, 0)

        # Create test platforms for US011 physics validation
        self.platforms = [
            TestPlatform(0, 550, 800, 50),      # Ground platform
            TestPlatform(300, 400, 200, 20),    # Floating platform
            TestPlatform(600, 300, 150, 20)     # Higher floating platform
        ]

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
                # Space bar to jump (US011 physics validation)
                elif event.key == pygame.K_SPACE:
                    self.player.jump()

    def update(self, dt):
        """
        Update game state.

        Args:
            dt (float): Delta time in seconds since last frame
        """
        # Update player with test platforms
        self.player.update(dt, self.platforms)

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
