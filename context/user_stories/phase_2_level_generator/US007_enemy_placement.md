# US007: Implement Enemy Placement Logic

**As a** developer
**I want** to place enemies with patrol routes in generated levels
**So that** players face appropriate challenges

## Priority
High

## Story Points
3

## Acceptance Criteria

1. **Enemy Count Per Level**
   - [x] Level 1: 2-3 Polochos
   - [x] Level 2: 4-5 Polochos
   - [x] Level 3: 6-7 Polochos
   - [x] Level 4: 8-9 Polochos
   - [x] Level 5: 10-12 Polochos
   - [x] Count matches game_implementation.md Section 6.2

2. **Enemy Positioning**
   - [x] Enemies spawn on platforms (not in air or pits)
   - [x] Enemy y-position is platform.y - 40 (standing on platform)
   - [x] Enemies are spread throughout the level
   - [x] Not all enemies are on the ground floor

3. **Patrol Range Definition**
   - [x] Each enemy has `patrol_left` and `patrol_right` boundaries
   - [x] Patrol ranges are 100-300 pixels wide
   - [x] Patrol boundaries stay within platform boundaries
   - [x] Patrol ranges don't cross pit boundaries

4. **Strategic Placement**
   - [x] Some enemies guard power-ups
   - [x] Some enemies patrol narrow platforms
   - [x] Density increases near level goal
   - [x] First 200 pixels (spawn area) have no enemies

5. **JSON Output Format**
   - [x] Each enemy has: `type`, `x`, `y`, `patrol_left`, `patrol_right`
   - [x] Type is always "polocho"
   - [x] Enemies array is properly formatted

6. **Validation**
   - [x] All enemies spawn on valid platforms
   - [x] Patrol ranges don't cause enemies to fall off
   - [x] Enemy placement is deterministic (same seed = same placement)

## Technical Notes

```python
def place_enemies(self, level_data, difficulty):
    enemies = []
    config = self.level_configs[level_data['level_number']]
    enemy_count = random.randint(*config['enemies'])

    # Get all platforms suitable for enemy patrols
    valid_platforms = [p for p in level_data['platforms']
                      if p['width'] >= 100 and p['x'] > 200]

    for i in range(enemy_count):
        platform = random.choice(valid_platforms)

        # Position on platform
        patrol_width = min(200, platform['width'] - 20)
        patrol_start = platform['x'] + 10

        enemy = {
            'type': 'polocho',
            'x': patrol_start + patrol_width // 2,
            'y': platform['y'] - 40,
            'patrol_left': patrol_start,
            'patrol_right': patrol_start + patrol_width
        }
        enemies.append(enemy)

    return enemies
```

- Use random.seed() for deterministic generation (if desired)
- Ensure enemy size (40px) fits on platforms
- Avoid clustering too many enemies in one area

## Dependencies
- US005: Level generator structure must exist
- US006: Platforms must be generated first
