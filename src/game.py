"""
SANCHO BROS - Main Game Class
Manages the game loop, state, and core systems.
"""

import pygame
from src.constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    FPS
)
from src.entities import Player
from src.camera import Camera
from src.level import LevelLoader, Level


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

        # Initialize camera with viewport dimensions
        self.camera = Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

        # Level management
        self.level_loader = LevelLoader()
        self.current_level_number = 1
        self.current_level = None
        self.load_level(1)

        # Initialize player at level spawn position
        spawn = self.current_level.get_spawn_position()
        self.player = Player(spawn[0], spawn[1])

    def load_level(self, level_num):
        """
        Load a level by number.

        Args:
            level_num (int): Level number (1-5)
        """
        level_data = self.level_loader.load_level_by_number(level_num)
        if level_data:
            self.current_level = Level(level_data)
            self.current_level_number = level_num
            print(f"Loaded Level {level_num}")
        else:
            print(f"Failed to load Level {level_num}")
            self.running = False

    def load_next_level(self):
        """Load the next level and reset player."""
        next_level = self.current_level_number + 1
        if next_level <= 5:
            self.load_level(next_level)
            self.respawn_player()
            print(f"Level {self.current_level_number - 1} Complete! Moving to Level {self.current_level_number}")
        else:
            print("Game Complete! You beat all 5 levels!")
            self.running = False

    def respawn_player(self):
        """Respawn player at current level's spawn point."""
        spawn = self.current_level.get_spawn_position()
        self.player.position.x = spawn[0]
        self.player.position.y = spawn[1]
        self.player.velocity.x = 0
        self.player.velocity.y = 0
        self.player.is_grounded = False
        print(f"Player respawned at ({spawn[0]}, {spawn[1]})")

    def load_specific_level(self, level_num):
        """
        Load a specific level (for testing purposes).

        Args:
            level_num (int): Level number (1-5)
        """
        if 1 <= level_num <= 5:
            self.load_level(level_num)
            spawn = self.current_level.get_spawn_position()
            self.player.position.x = spawn[0]
            self.player.position.y = spawn[1]
            self.player.velocity = pygame.Vector2(0, 0)
            self.player.is_grounded = False
            self.camera.offset.x = 0
            self.camera.offset.y = 0
            print(f"[TEST] Jumped to Level {level_num}")
        else:
            print(f"[TEST] Invalid level number: {level_num}. Must be 1-5.")

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

                # Testing shortcuts: Jump to specific levels (1-5 keys)
                elif event.key == pygame.K_1:
                    self.load_specific_level(1)
                elif event.key == pygame.K_2:
                    self.load_specific_level(2)
                elif event.key == pygame.K_3:
                    self.load_specific_level(3)
                elif event.key == pygame.K_4:
                    self.load_specific_level(4)
                elif event.key == pygame.K_5:
                    self.load_specific_level(5)
                # R key to restart current level
                elif event.key == pygame.K_r:
                    self.load_specific_level(self.current_level_number)

    def update(self, dt):
        """
        Update game state.

        Args:
            dt (float): Delta time in seconds since last frame
        """
        # Update level
        self.current_level.update(dt, self.player)

        # Update player with level platforms
        platforms = self.current_level.get_platforms()
        self.player.update(dt, platforms)

        # Update camera to follow player with level width as boundary
        self.camera.update(self.player.position, self.current_level.width)

        # Check enemy collisions
        from src.physics.collision import check_enemy_collision, check_stomp
        colliding_enemy = check_enemy_collision(self.player, self.current_level.enemies)

        if colliding_enemy:
            # Check stomp first (priority over damage)
            if check_stomp(self.player, colliding_enemy):
                # Stomp! Defeat the enemy
                colliding_enemy.die()
                self.player.velocity.y = -8  # Bounce player upward
                print("Enemy stomped!")
            else:
                # Player takes damage from side/bottom collision
                damage_applied = self.player.take_damage()

                if damage_applied:  # Only respawn if damage was actually applied (not invincible)
                    if self.player.lives > 0:
                        # Respawn player at spawn point
                        self.respawn_player()
                    else:
                        # Game over - no lives remaining
                        print("Game Over! No lives remaining.")
                        self.running = False

        # Check win condition
        if self.current_level.check_goal(self.player):
            self.load_next_level()

        # Check lose condition
        if self.current_level.check_pits(self.player):
            self.player.take_damage()
            print(f"Player fell in pit! Lives remaining: {self.player.lives}")

            if self.player.lives > 0:
                # Respawn player
                self.respawn_player()
            else:
                print("Game Over! No lives remaining.")
                self.running = False

    def render(self):
        """
        Render the game to the screen.
        """
        # Render level (includes background color, platforms, goal)
        self.current_level.render(self.screen, self.camera)

        # Render player on top of level
        self.player.render(self.screen, self.camera)

        # Update the display
        pygame.display.flip()
