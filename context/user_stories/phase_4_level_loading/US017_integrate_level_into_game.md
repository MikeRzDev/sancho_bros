# US017: Integrate Level Loading into Game Loop

**As a** developer
**I want** to integrate level loading into the main game loop
**So that** the game can play actual generated levels

## Priority
Critical

## Story Points
5

## Acceptance Criteria

1. **Game State Extended**
   - [ ] Game class tracks current level number
   - [ ] Game class has `current_level` attribute (Level object)
   - [ ] Game can load specific level by number

2. **Level Loading at Start**
   - [ ] Game loads Level 1 when starting
   - [ ] LevelLoader instantiated in game initialization
   - [ ] Level object created from JSON data
   - [ ] Player spawned at level's spawn position

3. **Player-Level Integration**
   - [ ] Player collides with level's platforms
   - [ ] Player receives level platforms in update()
   - [ ] Camera uses level width as boundary
   - [ ] Player can navigate the level

4. **Level Rendering Integration**
   - [ ] Level renders before player (background)
   - [ ] All level elements visible
   - [ ] Camera applies to all level elements
   - [ ] Z-order correct (background → platforms → player)

5. **Level Update Integration**
   - [ ] Level's update() called in game loop
   - [ ] Level receives player reference
   - [ ] Level checks win/lose conditions
   - [ ] Pit detection active

6. **Win Condition**
   - [ ] Level checks if player reached goal
   - [ ] Game state changes to LEVEL_COMPLETE when goal reached
   - [ ] Message displayed (placeholder text)
   - [ ] Can exit or proceed (basic handling)

7. **Lose Condition**
   - [ ] Level checks if player fell in pit
   - [ ] Player loses a life
   - [ ] Player respawns at spawn point
   - [ ] Game over when lives reach 0

8. **Level Progression**
   - [ ] Method to load next level: `load_next_level()`
   - [ ] Current level increments
   - [ ] Player resets to new level's spawn
   - [ ] Camera resets
   - [ ] Can progress from Level 1 → 2 (basic test)

9. **Validation**
   - [ ] Level 1 loads and displays correctly
   - [ ] Player can navigate level terrain
   - [ ] Reaching goal shows completion
   - [ ] Falling in pit respawns player
   - [ ] Can load all 5 levels without errors

## Technical Notes

```python
# In Game class:
from src.level.level_loader import LevelLoader
from src.level.level import Level
from src.entities.player import Player

class Game:
    def __init__(self):
        # ... existing init code ...

        # Level management
        self.level_loader = LevelLoader()
        self.current_level_number = 1
        self.current_level = None
        self.load_level(1)

        # Player at spawn position
        spawn = self.current_level.get_spawn_position()
        self.player = Player(spawn[0], spawn[1])

    def load_level(self, level_num):
        """Load a level by number"""
        level_data = self.level_loader.load_level_by_number(level_num)
        if level_data:
            self.current_level = Level(level_data)
            self.current_level_number = level_num
            print(f"Loaded Level {level_num}")
        else:
            print(f"Failed to load Level {level_num}")

    def load_next_level(self):
        """Load the next level"""
        next_level = self.current_level_number + 1
        if next_level <= 5:
            self.load_level(next_level)
            # Respawn player
            spawn = self.current_level.get_spawn_position()
            self.player.position.x = spawn[0]
            self.player.position.y = spawn[1]
            self.player.velocity.x = 0
            self.player.velocity.y = 0
        else:
            print("Game Complete!")

    def update(self, dt):
        # Update level
        self.current_level.update(dt, self.player)

        # Update player with level platforms
        platforms = self.current_level.get_platforms()
        self.player.update(dt, platforms)

        # Update camera
        self.camera.update(self.player.position, self.current_level.width)

        # Check win condition
        if self.current_level.check_goal(self.player):
            print("Level Complete!")
            self.load_next_level()

        # Check lose condition
        if self.current_level.check_pits(self.player):
            self.player.take_damage()
            if self.player.lives > 0:
                # Respawn
                spawn = self.current_level.get_spawn_position()
                self.player.position.x = spawn[0]
                self.player.position.y = spawn[1]
                self.player.velocity.y = 0
            else:
                print("Game Over!")

    def render(self):
        # Render level (background, platforms)
        self.current_level.render(self.screen, self.camera)

        # Render player
        self.player.render(self.screen, self.camera)

        pygame.display.flip()
```

## Dependencies
- US015: Level loader must exist
- US016: Level class must exist
- US010: Player class must exist
- US014: Camera must exist
- US013: Collision system must work
