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
   - [x] `src/level/level.py` exists
   - [x] `Level` class is defined

2. **Level Attributes**
   - [x] `level_number`: int
   - [x] `width`, `height`: int (level dimensions)
   - [x] `background_color`: tuple (RGB)
   - [x] `player_spawn`: dict with x, y
   - [x] `goal`: dict with x, y
   - [x] `platforms`: list of Platform objects
   - [x] `enemies`: list (placeholder for Phase 5)
   - [x] `powerups`: list (placeholder for Phase 6)
   - [x] `pits`: list of pit zones

3. **Level Initialization**
   - [x] `__init__(level_data)`: Takes parsed JSON data
   - [x] Converts JSON data to game objects
   - [x] Creates Platform objects from platform data
   - [x] Stores all level information

4. **Level Methods**
   - [x] `update(dt, player)`: Update all entities
   - [x] `render(screen, camera)`: Draw all level elements
   - [x] `check_goal(player)`: Detect level completion
   - [x] `check_pits(player)`: Detect pit falls
   - [x] `reset()`: Reset level state (for retrying)
   - [x] `get_platforms()`: Return platform list
   - [x] `get_spawn_position()`: Return player spawn coords

5. **Platform Object Creation**
   - [x] Converts JSON platform data to Platform objects
   - [x] All platforms are created with correct dimensions
   - [x] Platform types ("solid", "floating") preserved
   - [x] Platform list accessible for collision detection

6. **Pit Detection**
   - [x] Checks if player x-position is within any pit's range
   - [x] Returns True if player falls into pit
   - [x] Uses pit x and width from JSON data

7. **Goal Detection**
   - [x] Checks if player is near goal position (within 50 pixels)
   - [x] Returns True when level should be completed
   - [x] Goal position from JSON data

8. **Rendering**
   - [x] Background filled with background_color
   - [x] All platforms rendered
   - [x] Goal indicator rendered (placeholder rectangle)
   - [x] Rendering uses camera offset

9. **Validation**
   - [x] Level can be instantiated from loaded JSON
   - [x] All platforms render correctly
   - [x] Level dimensions match JSON data
   - [x] Player spawn position accessible

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
