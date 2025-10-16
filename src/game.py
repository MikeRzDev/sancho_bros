"""
SANCHO BROS - Main Game Class
Manages the game loop, state, and core systems.
"""

import pygame
from src.constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    FPS,
    GameState
)
from src.entities import Player
from src.camera import Camera
from src.level import LevelLoader, Level
from src.ui import MainMenu
from src.ui.hud import HUD


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
        self.state = GameState.MENU  # Start in menu state

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

        # Projectile management
        self.lasers = []  # List of active laser projectiles

        # UI components
        self.main_menu = MainMenu(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.hud = HUD()

    def change_state(self, new_state):
        """
        Change game state with logging.

        Args:
            new_state (str): The new game state to transition to
        """
        print(f"[STATE] {self.state} -> {new_state}")
        self.state = new_state

        # Handle state-specific setup
        if new_state == GameState.LEVEL_COMPLETE:
            # Could add a timer here for level transition delay
            pass

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
        State-aware event handling.
        """
        for event in pygame.event.get():
            # Handle window close button
            if event.type == pygame.QUIT:
                self.running = False

            # Handle keyboard events
            elif event.type == pygame.KEYDOWN:
                # Pause toggle (ESC or P) - only in PLAYING or PAUSED states
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_p:
                    if self.state == GameState.PLAYING:
                        self.change_state(GameState.PAUSED)
                    elif self.state == GameState.PAUSED:
                        self.change_state(GameState.PLAYING)

                # State-specific input handling
                if self.state == GameState.MENU:
                    # ENTER key starts the game
                    if event.key == pygame.K_RETURN:
                        self.change_state(GameState.PLAYING)
                    # Q or ESC key quits the game
                    elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                        self.running = False

                elif self.state == GameState.PLAYING:
                    # X or Ctrl key: Shoot laser (when powered up)
                    if event.key == pygame.K_x or event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL:
                        laser = self.player.shoot()
                        if laser:
                            self.lasers.append(laser)

                    # Testing shortcuts: Jump to specific levels (1-5 keys)
                    if event.key == pygame.K_1:
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
                    if event.key == pygame.K_r:
                        self.load_specific_level(self.current_level_number)

                    # DEBUG COMMANDS
                    # K key: Kill all enemies
                    if event.key == pygame.K_k:
                        for enemy in self.current_level.enemies:
                            enemy.die()
                        print("[DEBUG] All enemies defeated")

                    # L key: Reset lives to 3
                    if event.key == pygame.K_l:
                        self.player.lives = 3
                        print(f"[DEBUG] Lives reset to 3")

                    # I key: Toggle invincibility
                    if event.key == pygame.K_i:
                        self.player.is_invincible = not self.player.is_invincible
                        print(f"[DEBUG] Invincibility: {self.player.is_invincible}")

                    # T key: Add time to power-up timer
                    if event.key == pygame.K_t:
                        if self.player.has_powerup:
                            self.player.powerup_timer = 30.0
                            print("[DEBUG] Power-up timer extended to 30s")
                        else:
                            print("[DEBUG] No active power-up to extend")

                elif self.state == GameState.GAME_OVER:
                    # R key restarts the game from level 1
                    if event.key == pygame.K_r:
                        self.restart_game()
                    # M key returns to menu
                    elif event.key == pygame.K_m:
                        self.change_state(GameState.MENU)

    def update(self, dt):
        """
        Update game state based on current game state.

        Args:
            dt (float): Delta time in seconds since last frame
        """
        if self.state == GameState.PLAYING:
            # Normal gameplay updates
            # Update level
            self.current_level.update(dt, self.player)

            # Update player with level platforms
            platforms = self.current_level.get_platforms()
            self.player.update(dt, platforms)

            # Update camera to follow player with level width as boundary
            self.camera.update(self.player.position, self.current_level.width)

            # Check power-up collection
            for powerup in self.current_level.powerups:
                if powerup.check_collection(self.player):
                    powerup.collect()
                    self.player.collect_powerup()

            # Check enemy collisions
            from src.physics.collision import check_enemy_collision, check_stomp
            colliding_enemy = check_enemy_collision(self.player, self.current_level.enemies)

            if colliding_enemy:
                # Check stomp first (priority over damage)
                if check_stomp(self.player, colliding_enemy):
                    # Stomp! Defeat the enemy
                    colliding_enemy.die()
                    self.player.velocity.y = -8  # Bounce player upward
                    # DEBUG logging for stomp
                    print(f"[STOMP] Player pos: ({self.player.position.x:.1f}, {self.player.position.y:.1f}), "
                          f"Enemy pos: ({colliding_enemy.position.x:.1f}, {colliding_enemy.position.y:.1f})")
                else:
                    # Player takes damage from side/bottom collision
                    damage_applied = self.player.take_damage()

                    if damage_applied:  # Only respawn if damage was actually applied (not invincible)
                        # DEBUG logging for damage
                        print(f"[DAMAGE] Player pos: ({self.player.position.x:.1f}, {self.player.position.y:.1f}), "
                              f"Enemy pos: ({colliding_enemy.position.x:.1f}, {colliding_enemy.position.y:.1f}), "
                              f"Lives: {self.player.lives}")

                        if self.player.lives > 0:
                            # Respawn player at spawn point
                            self.respawn_player()
                        else:
                            # Game over - no lives remaining
                            print("Game Over! No lives remaining.")
                            self.change_state(GameState.GAME_OVER)

            # Check win condition
            if self.current_level.check_goal(self.player):
                self.change_state(GameState.LEVEL_COMPLETE)

            # Check lose condition
            if self.current_level.check_pits(self.player):
                self.player.take_damage()
                print(f"Player fell in pit! Lives remaining: {self.player.lives}")

                if self.player.lives > 0:
                    # Respawn player
                    self.respawn_player()
                else:
                    print("Game Over! No lives remaining.")
                    self.change_state(GameState.GAME_OVER)

            # Update lasers
            for laser in self.lasers[:]:  # Copy list to allow removal during iteration
                laser.update(dt, platforms, self.current_level.enemies)
                if not laser.is_active:
                    self.lasers.remove(laser)

        elif self.state == GameState.LEVEL_COMPLETE:
            # Handle level transition
            self.load_next_level()
            if self.running:  # If game is still running (not completed all levels)
                self.change_state(GameState.PLAYING)

        elif self.state == GameState.PAUSED:
            # Don't update game entities when paused
            pass

        elif self.state == GameState.MENU:
            # Update menu animations
            self.main_menu.update(dt)

        elif self.state == GameState.GAME_OVER:
            # Game over state - no game updates needed
            pass

    def render(self):
        """
        Render the game to the screen based on current state.
        """
        if self.state == GameState.MENU:
            # Render main menu
            self.render_main_menu()

        elif self.state == GameState.PLAYING:
            # Render game world
            self.current_level.render(self.screen, self.camera)
            self.player.render(self.screen, self.camera)

            # Render lasers
            for laser in self.lasers:
                laser.render(self.screen, self.camera)

            # Render HUD on top of game world
            self.hud.render(self.screen, self.player, self.current_level)

        elif self.state == GameState.PAUSED:
            # Render game world (frozen)
            self.current_level.render(self.screen, self.camera)
            self.player.render(self.screen, self.camera)

            # Render lasers
            for laser in self.lasers:
                laser.render(self.screen, self.camera)

            # Render HUD on top of game world
            self.hud.render(self.screen, self.player, self.current_level)

            # Render pause overlay on top
            self.render_pause_overlay()

        elif self.state == GameState.GAME_OVER:
            # Render game over screen
            self.render_game_over()

        elif self.state == GameState.LEVEL_COMPLETE:
            # Render level complete message
            self.render_level_complete()

        # Update the display
        pygame.display.flip()

    def render_main_menu(self):
        """Render the main menu screen."""
        self.main_menu.render(self.screen)

    def render_pause_overlay(self):
        """Render pause overlay on top of the frozen game."""
        from src.constants import COLOR_WHITE

        # Semi-transparent overlay
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(128)
        overlay.fill((0, 0, 0))
        self.screen.blit(overlay, (0, 0))

        # Pause text
        font = pygame.font.Font(None, 72)
        pause_text = font.render("PAUSED", True, COLOR_WHITE)
        pause_rect = pause_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        self.screen.blit(pause_text, pause_rect)

        # Instructions
        small_font = pygame.font.Font(None, 36)
        resume_text = small_font.render("Press ESC or P to Resume", True, COLOR_WHITE)
        resume_rect = resume_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
        self.screen.blit(resume_text, resume_rect)

    def render_game_over(self):
        """Render game over screen."""
        from src.constants import COLOR_BLACK, COLOR_WHITE, COLOR_RED

        # Clear screen
        self.screen.fill(COLOR_BLACK)

        # Game Over title
        title_font = pygame.font.Font(None, 72)
        game_over_text = title_font.render("GAME OVER", True, COLOR_RED)
        game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, 200))
        self.screen.blit(game_over_text, game_over_rect)

        # Instructions
        font = pygame.font.Font(None, 36)
        restart_text = font.render("Press R to Restart", True, COLOR_WHITE)
        restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, 350))
        self.screen.blit(restart_text, restart_rect)

        menu_text = font.render("Press M for Menu", True, COLOR_WHITE)
        menu_rect = menu_text.get_rect(center=(SCREEN_WIDTH // 2, 400))
        self.screen.blit(menu_text, menu_rect)

    def render_level_complete(self):
        """Render level complete screen."""
        from src.constants import COLOR_BACKGROUND, COLOR_WHITE, COLOR_GREEN

        # Clear screen
        self.screen.fill(COLOR_BACKGROUND)

        # Level complete message
        font = pygame.font.Font(None, 72)
        complete_text = font.render("LEVEL COMPLETE!", True, COLOR_GREEN)
        complete_rect = complete_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.screen.blit(complete_text, complete_rect)

    def restart_game(self):
        """Restart the game from Level 1."""
        print("[RESTART] Restarting game from Level 1")

        # Reset to level 1
        self.load_level(1)

        # Reset player
        spawn = self.current_level.get_spawn_position()
        self.player = Player(spawn[0], spawn[1])

        # Clear lasers
        self.lasers = []

        # Change to playing state
        self.change_state(GameState.PLAYING)
