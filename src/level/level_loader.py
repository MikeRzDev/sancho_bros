"""
Level Loader Module

Loads and validates JSON level files for Sancho Bros.
"""

import json
import os


class LevelLoader:
    """
    Handles loading and validation of level JSON files.

    The LevelLoader reads level data from JSON files in the levels/ directory,
    validates the data structure, and returns parsed level dictionaries ready
    for use by the game.
    """

    def __init__(self):
        """Initialize the level loader with the levels directory path."""
        self.levels_dir = "levels"

    def load_level(self, filename):
        """
        Load and parse a level JSON file.

        Args:
            filename (str): Path to the level JSON file (relative or absolute)

        Returns:
            dict: Parsed level data if valid, None if error occurred

        Raises:
            ValueError: If level data fails validation
        """
        try:
            # Read and parse JSON file
            with open(filename, 'r') as f:
                level_data = json.load(f)

            # Validate the level data structure
            if self.validate_level(level_data):
                print(f"Successfully loaded level: {filename}")
                return level_data
            else:
                raise ValueError(f"Invalid level data in {filename}")

        except FileNotFoundError:
            print(f"Error: Level file not found: {filename}")
            print(f"  Make sure the file exists in the correct location.")
            return None

        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON in {filename}")
            print(f"  JSON parse error: {e}")
            return None

        except ValueError as e:
            print(f"Error: {e}")
            return None

    def load_level_by_number(self, level_num):
        """
        Load a level by its number (1-5).

        Args:
            level_num (int): Level number (1 through 5)

        Returns:
            dict: Parsed level data if valid, None if error occurred
        """
        filename = os.path.join(self.levels_dir, f"level_{level_num}.json")
        return self.load_level(filename)

    def validate_level(self, data):
        """
        Validate level data structure and contents.

        Checks for:
        - Required top-level fields
        - Correct data types
        - Required nested properties
        - Coordinate bounds validation

        Args:
            data (dict): Level data dictionary to validate

        Returns:
            bool: True if valid, False if validation fails
        """
        # Check required top-level fields
        required_fields = [
            'level_number', 'width', 'height', 'background_color',
            'player_spawn', 'platforms', 'enemies', 'powerups',
            'pits', 'goal'
        ]

        for field in required_fields:
            if field not in data:
                print(f"Error: Missing required field: {field}")
                return False

        # Validate numeric fields
        if not isinstance(data['level_number'], int):
            print("Error: level_number must be an integer")
            return False

        if not isinstance(data['width'], int) or data['width'] <= 0:
            print("Error: width must be a positive integer")
            return False

        if not isinstance(data['height'], int) or data['height'] <= 0:
            print("Error: height must be a positive integer")
            return False

        # Validate background_color
        if not isinstance(data['background_color'], list) or len(data['background_color']) != 3:
            print("Error: background_color must be an array of 3 RGB values")
            return False

        for i, color in enumerate(data['background_color']):
            if not isinstance(color, int) or color < 0 or color > 255:
                print(f"Error: background_color[{i}] must be an integer between 0-255")
                return False

        # Validate player_spawn
        if not isinstance(data['player_spawn'], dict):
            print("Error: player_spawn must be an object")
            return False

        if 'x' not in data['player_spawn'] or 'y' not in data['player_spawn']:
            print("Error: player_spawn missing x or y coordinate")
            return False

        if not isinstance(data['player_spawn']['x'], (int, float)) or \
           not isinstance(data['player_spawn']['y'], (int, float)):
            print("Error: player_spawn coordinates must be numeric")
            return False

        # Check player spawn is within level bounds
        if not (0 <= data['player_spawn']['x'] <= data['width']) or \
           not (0 <= data['player_spawn']['y'] <= data['height']):
            print(f"Error: player_spawn coordinates out of bounds (0-{data['width']}, 0-{data['height']})")
            return False

        # Validate goal
        if not isinstance(data['goal'], dict):
            print("Error: goal must be an object")
            return False

        if 'x' not in data['goal'] or 'y' not in data['goal']:
            print("Error: goal missing x or y coordinate")
            return False

        if not isinstance(data['goal']['x'], (int, float)) or \
           not isinstance(data['goal']['y'], (int, float)):
            print("Error: goal coordinates must be numeric")
            return False

        # Check goal is within level bounds
        if not (0 <= data['goal']['x'] <= data['width']) or \
           not (0 <= data['goal']['y'] <= data['height']):
            print(f"Error: goal coordinates out of bounds (0-{data['width']}, 0-{data['height']})")
            return False

        # Validate arrays
        if not isinstance(data['platforms'], list):
            print("Error: platforms must be an array")
            return False

        if not isinstance(data['enemies'], list):
            print("Error: enemies must be an array")
            return False

        if not isinstance(data['powerups'], list):
            print("Error: powerups must be an array")
            return False

        if not isinstance(data['pits'], list):
            print("Error: pits must be an array")
            return False

        # Validate platform objects
        for i, platform in enumerate(data['platforms']):
            if not isinstance(platform, dict):
                print(f"Error: platforms[{i}] must be an object")
                return False

            required_platform_fields = ['type', 'x', 'y', 'width', 'height']
            for field in required_platform_fields:
                if field not in platform:
                    print(f"Error: platforms[{i}] missing required field: {field}")
                    return False

            # Validate platform coordinates are within bounds
            if not (0 <= platform['x'] <= data['width']) or \
               not (0 <= platform['y'] <= data['height']):
                print(f"Error: platforms[{i}] coordinates out of bounds")
                return False

        # Validate enemy objects
        for i, enemy in enumerate(data['enemies']):
            if not isinstance(enemy, dict):
                print(f"Error: enemies[{i}] must be an object")
                return False

            required_enemy_fields = ['type', 'x', 'y', 'patrol_left', 'patrol_right']
            for field in required_enemy_fields:
                if field not in enemy:
                    print(f"Error: enemies[{i}] missing required field: {field}")
                    return False

            # Validate enemy coordinates are within bounds
            if not (0 <= enemy['x'] <= data['width']) or \
               not (0 <= enemy['y'] <= data['height']):
                print(f"Error: enemies[{i}] coordinates out of bounds")
                return False

        # Validate powerup objects
        for i, powerup in enumerate(data['powerups']):
            if not isinstance(powerup, dict):
                print(f"Error: powerups[{i}] must be an object")
                return False

            required_powerup_fields = ['type', 'x', 'y']
            for field in required_powerup_fields:
                if field not in powerup:
                    print(f"Error: powerups[{i}] missing required field: {field}")
                    return False

            # Validate powerup coordinates are within bounds
            if not (0 <= powerup['x'] <= data['width']) or \
               not (0 <= powerup['y'] <= data['height']):
                print(f"Error: powerups[{i}] coordinates out of bounds")
                return False

        # Validate pit objects
        for i, pit in enumerate(data['pits']):
            if not isinstance(pit, dict):
                print(f"Error: pits[{i}] must be an object")
                return False

            required_pit_fields = ['x', 'width']
            for field in required_pit_fields:
                if field not in pit:
                    print(f"Error: pits[{i}] missing required field: {field}")
                    return False

            # Validate pit is within bounds
            if not (0 <= pit['x'] <= data['width']):
                print(f"Error: pits[{i}] x coordinate out of bounds")
                return False

            if pit['width'] <= 0:
                print(f"Error: pits[{i}] width must be positive")
                return False

        # All validations passed
        return True
