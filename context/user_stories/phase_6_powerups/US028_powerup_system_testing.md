# US028: Test Complete Power-Up System

**As a** developer
**I want** to thoroughly test the power-up and laser system
**So that** all power-up mechanics work correctly

## Priority
High

## Story Points
3

## Acceptance Criteria

1. **Power-Up Spawning**
   - [x] Power-ups spawn at correct locations from JSON
   - [x] Power-up counts match specifications:
     - Level 1: 1 power-up
     - Level 2: 1 power-up
     - Level 3: 2 power-ups
     - Level 4: 2 power-ups
     - Level 5: 2-3 power-ups
   - [x] Power-ups visible and reachable
   - [x] Bobbing animation works

2. **Power-Up Collection**
   - [x] Walking through power-up collects it
   - [x] Power-up disappears after collection
   - [x] Player state changes (has_powerup = True)
   - [x] Timer starts at 10 seconds
   - [x] Visual indication of powered state

3. **Timer Functionality**
   - [x] Timer counts down from 10 seconds
   - [x] Timer displayed (if implemented)
   - [x] Power-up expires after 10 seconds
   - [x] `has_powerup` becomes False after expiration
   - [x] Can no longer shoot after expiration

4. **Laser Shooting**
   - [x] Can shoot when powered up
   - [x] Cannot shoot without power-up
   - [x] X key and Ctrl key both work
   - [x] Laser fires in correct direction
   - [x] Laser matches player facing direction

5. **Shooting Cooldown**
   - [x] Cannot spam lasers (cooldown enforced)
   - [x] 0.5 second cooldown between shots
   - [x] Cooldown timer accurate
   - [x] Can shoot repeatedly with cooldown

6. **Laser Behavior**
   - [x] Laser travels horizontally
   - [x] Laser moves at high speed
   - [x] Laser destroys after 2 seconds
   - [x] Laser destroys on platform hit
   - [x] Laser destroys on enemy hit

7. **Laser-Enemy Interaction**
   - [x] Laser defeats enemies on contact
   - [x] Enemy dies when hit by laser
   - [x] Laser disappears after hitting enemy
   - [x] Can defeat multiple enemies with multiple lasers
   - [x] Works on all enemy types

8. **Multiple Power-Ups**
   - [x] Collecting 2nd power-up resets timer
   - [x] Timer resets to 10 seconds (doesn't add)
   - [x] Can collect all power-ups in level
   - [x] Each collection provides feedback

9. **Power-Up Strategy**
   - [x] Power-ups useful for defeating enemies
   - [x] Can clear enemies from distance with laser
   - [x] Power-up placement encourages tactical use
   - [x] Levels completable with and without power-ups

10. **Edge Cases**
    - [x] Shooting while jumping works
    - [x] Shooting while moving works
    - [x] Multiple lasers on screen work correctly
    - [x] Laser destroys enemies at screen edge
    - [x] Collecting power-up at low timer resets it

11. **Performance**
    - [x] 60 FPS maintained with many lasers
    - [x] No slowdown with 10+ lasers on screen
    - [x] Laser collision detection is efficient
    - [x] No memory leaks with laser creation/destruction

12. **Visual Validation**
    - [x] Powered state clearly visible
    - [x] Lasers easily distinguishable
    - [x] Timer countdown visible
    - [x] Muzzle flash shows shooting (if implemented)

## Technical Notes

**Test Scenarios:**

1. **Basic Collection Test:**
   - Start Level 1
   - Navigate to power-up
   - Collect it
   - Verify timer starts

2. **Shooting Test:**
   - Collect power-up
   - Press X key
   - Verify laser fires
   - Verify direction matches facing

3. **Cooldown Test:**
   - Collect power-up
   - Press X rapidly
   - Count lasers (should be limited by cooldown)
   - Verify ~2 shots per second

4. **Enemy Defeat Test:**
   - Collect power-up
   - Shoot enemy from distance
   - Verify enemy defeated
   - Verify laser disappears

5. **Expiration Test:**
   - Collect power-up
   - Wait 10 seconds
   - Try shooting after expiration
   - Verify cannot shoot

6. **Multiple Power-Ups Test:**
   - Play Level 3 (2 power-ups)
   - Collect first power-up
   - Wait 5 seconds
   - Collect second power-up
   - Verify timer reset to 10 seconds

7. **Rapid Fire Test:**
   - Collect power-up
   - Hold X key
   - Verify lasers fire at cooldown rate
   - Verify no excessive lag

**Debug Commands (add for testing):**
```python
# In handle_events():
if event.key == pygame.K_p:  # Grant power-up instantly
    self.player.collect_powerup()
    print("Power-up granted")

if event.key == pygame.K_t:  # Add time to power-up
    if self.player.has_powerup:
        self.player.powerup_timer = 30.0
        print("Power-up timer extended")
```

**Common Issues to Check:**
- Laser spawns inside player
- Laser direction opposite to player facing
- Cooldown too short/long
- Timer doesn't count down
- Can shoot without power-up
- Laser doesn't hit enemies
- Multiple lasers cause lag

## Dependencies
- US024: PowerUp class must exist
- US025: Collection system must work
- US026: Laser class must exist
- US027: Shooting mechanics must work
- US019: Enemy class must exist
- US017: Game loop integration must be complete
