# US018: Test All 5 Levels Are Playable

**As a** developer
**I want** to verify all 5 generated levels load and are playable
**So that** level progression works correctly

## Priority
High

## Story Points
3

## Acceptance Criteria

1. **Level 1 Playability**
   - [x] Level 1 loads without errors
   - [x] Player spawns at correct position
   - [x] All platforms render correctly
   - [x] Player can navigate from spawn to goal
   - [x] Pits are positioned correctly
   - [x] Goal is reachable

2. **Level 2 Playability**
   - [x] Level 2 loads after completing Level 1
   - [x] Level dimensions match specification (2500px)
   - [x] Increased difficulty is noticeable
   - [x] All jumps are possible
   - [x] Level is completable

3. **Level 3 Playability**
   - [x] Level 3 loads after completing Level 2
   - [x] Level dimensions match specification (3000px)
   - [x] Complex platform arrangements work
   - [x] All jumps are possible
   - [x] Level is completable

4. **Level 4 Playability**
   - [x] Level 4 loads after completing Level 3
   - [x] Level dimensions match specification (3500px)
   - [x] Long jumps are challenging but possible
   - [x] Camera scrolling works for longer level
   - [x] Level is completable

5. **Level 5 Playability**
   - [x] Level 5 loads after completing Level 4
   - [x] Level dimensions match specification (4000px)
   - [x] Maximum difficulty is evident
   - [x] All sections are reachable
   - [x] Level is completable

6. **Level Transitions**
   - [x] Smooth transition between levels
   - [x] No crashes during level loading
   - [x] Player state resets properly
   - [x] Camera resets for each level
   - [x] Lives persist across levels

7. **Level Variety Validation**
   - [x] Each level feels distinct
   - [x] Difficulty progression is clear
   - [x] Platform layouts are varied
   - [x] No identical level designs

8. **Performance**
   - [x] All levels maintain 60 FPS
   - [x] No memory leaks across level transitions
   - [x] Level loading is fast (< 1 second)

9. **Fallback Testing**
   - [x] Can restart any level if failed
   - [x] Can manually jump to specific level (for testing)
   - [x] Invalid level number handled gracefully

## Technical Notes

```python
# Add to Game class for testing:
def load_specific_level(self, level_num):
    """Load a specific level (for testing)"""
    if 1 <= level_num <= 5:
        self.load_level(level_num)
        spawn = self.current_level.get_spawn_position()
        self.player.position.x = spawn[0]
        self.player.position.y = spawn[1]
        self.player.velocity = pygame.Vector2(0, 0)
        print(f"Jumped to Level {level_num}")

# Test keyboard shortcut (in handle_events):
if event.key == pygame.K_1:  # Load Level 1
    self.load_specific_level(1)
elif event.key == pygame.K_2:  # Load Level 2
    self.load_specific_level(2)
# ... etc for testing
```

**Testing Checklist:**
1. Start game → complete Level 1 → verify Level 2 loads
2. Complete all 5 levels in sequence
3. Test each level individually using shortcuts
4. Verify impossible jumps don't exist
5. Check pit placement doesn't block progression
6. Confirm goal is always reachable

**Common Issues to Check:**
- Platforms too far apart (max jump distance)
- Pits without crossing method
- Goals inside walls or unreachable
- Player spawn in mid-air or pit
- Overlapping platforms causing collision issues

## Dependencies
- US017: Game loop integration must be complete
- US009: All 5 level JSON files must exist
- US013: Collision system must work
