# US015: Create Level Loader and JSON Parser

**As a** developer
**I want** to create a level loader that parses JSON files
**So that** level data can be loaded into the game

## Priority
Critical

## Story Points
5

## Acceptance Criteria

1. **Level Loader Class Created**
   - [ ] `src/level/level_loader.py` exists
   - [ ] `LevelLoader` class is defined

2. **JSON Loading Method**
   - [ ] `load_level(filename)` method reads JSON file
   - [ ] Returns parsed level data as dictionary
   - [ ] Handles file not found errors gracefully
   - [ ] Handles JSON parse errors gracefully

3. **Level Validation**
   - [ ] `validate_level(data)` method checks required fields:
     - level_number
     - width, height
     - background_color
     - player_spawn (x, y)
     - platforms (array)
     - enemies (array)
     - powerups (array)
     - pits (array)
     - goal (x, y)
   - [ ] Returns True if valid, False otherwise
   - [ ] Logs descriptive error messages for missing fields

4. **Data Type Validation**
   - [ ] Numeric fields are numbers
   - [ ] Arrays are lists
   - [ ] Objects have required properties
   - [ ] Coordinates are within level bounds

5. **Error Handling**
   - [ ] FileNotFoundError: Clear error message
   - [ ] JSONDecodeError: Clear error message
   - [ ] Invalid data: Clear error message with field name
   - [ ] All errors logged to console

6. **Level Path Handling**
   - [ ] Accepts relative paths: `"levels/level_1.json"`
   - [ ] Accepts level number: `load_level_by_number(1)` → loads level_1.json
   - [ ] Works from project root directory

7. **Validation**
   - [ ] Can load all 5 generated level files
   - [ ] Returns correct data structure
   - [ ] Validates successfully for valid levels
   - [ ] Rejects invalid/corrupted level files

## Technical Notes

```python
# src/level/level_loader.py
import json
import os

class LevelLoader:
    def __init__(self):
        self.levels_dir = "levels"

    def load_level(self, filename):
        """Load and parse a level JSON file"""
        try:
            with open(filename, 'r') as f:
                level_data = json.load(f)

            if self.validate_level(level_data):
                return level_data
            else:
                raise ValueError(f"Invalid level data in {filename}")

        except FileNotFoundError:
            print(f"Error: Level file not found: {filename}")
            return None
        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON in {filename}: {e}")
            return None

    def load_level_by_number(self, level_num):
        """Load level by number (1-5)"""
        filename = os.path.join(self.levels_dir, f"level_{level_num}.json")
        return self.load_level(filename)

    def validate_level(self, data):
        """Validate level data structure"""
        required_fields = [
            'level_number', 'width', 'height', 'background_color',
            'player_spawn', 'platforms', 'enemies', 'powerups',
            'pits', 'goal'
        ]

        for field in required_fields:
            if field not in data:
                print(f"Error: Missing required field: {field}")
                return False

        # Validate player_spawn
        if 'x' not in data['player_spawn'] or 'y' not in data['player_spawn']:
            print("Error: player_spawn missing x or y")
            return False

        # Validate goal
        if 'x' not in data['goal'] or 'y' not in data['goal']:
            print("Error: goal missing x or y")
            return False

        # Validate arrays
        if not isinstance(data['platforms'], list):
            print("Error: platforms must be an array")
            return False

        return True
```

## Dependencies
- US009: Level JSON files must be generated
