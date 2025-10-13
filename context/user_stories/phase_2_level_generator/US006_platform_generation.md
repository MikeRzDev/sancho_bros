# US006: Implement Platform Generation Logic

**As a** developer
**I want** to generate platform layouts for each level
**So that** players have ground to walk on and obstacles to jump across

## Priority
Critical

## Story Points
5

## Acceptance Criteria

1. **Ground Platform Generation**
   - [x] Each level has a continuous ground floor at y=550
   - [x] Ground extends from x=0 to appropriate positions
   - [x] Ground has gaps (pits) at designated locations
   - [x] Ground segments are type "solid"

2. **Floating Platform Generation**
   - [x] Floating platforms are type "floating"
   - [x] Platforms are placed at varying heights (y: 200-500)
   - [x] Platform spacing allows for reasonable jumps (considering JUMP_STRENGTH = -15)
   - [x] Platform density increases with level difficulty
   - [x] Platforms are 60-150 pixels wide, 20 pixels high

3. **Platform Placement Rules**
   - [x] Minimum platform spacing: 100 pixels horizontally
   - [x] Maximum jump gap: 250 pixels (must be reachable)
   - [x] Platforms don't overlap
   - [x] At least one platform every 400 pixels for progression

4. **Progressive Difficulty**
   - [x] Level 1: Simple layout, wide platforms, small gaps
   - [x] Level 2-3: More floating platforms, moderate gaps
   - [x] Level 4-5: Complex arrangements, challenging jumps

5. **JSON Output Format**
   - [x] Each platform has: `type`, `x`, `y`, `width`, `height`
   - [x] Platforms array is properly formatted
   - [x] All platforms are within level boundaries

6. **Validation**
   - [x] Generated levels are completable (path exists from start to goal)
   - [x] No impossible jumps
   - [x] Platform data is valid JSON

## Technical Notes

```python
def place_platforms(self, level_data, difficulty):
    platforms = []
    level_width = level_data['width']

    # Create ground segments with pit gaps
    current_x = 0
    for pit in level_data['pits']:
        # Ground before pit
        platforms.append({
            'type': 'solid',
            'x': current_x,
            'y': 550,
            'width': pit['x'] - current_x,
            'height': 50
        })
        current_x = pit['x'] + pit['width']

    # Final ground segment
    platforms.append({
        'type': 'solid',
        'x': current_x,
        'y': 550,
        'width': level_width - current_x,
        'height': 50
    })

    # Add floating platforms based on difficulty
    # ...

    return platforms
```

- Use constants for jump reach calculations
- Ensure player spawn and goal positions have platforms nearby
- Consider enemy patrol areas when placing platforms

## Dependencies
- US005: Level generator structure must exist
- US003: Constants (for jump calculations)
