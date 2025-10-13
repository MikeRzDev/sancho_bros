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
   - [ ] Each level has a continuous ground floor at y=550
   - [ ] Ground extends from x=0 to appropriate positions
   - [ ] Ground has gaps (pits) at designated locations
   - [ ] Ground segments are type "solid"

2. **Floating Platform Generation**
   - [ ] Floating platforms are type "floating"
   - [ ] Platforms are placed at varying heights (y: 200-500)
   - [ ] Platform spacing allows for reasonable jumps (considering JUMP_STRENGTH = -15)
   - [ ] Platform density increases with level difficulty
   - [ ] Platforms are 60-150 pixels wide, 20 pixels high

3. **Platform Placement Rules**
   - [ ] Minimum platform spacing: 100 pixels horizontally
   - [ ] Maximum jump gap: 250 pixels (must be reachable)
   - [ ] Platforms don't overlap
   - [ ] At least one platform every 400 pixels for progression

4. **Progressive Difficulty**
   - [ ] Level 1: Simple layout, wide platforms, small gaps
   - [ ] Level 2-3: More floating platforms, moderate gaps
   - [ ] Level 4-5: Complex arrangements, challenging jumps

5. **JSON Output Format**
   - [ ] Each platform has: `type`, `x`, `y`, `width`, `height`
   - [ ] Platforms array is properly formatted
   - [ ] All platforms are within level boundaries

6. **Validation**
   - [ ] Generated levels are completable (path exists from start to goal)
   - [ ] No impossible jumps
   - [ ] Platform data is valid JSON

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
