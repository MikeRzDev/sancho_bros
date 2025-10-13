# US023: Test Enemy System Integration

**As a** developer
**I want** to thoroughly test the enemy system
**So that** all enemy behaviors work correctly in all levels

## Priority
High

## Story Points
3

## Acceptance Criteria

1. **Enemy Spawning**
   - [ ] All enemies from level JSON spawn correctly
   - [ ] Enemy counts match specifications:
     - Level 1: 2-3 enemies
     - Level 2: 4-5 enemies
     - Level 3: 6-7 enemies
     - Level 4: 8-9 enemies
     - Level 5: 10-12 enemies
   - [ ] Enemies spawn at correct positions
   - [ ] Enemies spawn on platforms (not in air)

2. **Patrol Behavior Testing**
   - [ ] All enemies patrol within their boundaries
   - [ ] No enemies fall off platforms unexpectedly
   - [ ] Enemies turn around at patrol boundaries
   - [ ] Patrol ranges from JSON are respected
   - [ ] Multiple enemies patrol independently

3. **Collision Testing**
   - [ ] Walking into enemy causes damage
   - [ ] Jumping on enemy defeats it
   - [ ] Stomp works from different approach angles
   - [ ] Side collision causes damage (not stomp)
   - [ ] Dead enemies don't cause collision

4. **Player Lives System**
   - [ ] Lives start at 3
   - [ ] Lives decrement on enemy collision
   - [ ] Lives displayed correctly (prepared for HUD)
   - [ ] Player respawns after taking damage
   - [ ] Game over when lives reach 0

5. **Respawn System**
   - [ ] Player respawns at level spawn point
   - [ ] Player velocity resets on respawn
   - [ ] Enemies continue patrolling after player respawn
   - [ ] Level state persists (defeated enemies stay dead)

6. **Multi-Enemy Scenarios**
   - [ ] Can defeat multiple enemies in sequence
   - [ ] Can stomp chain (stomp, bounce, stomp again)
   - [ ] Multiple enemies in same area work correctly
   - [ ] No collision detection bugs with many enemies

7. **Level Completion with Enemies**
   - [ ] Can complete level without defeating all enemies
   - [ ] Can complete level after defeating all enemies
   - [ ] Enemy defeat is optional (can be avoided)
   - [ ] Level progression works with active enemies

8. **Edge Cases**
   - [ ] Enemy at screen edge renders correctly
   - [ ] Enemy near pit doesn't fall in (patrol boundaries)
   - [ ] Simultaneous collision with multiple enemies handled
   - [ ] Very fast player movement doesn't skip collision

9. **Performance Testing**
   - [ ] 60 FPS maintained with 12 enemies (Level 5)
   - [ ] No slowdown with many enemies on screen
   - [ ] No memory leaks over time
   - [ ] Collision detection is efficient

10. **Visual Validation**
    - [ ] Enemy direction changes visible (facing direction)
    - [ ] Defeated enemies disappear appropriately
    - [ ] Player bounce on stomp is visible
    - [ ] Multiple enemies distinguishable

## Technical Notes

**Test Scenarios:**

1. **Basic Patrol Test:**
   - Stand still and watch enemy patrol
   - Verify turnaround at boundaries
   - Observe for 30 seconds

2. **Stomp Test:**
   - Approach enemy from above
   - Jump directly onto enemy
   - Verify bounce and enemy death

3. **Damage Test:**
   - Walk directly into enemy
   - Verify life loss and respawn

4. **Multi-Stomp Test:**
   - Line up multiple enemies
   - Attempt to stomp chain
   - Verify consecutive defeats

5. **Edge Test:**
   - Spawn near enemy
   - Move away quickly
   - Verify no unexpected collision

**Debug Commands (add to game.py for testing):**
```python
# In handle_events():
if event.key == pygame.K_k:  # Kill all enemies (testing)
    for enemy in self.current_level.enemies:
        enemy.die()
    print("All enemies defeated")

if event.key == pygame.K_l:  # Reset lives to 3 (testing)
    self.player.lives = 3
    print("Lives reset to 3")

if event.key == pygame.K_i:  # Toggle invincibility (testing)
    self.player.is_invincible = not self.player.is_invincible
    print(f"Invincibility: {self.player.is_invincible}")
```

**Logging for Debug:**
```python
# Enemy collision logging:
if colliding_enemy:
    if check_stomp(self.player, colliding_enemy):
        print(f"STOMP at player pos: {self.player.position}, enemy pos: {colliding_enemy.position}")
        colliding_enemy.die()
    else:
        print(f"DAMAGE at player pos: {self.player.position}, enemy pos: {colliding_enemy.position}")
        self.player.take_damage()
```

## Dependencies
- US019: Enemy class must exist
- US020: Patrol AI must work
- US021: Player-enemy collision must work
- US022: Stomp mechanic must work
- US017: Level integration must be complete
