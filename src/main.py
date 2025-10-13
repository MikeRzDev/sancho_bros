"""
SANCHO BROS - Main Entry Point
Starts the game by initializing and running the Game instance.
"""

from src.game import Game


def main():
    """Initialize and run the Sancho Bros game."""
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
