# US021: Implement Player-Enemy Collision Detection

**As a** developer
**I want** to detect collisions between player and enemies
**So that** enemies can damage the player

## Priority
High

## Story Points
3

## Acceptance Criteria

1. **Collision Detection**
   - [ ] `check_enemy_collision(player, enemies)` function created
   - [ ] Uses AABB collision between player and enemy rects
   - [ ] Returns colliding enemy or None
   - [ ] Checks all alive enemies

2. **Collision Types**
   - [ ] Detects when player touches enemy from any side
   - [ ] Distinguishes between stomp (top) and damage (other sides)
   - [ ] Collision type determined by velocity and position

3. **Damage Collision**
   - [ ] Player takes damage when touching enemy from side/bottom
   - [ ] Collision detected when player.rect overlaps enemy.rect
   - [ ] Damage only applies to alive enemies
   - [ ] Player knocked back slightly on hit (optional)

4. **Player Damage Handling**
   - [ ] `take_damage()` method reduces lives by 1
   - [ ] Player respawns at level spawn point
   - [ ] Player gets brief invincibility (1-2 seconds, optional)
   - [ ] Lives counter updates correctly

5. **Knockback Effect (Optional)**
   - [ ] Player pushed away from enemy on hit
   - [ ] Knockback direction opposite to collision side
   - [ ] Knockback velocity added to player

6. **Integration with Game Loop**
   - [ ] Collision check called in level or game update
   - [ ] Happens after player and enemy movement
   - [ ] Before rendering

7. **Visual Feedback**
   - [ ] Player blinks during invincibility (optional)
   - [ ] Clear indication of damage taken
   - [ ] Lives display updates (prepared for Phase 7)

8. **Validation**
   - [ ] Walking into enemy causes damage
   - [ ] Player respawns after damage
   - [ ] Lives decrement correctly
   - [ ] Game over when lives = 0
   - [ ] Collision works with multiple enemies

## Technical Notes

```python
# Add to src/physics/collision.py:
def check_enemy_collision(player, enemies):
    """Check collision between player and enemies"""
    for enemy in enemies:
        if enemy.is_alive and check_aabb_collision(player.rect, enemy.rect):
            return enemy
    return None

# In Player class:
def take_damage(self):
    """Handle player taking damage"""
    self.lives -= 1
    print(f"Player hit! Lives remaining: {self.lives}")

    if self.lives > 0:
        # Player will respawn (handled by game loop)
        pass
    else:
        print("Game Over!")

def apply_knockback(self, direction, strength=5):
    """Apply knockback to player (optional)"""
    if direction == "LEFT":
        self.velocity.x = -strength
    else:
        self.velocity.x = strength

# In Level or Game update:
def update(self, dt):
    # ... existing updates ...

    # Check enemy collisions
    from src.physics.collision import check_enemy_collision
    colliding_enemy = check_enemy_collision(self.player, self.current_level.enemies)

    if colliding_enemy:
        # Check if stomp (will be in US022)
        if self.player.velocity.y > 0 and self.player.rect.bottom < colliding_enemy.rect.centery:
            # Stomp - handled in US022
            pass
        else:
            # Damage
            self.player.take_damage()
            if self.player.lives > 0:
                # Respawn
                spawn = self.current_level.get_spawn_position()
                self.player.position.x = spawn[0]
                self.player.position.y = spawn[1]
                self.player.velocity = pygame.Vector2(0, 0)
            else:
                # Game over
                self.state = "GAME_OVER"
```

**Optional - Invincibility System:**
```python
# In Player class:
def __init__(self, x, y):
    # ... existing code ...
    self.is_invincible = False
    self.invincibility_timer = 0.0

def update(self, dt, platforms):
    # ... existing code ...

    # Update invincibility
    if self.is_invincible:
        self.invincibility_timer -= dt
        if self.invincibility_timer <= 0:
            self.is_invincible = False

def take_damage(self):
    if not self.is_invincible:
        self.lives -= 1
        self.is_invincible = True
        self.invincibility_timer = 2.0  # 2 seconds
```

## Dependencies
- US010: Player class must exist
- US019: Enemy class must exist
- US013: Collision system must exist
