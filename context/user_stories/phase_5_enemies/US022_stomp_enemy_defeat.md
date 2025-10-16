# US022: Implement Stomp Mechanic to Defeat Enemies

**As a** developer
**I want** to implement the stomp mechanic for defeating enemies
**So that** players can defeat Polochos by jumping on them

## Priority
High

## Story Points
5

## Acceptance Criteria

1. **Stomp Detection Logic**
   - [x] `check_stomp(player, enemy)` function created in collision.py
   - [x] Detects when player lands on enemy from above
   - [x] Requires player moving downward (velocity.y > 0)
   - [x] Requires player rect.bottom near enemy rect.top
   - [x] Returns True if valid stomp, False otherwise

2. **Stomp Conditions**
   - [x] Player must be falling (velocity.y > 0)
   - [x] Player's bottom must hit enemy's top half
   - [x] Collision must be from above (not sides)
   - [x] Enemy must be alive

3. **Enemy Defeat**
   - [x] Enemy's `die()` method called on stomp
   - [x] `is_alive` set to False
   - [x] Enemy stops updating
   - [x] Enemy stops rendering
   - [x] Enemy removed from collision checks

4. **Player Bounce**
   - [x] Player bounces upward after stomping
   - [x] Bounce velocity: velocity.y = small negative value (e.g., -8)
   - [x] Allows chaining stomps
   - [x] Feels responsive and satisfying

5. **Stomp vs Damage Distinction**
   - [x] Stomp takes priority over damage collision
   - [x] Checked before damage collision
   - [x] Clear distinction in collision checking order

6. **Visual Feedback**
   - [x] Enemy disappears when defeated (basic)
   - [x] Player bounces visibly
   - [x] Optional: squash animation (placeholder)

7. **Audio Feedback (Placeholder)**
   - [x] Print message when enemy stomped
   - [x] Prepared for sound effect in Phase 7

8. **Multiple Enemy Testing**
   - [x] Can stomp multiple enemies in sequence
   - [x] Stomping one doesn't affect others
   - [x] All enemies can be defeated individually

9. **Validation**
   - [x] Jumping on enemy defeats it
   - [x] Landing from above triggers stomp
   - [x] Walking into enemy still causes damage
   - [x] Player bounces after stomp
   - [x] Can complete levels by defeating all enemies

## Technical Notes

```python
# Add to src/physics/collision.py:
def check_stomp(player, enemy):
    """Check if player is stomping on enemy"""
    if not enemy.is_alive:
        return False

    # Player must be falling
    if player.velocity.y <= 0:
        return False

    # Check if player is above enemy
    if player.rect.bottom >= enemy.rect.top and player.rect.bottom <= enemy.rect.centery:
        # Check horizontal overlap
        if check_aabb_collision(player.rect, enemy.rect):
            return True

    return False

# In Level or Game update (modify from US021):
def update(self, dt):
    # ... existing updates ...

    # Check enemy collisions
    from src.physics.collision import check_enemy_collision, check_stomp
    colliding_enemy = check_enemy_collision(self.player, self.current_level.enemies)

    if colliding_enemy:
        # Check stomp first (priority)
        if check_stomp(self.player, colliding_enemy):
            # Stomp!
            colliding_enemy.die()
            self.player.velocity.y = -8  # Bounce
            print(f"Enemy stomped!")
        else:
            # Damage collision
            self.player.take_damage()
            if self.player.lives > 0:
                # Respawn
                spawn = self.current_level.get_spawn_position()
                self.player.position.x = spawn[0]
                self.player.position.y = spawn[1]
                self.player.velocity = pygame.Vector2(0, 0)
            else:
                self.state = "GAME_OVER"
```

**Optional - Squash Animation:**
```python
# In Polocho class:
def __init__(self, x, y, patrol_left, patrol_right):
    # ... existing code ...
    self.squashed = False
    self.death_timer = 0.0

def die(self):
    """Handle enemy death"""
    self.is_alive = False
    self.squashed = True
    self.death_timer = 0.5  # Show squashed sprite briefly

def update(self, dt, platforms):
    if self.squashed:
        self.death_timer -= dt
        if self.death_timer <= 0:
            # Remove from game (handled by level)
            pass
        return

    # ... existing update code ...

def render(self, screen, camera):
    if not self.is_alive and not self.squashed:
        return

    screen_x = self.position.x - camera.x
    screen_y = self.position.y - camera.y

    if self.squashed:
        # Draw squashed (flattened rectangle)
        pygame.draw.rect(screen, COLOR_ENEMY,
                        (screen_x, screen_y + self.height - 10, self.width, 10))
    else:
        # Normal rendering
        pygame.draw.rect(screen, COLOR_ENEMY,
                        (screen_x, screen_y, self.width, self.height))
```

## Dependencies
- US019: Enemy class must exist
- US021: Player-enemy collision must exist
- US013: Collision system must work
