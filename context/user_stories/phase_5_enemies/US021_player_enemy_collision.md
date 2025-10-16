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
   - [x] `check_enemy_collision(player, enemies)` function created
   - [x] Uses AABB collision between player and enemy rects
   - [x] Returns colliding enemy or None
   - [x] Checks all alive enemies

2. **Collision Types**
   - [x] Detects when player touches enemy from any side
   - [x] Distinguishes between stomp (top) and damage (other sides)
   - [x] Collision type determined by velocity and position

3. **Damage Collision**
   - [x] Player takes damage when touching enemy from side/bottom
   - [x] Collision detected when player.rect overlaps enemy.rect
   - [x] Damage only applies to alive enemies
   - [x] Player knocked back slightly on hit (optional) - method created, can be used in future

4. **Player Damage Handling**
   - [x] `take_damage()` method reduces lives by 1
   - [x] Player respawns at level spawn point
   - [x] Player gets brief invincibility (1-2 seconds, optional)
   - [x] Lives counter updates correctly

5. **Knockback Effect (Optional)**
   - [x] Player pushed away from enemy on hit - method created
   - [x] Knockback direction opposite to collision side - method created
   - [x] Knockback velocity added to player - method created

6. **Integration with Game Loop**
   - [x] Collision check called in level or game update
   - [x] Happens after player and enemy movement
   - [x] Before rendering

7. **Visual Feedback**
   - [ ] Player blinks during invincibility (optional) - will be implemented with visual polish
   - [x] Clear indication of damage taken - console messages
   - [ ] Lives display updates (prepared for Phase 7) - HUD will be in Phase 7

8. **Validation**
   - [x] Walking into enemy causes damage
   - [x] Player respawns after damage
   - [x] Lives decrement correctly
   - [x] Game over when lives = 0
   - [x] Collision works with multiple enemies

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
