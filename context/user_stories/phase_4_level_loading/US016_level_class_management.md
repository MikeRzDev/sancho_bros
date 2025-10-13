# US016: Create Level Class for Game Management

**As a** developer
**I want** to create a Level class that manages all level entities
**So that** the game can interact with a complete level

## Priority
Critical

## Story Points
5

## Acceptance Criteria

1. **Level Class Created**
   - [ ] `src/level/level.py` exists
   - [ ] `Level` class is defined

2. **Level Attributes**
   - [ ] `level_number`: int
   - [ ] `width`, `height`: int (level dimensions)
   - [ ] `background_color`: tuple (RGB)
   - [ ] `player_spawn`: dict with x, y
   - [ ] `goal`: dict with x, y
   - [ ] `platforms`: list of Platform objects
   - [ ] `enemies`: list (placeholder for Phase 5)
   - [ ] `powerups`: list (placeholder for Phase 6)
   - [ ] `pits`: list of pit zones

3. **Level Initialization**
   - [ ] `__init__(level_data)`: Takes parsed JSON data
   - [ ] Converts JSON data to game objects
   - [ ] Creates Platform objects from platform data
   - [ ] Stores all level information

4. **Level Methods**
   - [ ] `update(dt, player)`: Update all entities
   - [ ] `render(screen, camera)`: Draw all level elements
   - [ ] `check_goal(player)`: Detect level completion
   - [ ] `check_pits(player)`: Detect pit falls
   - [ ] `reset()`: Reset level state (for retrying)
   - [ ] `get_platforms()`: Return platform list
   - [ ] `get_spawn_position()`: Return player spawn coords

5. **Platform Object Creation**
   - [ ] Converts JSON platform data to Platform objects
   - [ ] All platforms are created with correct dimensions
   - [ ] Platform types ("solid", "floating") preserved
   - [ ] Platform list accessible for collision detection

6. **Pit Detection**
   - [ ] Checks if player x-position is within any pit's range
   - [ ] Returns True if player falls into pit
   - [ ] Uses pit x and width from JSON data

7. **Goal Detection**
   - [ ] Checks if player is near goal position (within 50 pixels)
   - [ ] Returns True when level should be completed
   - [ ] Goal position from JSON data

8. **Rendering**
   - [ ] Background filled with background_color
   - [ ] All platforms rendered
   - [ ] Goal indicator rendered (placeholder rectangle)
   - [ ] Rendering uses camera offset

9. **Validation**
   - [ ] Level can be instantiated from loaded JSON
   - [ ] All platforms render correctly
   - [ ] Level dimensions match JSON data
   - [ ] Player spawn position accessible

## Technical Notes

```python
# src/level/level.py
import pygame
from src.level.tile import Platform

class Level:
    def __init__(self, level_data):
        self.level_number = level_data['level_number']
        self.width = level_data['width']
        self.height = level_data['height']
        self.background_color = tuple(level_data['background_color'])

        self.player_spawn = level_data['player_spawn']
        self.goal = level_data['goal']
        self.pits = level_data['pits']

        # Create platform objects
        self.platforms = []
        for p_data in level_data['platforms']:
            platform = Platform(
                p_data['x'], p_data['y'],
                p_data['width'], p_data['height'],
                p_data['type']
            )
            self.platforms.append(platform)

        # Placeholders for Phase 5 & 6
        self.enemies = []
        self.powerups = []

    def update(self, dt, player):
        """Update all level entities"""
        # Update enemies (Phase 5)
        # Update powerups (Phase 6)
        pass

    def render(self, screen, camera):
        """Render all level elements"""
        # Fill background
        screen.fill(self.background_color)

        # Render platforms
        for platform in self.platforms:
            platform.render(screen, camera)

        # Render goal (placeholder)
        goal_screen_x = self.goal['x'] - camera.x
        goal_screen_y = self.goal['y'] - camera.y
        pygame.draw.rect(screen, (0, 255, 0),
                        (goal_screen_x, goal_screen_y, 50, 50))

    def check_goal(self, player):
        """Check if player reached goal"""
        distance = abs(player.position.x - self.goal['x'])
        return distance < 50

    def check_pits(self, player):
        """Check if player fell into a pit"""
        for pit in self.pits:
            if (player.position.x >= pit['x'] and
                player.position.x <= pit['x'] + pit['width'] and
                player.position.y > self.height - 100):
                return True
        return False

    def get_platforms(self):
        return self.platforms

    def get_spawn_position(self):
        return (self.player_spawn['x'], self.player_spawn['y'])

    def reset(self):
        """Reset level state"""
        # Reset enemies, powerups, etc.
        pass
```

## Dependencies
- US013: Platform class must exist
- US015: Level loader must exist
