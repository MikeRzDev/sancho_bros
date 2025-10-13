#!/usr/bin/env python3
"""
Level Generator Tool for Sancho Bros
Generates JSON level files with progressive difficulty.
"""

import json
import os
import random


class LevelGenerator:
    """Generates level JSON files for Sancho Bros game."""

    def __init__(self):
        """Initialize the level generator with difficulty configurations."""
        # Difficulty configuration for each level (1-5)
        self.level_configs = {
            1: {'length': 2000, 'enemies': (2, 3), 'powerups': 1, 'pits': (1, 2)},
            2: {'length': 2500, 'enemies': (4, 5), 'powerups': 1, 'pits': (2, 3)},
            3: {'length': 3000, 'enemies': (6, 7), 'powerups': 2, 'pits': (3, 4)},
            4: {'length': 3500, 'enemies': (8, 9), 'powerups': 2, 'pits': (4, 5)},
            5: {'length': 4000, 'enemies': (10, 12), 'powerups': (2, 3), 'pits': (5, 6)}
        }

        # Standard level height
        self.level_height = 600

        # Background colors (sky blue)
        self.background_color = [135, 206, 235]

    def generate_level(self, level_num):
        """
        Generate a complete level data structure.

        Args:
            level_num: Level number (1-5)

        Returns:
            dict: Complete level data with all required fields
        """
        if level_num not in self.level_configs:
            raise ValueError(f"Invalid level number: {level_num}. Must be 1-5.")

        config = self.level_configs[level_num]

        # Initialize level data structure
        level_data = {
            'level_number': level_num,
            'width': config['length'],
            'height': self.level_height,
            'background_color': self.background_color,
            'player_spawn': {'x': 100, 'y': 400},
            'platforms': [],
            'enemies': [],
            'powerups': [],
            'pits': [],
            'goal': {'x': config['length'] - 200, 'y': self.level_height - 100}
        }

        # Generate level elements based on difficulty
        self.place_platforms(level_data, config)
        self.place_enemies(level_data, config)
        self.place_powerups(level_data, config)
        self.create_pits(level_data, config)

        return level_data

    def place_platforms(self, level_data, difficulty):
        """
        Create platform layout for the level.

        Args:
            level_data: Level data dictionary to modify
            difficulty: Difficulty configuration for this level
        """
        # TODO: Implement platform generation logic in US006
        pass

    def place_enemies(self, level_data, difficulty):
        """
        Position enemies throughout the level.

        Args:
            level_data: Level data dictionary to modify
            difficulty: Difficulty configuration for this level
        """
        # TODO: Implement enemy placement logic in US007
        pass

    def place_powerups(self, level_data, difficulty):
        """
        Position power-ups throughout the level.

        Args:
            level_data: Level data dictionary to modify
            difficulty: Difficulty configuration for this level
        """
        # TODO: Implement power-up placement logic in US008
        pass

    def create_pits(self, level_data, difficulty):
        """
        Generate pit hazards in the level.

        Args:
            level_data: Level data dictionary to modify
            difficulty: Difficulty configuration for this level
        """
        # TODO: Implement pit placement logic in US008
        pass

    def save_to_file(self, level_data, filename):
        """
        Write level data to JSON file.

        Args:
            level_data: Level data dictionary to save
            filename: Output filename (e.g., 'levels/level_1.json')
        """
        # Ensure the levels directory exists
        os.makedirs(os.path.dirname(filename), exist_ok=True)

        # Write JSON with proper formatting
        with open(filename, 'w') as f:
            json.dump(level_data, f, indent=2)

        print(f"Generated: {filename}")

    def generate_all_levels(self):
        """Generate all 5 level JSON files."""
        print("Sancho Bros Level Generator")
        print("=" * 40)

        for level_num in range(1, 6):
            level_data = self.generate_level(level_num)
            filename = f"levels/level_{level_num}.json"
            self.save_to_file(level_data, filename)

        print("=" * 40)
        print("All 5 levels generated successfully!")


def main():
    """Main entry point for the level generator tool."""
    generator = LevelGenerator()
    generator.generate_all_levels()


if __name__ == "__main__":
    main()
