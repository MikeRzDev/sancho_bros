"""
Test script for US023 AC1: Enemy Spawning
Verifies that enemies spawn correctly in all 5 levels.
"""

import pygame
from src.level import LevelLoader

def test_enemy_spawning():
    """Test enemy spawning for all 5 levels."""
    pygame.init()

    loader = LevelLoader()

    print("=" * 60)
    print("US023 AC1: ENEMY SPAWNING TEST")
    print("=" * 60)

    expected_counts = {
        1: (2, 3),   # Level 1: 2-3 enemies
        2: (4, 5),   # Level 2: 4-5 enemies
        3: (6, 7),   # Level 3: 6-7 enemies
        4: (8, 9),   # Level 4: 8-9 enemies
        5: (10, 12)  # Level 5: 10-12 enemies
    }

    all_tests_passed = True

    for level_num in range(1, 6):
        print(f"\n--- LEVEL {level_num} ---")

        # Load level data
        level_data = loader.load_level_by_number(level_num)

        if not level_data:
            print(f"❌ FAILED: Could not load level {level_num}")
            all_tests_passed = False
            continue

        # Get enemy data
        enemies_data = level_data.get('enemies', [])
        enemy_count = len(enemies_data)

        min_expected, max_expected = expected_counts[level_num]

        # Test 1: Enemy count matches specification
        if min_expected <= enemy_count <= max_expected:
            print(f"✓ Enemy count: {enemy_count} (expected {min_expected}-{max_expected})")
        else:
            print(f"❌ Enemy count: {enemy_count} (expected {min_expected}-{max_expected})")
            all_tests_passed = False

        # Test 2: All enemies have required fields
        for i, enemy in enumerate(enemies_data):
            if 'type' not in enemy or enemy['type'] != 'polocho':
                print(f"❌ Enemy {i}: Missing or invalid type")
                all_tests_passed = False
            if 'x' not in enemy or 'y' not in enemy:
                print(f"❌ Enemy {i}: Missing position")
                all_tests_passed = False
            if 'patrol_left' not in enemy or 'patrol_right' not in enemy:
                print(f"❌ Enemy {i}: Missing patrol boundaries")
                all_tests_passed = False

            # Test 3: Enemy spawns at correct position (show positions)
            if 'x' in enemy and 'y' in enemy:
                print(f"  Enemy {i+1}: pos=({enemy['x']}, {enemy['y']}), "
                      f"patrol=[{enemy.get('patrol_left', 'N/A')}, {enemy.get('patrol_right', 'N/A')}]")

        # Test 4: Verify enemies spawn on platforms (y position check)
        platforms = level_data.get('platforms', [])
        for i, enemy in enumerate(enemies_data):
            enemy_x = enemy.get('x', 0)
            enemy_y = enemy.get('y', 0)
            enemy_bottom = enemy_y + 40  # Assume enemy height is 40

            on_platform = False
            for platform in platforms:
                plat_x = platform['x']
                plat_y = platform['y']
                plat_width = platform['width']

                # Check if enemy is above and near a platform
                if (plat_x <= enemy_x <= plat_x + plat_width and
                    abs(enemy_bottom - plat_y) <= 50):
                    on_platform = True
                    break

            if not on_platform:
                print(f"⚠ Enemy {i+1} might not be on a platform (y={enemy_y})")

    print("\n" + "=" * 60)
    if all_tests_passed:
        print("✓ ALL ENEMY SPAWNING TESTS PASSED")
    else:
        print("❌ SOME TESTS FAILED")
    print("=" * 60)

    pygame.quit()
    return all_tests_passed

if __name__ == "__main__":
    test_enemy_spawning()
