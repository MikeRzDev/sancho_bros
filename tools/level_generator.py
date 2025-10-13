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
        # Note: Pits must be created first, as platforms need pit locations
        self.create_pits(level_data, config)
        self.place_platforms(level_data, config)
        self.place_enemies(level_data, config)
        self.place_powerups(level_data, config)

        return level_data

    def place_platforms(self, level_data, difficulty):
        """
        Create platform layout for the level.

        Args:
            level_data: Level data dictionary to modify
            difficulty: Difficulty configuration for this level
        """
        platforms = []
        level_width = level_data['width']
        level_num = level_data['level_number']

        # ===== GROUND PLATFORM GENERATION =====
        # Create ground segments with pit gaps
        current_x = 0
        pits = sorted(level_data['pits'], key=lambda p: p['x'])  # Sort pits by x position

        for pit in pits:
            # Create ground segment before this pit
            ground_width = pit['x'] - current_x
            if ground_width > 0:
                platforms.append({
                    'type': 'solid',
                    'x': current_x,
                    'y': 550,
                    'width': ground_width,
                    'height': 50
                })
            current_x = pit['x'] + pit['width']

        # Final ground segment to end of level
        final_width = level_width - current_x
        if final_width > 0:
            platforms.append({
                'type': 'solid',
                'x': current_x,
                'y': 550,
                'width': final_width,
                'height': 50
            })

        # ===== FLOATING PLATFORM GENERATION =====
        # Difficulty-based platform density
        # Level 1: Few platforms, wide and easy
        # Level 5: Many platforms, challenging layout
        platform_configs = {
            1: {'count': 5, 'min_width': 120, 'max_width': 150},   # Easy: wide platforms
            2: {'count': 8, 'min_width': 100, 'max_width': 140},
            3: {'count': 12, 'min_width': 80, 'max_width': 130},
            4: {'count': 15, 'min_width': 70, 'max_width': 120},
            5: {'count': 18, 'min_width': 60, 'max_width': 110}    # Hard: narrow platforms
        }

        config = platform_configs[level_num]

        # Generate floating platforms across the level
        # Ensure platforms are placed to allow progression
        safe_start = 300  # After spawn area
        safe_end = level_width - 400  # Before goal area
        placeable_width = safe_end - safe_start

        # Divide into segments to ensure even distribution
        segment_count = config['count']
        segment_width = placeable_width // segment_count if segment_count > 0 else placeable_width

        for i in range(config['count']):
            segment_start = safe_start + (i * segment_width)
            segment_end = segment_start + segment_width

            # Random platform width
            plat_width = random.randint(config['min_width'], config['max_width'])

            # Random x position within segment (with smaller buffer to fit more platforms)
            max_x = segment_end - plat_width - 20  # Small spacing buffer
            if max_x >= segment_start:
                plat_x = random.randint(segment_start, max(segment_start, max_x))

                # Random height: higher platforms for harder levels
                # Level 1: 350-450 (easier to reach)
                # Level 5: 200-500 (full range)
                if level_num == 1:
                    min_height = 350
                    max_height = 450
                elif level_num <= 3:
                    min_height = 300
                    max_height = 480
                else:
                    min_height = 200
                    max_height = 500

                plat_y = random.randint(min_height, max_height)

                # Check if this platform overlaps with any pit
                # If so, it might be crossing a pit gap - that's okay for floating platforms
                platforms.append({
                    'type': 'floating',
                    'x': plat_x,
                    'y': plat_y,
                    'width': plat_width,
                    'height': 20
                })

        # ===== ENSURE PROGRESSION PATH =====
        # Add platforms near spawn and goal to ensure they're reachable
        # Platform near spawn
        platforms.append({
            'type': 'floating',
            'x': 250,
            'y': 400,
            'width': 120,
            'height': 20
        })

        # Platform near goal
        platforms.append({
            'type': 'floating',
            'x': level_width - 400,
            'y': 450,
            'width': 120,
            'height': 20
        })

        # Sort platforms by x position for easier debugging
        platforms.sort(key=lambda p: p['x'])

        level_data['platforms'] = platforms

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
        pits = []
        level_width = level_data['width']
        pit_config = difficulty['pits']

        # Determine number of pits
        if isinstance(pit_config, tuple):
            num_pits = random.randint(pit_config[0], pit_config[1])
        else:
            num_pits = pit_config

        # Safe zones: Don't place pits near spawn (first 500px) or goal (last 500px)
        safe_start = 500
        safe_end = level_width - 500
        placeable_width = safe_end - safe_start

        if placeable_width > 0 and num_pits > 0:
            # Divide level into segments for pit placement
            segment_width = placeable_width // num_pits

            for i in range(num_pits):
                # Random position within this segment
                segment_start = safe_start + (i * segment_width)
                segment_end = segment_start + segment_width

                # Pit width varies: 80-150 pixels (smaller for level 1, larger for later levels)
                min_width = 80
                max_width = 100 + (level_data['level_number'] * 10)  # Scales with difficulty
                pit_width = random.randint(min_width, min(max_width, 150))

                # Random x position within segment, ensuring pit fits
                max_x = segment_end - pit_width
                if max_x > segment_start:
                    pit_x = random.randint(segment_start, max_x)

                    pits.append({
                        'x': pit_x,
                        'width': pit_width
                    })

        level_data['pits'] = pits

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
