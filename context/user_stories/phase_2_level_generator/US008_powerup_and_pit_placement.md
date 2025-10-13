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
   - [ ] Level 1: 1 Arepa Dorada
   - [ ] Level 2: 1 Arepa Dorada
   - [ ] Level 3: 2 Arepa Doradas
   - [ ] Level 4: 2 Arepa Doradas
   - [ ] Level 5: 2-3 Arepa Doradas
   - [ ] Count matches game_implementation.md Section 6.2

2. **Power-Up Positioning**
   - [ ] Power-ups placed above platforms (floating in air)
   - [ ] Height: 50-150 pixels above nearest platform
   - [ ] Positioned in reachable locations (require jumping)
   - [ ] Spread throughout level (not all in one area)
   - [ ] Some require defeating enemies or risky jumps to reach

3. **Power-Up JSON Format**
   - [ ] Each power-up has: `type`, `x`, `y`
   - [ ] Type is always "arepa_dorada"
   - [ ] Coordinates are within level bounds

### Pit Placement

4. **Pit Count Per Level**
   - [ ] Level 1: 1-2 pits
   - [ ] Level 2: 2-3 pits
   - [ ] Level 3: 3-4 pits
   - [ ] Level 4: 4-5 pits
   - [ ] Level 5: 5-6 pits
   - [ ] Count matches game_implementation.md Section 6.2

5. **Pit Positioning**
   - [ ] Pits are gaps in the ground floor
   - [ ] Pit widths: 100-200 pixels
   - [ ] Pits are jumpable OR have floating platforms to cross
   - [ ] Not placed in first 300 pixels (spawn area)
   - [ ] Not placed in last 200 pixels (goal area)

6. **Pit JSON Format**
   - [ ] Each pit has: `x`, `width`
   - [ ] Pits don't overlap
   - [ ] Pits array is properly formatted

### Overall

7. **Strategic Placement**
   - [ ] Some pits require power-up (laser) to safely cross
   - [ ] Power-ups placed near challenging sections
   - [ ] At least one power-up in first half of level
   - [ ] Risk/reward balance maintained

8. **Validation**
   - [ ] All power-ups are reachable
   - [ ] All pits are crossable
   - [ ] Level remains completable with placed hazards

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
