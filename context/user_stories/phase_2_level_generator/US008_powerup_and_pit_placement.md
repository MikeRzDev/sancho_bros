# US008: Implement Power-Up and Pit Placement

**As a** developer
**I want** to place power-ups and pits in generated levels
**So that** players have collectibles and hazards to navigate

## Priority
High

## Story Points
3

## Acceptance Criteria

### Power-Up Placement

1. **Power-Up Count Per Level**
   - [x] Level 1: 1 Arepa Dorada
   - [x] Level 2: 1 Arepa Dorada
   - [x] Level 3: 2 Arepa Doradas
   - [x] Level 4: 2 Arepa Doradas
   - [x] Level 5: 2-3 Arepa Doradas
   - [x] Count matches game_implementation.md Section 6.2

2. **Power-Up Positioning**
   - [x] Power-ups placed above platforms (floating in air)
   - [x] Height: 50-150 pixels above nearest platform
   - [x] Positioned in reachable locations (require jumping)
   - [x] Spread throughout level (not all in one area)
   - [x] Some require defeating enemies or risky jumps to reach

3. **Power-Up JSON Format**
   - [x] Each power-up has: `type`, `x`, `y`
   - [x] Type is always "arepa_dorada"
   - [x] Coordinates are within level bounds

### Pit Placement

4. **Pit Count Per Level**
   - [x] Level 1: 1-2 pits
   - [x] Level 2: 2-3 pits
   - [x] Level 3: 3-4 pits
   - [x] Level 4: 4-5 pits
   - [x] Level 5: 5-6 pits
   - [x] Count matches game_implementation.md Section 6.2

5. **Pit Positioning**
   - [x] Pits are gaps in the ground floor
   - [x] Pit widths: 100-200 pixels
   - [x] Pits are jumpable OR have floating platforms to cross
   - [x] Not placed in first 300 pixels (spawn area)
   - [x] Not placed in last 200 pixels (goal area)

6. **Pit JSON Format**
   - [x] Each pit has: `x`, `width`
   - [x] Pits don't overlap
   - [x] Pits array is properly formatted

### Overall

7. **Strategic Placement**
   - [x] Some pits require power-up (laser) to safely cross
   - [x] Power-ups placed near challenging sections
   - [x] At least one power-up in first half of level
   - [x] Risk/reward balance maintained

8. **Validation**
   - [x] All power-ups are reachable
   - [x] All pits are crossable
   - [x] Level remains completable with placed hazards

## Technical Notes

```python
def place_powerups(self, level_data, difficulty):
    powerups = []
    config = self.level_configs[level_data['level_number']]
    powerup_count = config['powerups']
    if isinstance(powerup_count, tuple):
        powerup_count = random.randint(*powerup_count)

    level_width = level_data['width']
    segment_width = level_width // (powerup_count + 1)

    for i in range(powerup_count):
        x = (i + 1) * segment_width + random.randint(-100, 100)
        y = random.randint(200, 400)

        powerups.append({
            'type': 'arepa_dorada',
            'x': x,
            'y': y
        })

    return powerups

def create_pits(self, level_data, difficulty):
    pits = []
    config = self.level_configs[level_data['level_number']]
    pit_count = random.randint(*config['pits'])

    level_width = level_data['width']
    safe_start = 300
    safe_end = level_width - 200

    for i in range(pit_count):
        pit_width = random.randint(100, 200)
        x = random.randint(safe_start, safe_end - pit_width)

        # Ensure not overlapping
        if not any(abs(p['x'] - x) < 300 for p in pits):
            pits.append({'x': x, 'width': pit_width})

    return sorted(pits, key=lambda p: p['x'])
```

## Dependencies
- US005: Level generator structure must exist
- US006: Platforms must be generated (for power-up placement)
