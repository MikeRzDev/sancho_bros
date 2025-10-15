# US009: Generate Complete Level JSON Files

**As a** developer
**I want** to generate all 5 level JSON files with complete data
**So that** the game can load and play these levels

## Priority
Critical

## Story Points
3

## Acceptance Criteria

1. **Complete Level Generation**
   - [x] All 5 level files are generated:
     - `levels/level_1.json`
     - `levels/level_2.json`
     - `levels/level_3.json`
     - `levels/level_4.json`
     - `levels/level_5.json`

2. **Level Metadata**
   - [x] Each level has correct `level_number` (1-5)
   - [x] Level dimensions:
     - Level 1: width=2000, height=600
     - Level 2: width=2500, height=600
     - Level 3: width=3000, height=600
     - Level 4: width=3500, height=600
     - Level 5: width=4000, height=600
   - [x] Background color is set (RGB: [135, 206, 235] - sky blue)

3. **Player Spawn and Goal**
   - [x] `player_spawn` is set to `{x: 100, y: 400}` for all levels
   - [x] `goal` is placed near the end of each level:
     - x: level_width - 200
     - y: 500 (on ground or platform)

4. **Complete Level Data**
   - [x] Each JSON file includes all required sections:
     - level_number
     - width, height
     - background_color
     - player_spawn
     - platforms (from US006)
     - enemies (from US007)
     - powerups (from US008)
     - pits (from US008)
     - goal

5. **JSON Validity**
   - [x] All JSON files are valid and parseable
   - [x] Proper formatting with indentation
   - [x] No syntax errors
   - [x] Can be loaded with `json.load()`

6. **Generator Execution**
   - [x] Running `python tools/level_generator.py` creates all files
   - [x] Script completes without errors
   - [x] Success message displayed for each level
   - [x] Files are written to `levels/` directory

7. **Validation Tests**
   - [x] Each level JSON matches the schema from game_implementation.md Section 5.1
   - [x] All coordinates are within level bounds
   - [x] All levels are theoretically completable (path from spawn to goal)

## Technical Notes

```python
def generate_level(self, level_num):
    config = self.level_configs[level_num]

    level_data = {
        'level_number': level_num,
        'width': config['length'],
        'height': 600,
        'background_color': [135, 206, 235],
        'player_spawn': {'x': 100, 'y': 400},
        'platforms': [],
        'enemies': [],
        'powerups': [],
        'pits': [],
        'goal': {'x': config['length'] - 200, 'y': 500}
    }

    # Generate pits first (affects platforms)
    level_data['pits'] = self.create_pits(level_data, level_num)

    # Generate platforms (considers pits)
    level_data['platforms'] = self.place_platforms(level_data, level_num)

    # Place enemies on platforms
    level_data['enemies'] = self.place_enemies(level_data, level_num)

    # Place power-ups
    level_data['powerups'] = self.place_powerups(level_data, level_num)

    return level_data

def save_to_file(self, level_data, filename):
    import json
    with open(filename, 'w') as f:
        json.dump(level_data, f, indent=2)
    print(f"Generated: {filename}")

def generate_all_levels(self):
    for i in range(1, 6):
        level_data = self.generate_level(i)
        self.save_to_file(level_data, f"levels/level_{i}.json")
    print("All levels generated successfully!")

if __name__ == "__main__":
    generator = LevelGenerator()
    generator.generate_all_levels()
```

## Dependencies
- US005: Level generator structure
- US006: Platform generation logic
- US007: Enemy placement logic
- US008: Power-up and pit placement logic
