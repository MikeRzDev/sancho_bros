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
   - [x] Game class tracks current level number
   - [x] Game class has `current_level` attribute (Level object)
   - [x] Game can load specific level by number

2. **Level Loading at Start**
   - [x] Game loads Level 1 when starting
   - [x] LevelLoader instantiated in game initialization
   - [x] Level object created from JSON data
   - [x] Player spawned at level's spawn position

3. **Player-Level Integration**
   - [x] Player collides with level's platforms
   - [x] Player receives level platforms in update()
   - [x] Camera uses level width as boundary
   - [x] Player can navigate the level

4. **Level Rendering Integration**
   - [x] Level renders before player (background)
   - [x] All level elements visible
   - [x] Camera applies to all level elements
   - [x] Z-order correct (background → platforms → player)

5. **Level Update Integration**
   - [x] Level's update() called in game loop
   - [x] Level receives player reference
   - [x] Level checks win/lose conditions
   - [x] Pit detection active

6. **Win Condition**
   - [x] Level checks if player reached goal
   - [x] Game state changes to LEVEL_COMPLETE when goal reached
   - [x] Message displayed (placeholder text)
   - [x] Can exit or proceed (basic handling)

7. **Lose Condition**
   - [x] Level checks if player fell in pit
   - [x] Player loses a life
   - [x] Player respawns at spawn point
   - [x] Game over when lives reach 0

8. **Level Progression**
   - [x] Method to load next level: `load_next_level()`
   - [x] Current level increments
   - [x] Player resets to new level's spawn
   - [x] Camera resets
   - [x] Can progress from Level 1 → 2 (basic test)

9. **Validation**
   - [x] Level 1 loads and displays correctly
   - [x] Player can navigate level terrain
   - [x] Reaching goal shows completion
   - [x] Falling in pit respawns player
   - [x] Can load all 5 levels without errors

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
