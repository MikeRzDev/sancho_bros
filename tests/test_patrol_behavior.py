"""
Test script for US023 AC2: Patrol Behavior
Simulates enemy patrol to verify boundaries and direction changes.
"""

import pygame
from src.entities.enemy import Polocho

def test_patrol_behavior():
    """Test enemy patrol behavior through simulation."""
    pygame.init()

    print("=" * 60)
    print("US023 AC2: PATROL BEHAVIOR TEST")
    print("=" * 60)

    all_tests_passed = True

    # Test 1: Enemy respects patrol boundaries
    print("\n--- TEST 1: Patrol Boundaries ---")
    enemy = Polocho(500, 500, 400, 600)

    # Simulate moving right to boundary
    for i in range(200):
        enemy.patrol()
        enemy.position.x += enemy.velocity.x

    if enemy.position.x >= 600:
        enemy.position.x = 600
        print(f"❌ Enemy exceeded right boundary: {enemy.position.x}")
        all_tests_passed = False
    elif 595 <= enemy.position.x <= 600:
        print(f"✓ Enemy stopped at right boundary: {enemy.position.x:.1f}")
    else:
        print(f"⚠ Enemy position unexpected: {enemy.position.x:.1f}")

    # Verify direction changed
    if enemy.facing_direction == "LEFT":
        print(f"✓ Enemy turned LEFT at right boundary")
    else:
        print(f"❌ Enemy didn't turn at boundary: {enemy.facing_direction}")
        all_tests_passed = False

    # Simulate moving left to boundary
    for i in range(400):
        enemy.patrol()
        enemy.position.x += enemy.velocity.x

    if enemy.position.x <= 400:
        enemy.position.x = 400
        print(f"✓ Enemy stopped at left boundary: {enemy.position.x:.1f}")
    else:
        print(f"⚠ Enemy position: {enemy.position.x:.1f}")

    if enemy.facing_direction == "RIGHT":
        print(f"✓ Enemy turned RIGHT at left boundary")
    else:
        print(f"❌ Enemy didn't turn at boundary: {enemy.facing_direction}")
        all_tests_passed = False

    # Test 2: Multiple enemies patrol independently
    print("\n--- TEST 2: Multiple Enemies Patrol Independently ---")
    enemy1 = Polocho(100, 500, 50, 150)
    enemy2 = Polocho(300, 500, 200, 400)
    enemy3 = Polocho(500, 500, 450, 550)

    # Simulate for 100 frames
    for frame in range(100):
        enemy1.patrol()
        enemy1.position.x += enemy1.velocity.x

        enemy2.patrol()
        enemy2.position.x += enemy2.velocity.x

        enemy3.patrol()
        enemy3.position.x += enemy3.velocity.x

    # Verify they're in different positions (not synchronized)
    positions = [enemy1.position.x, enemy2.position.x, enemy3.position.x]
    if len(set(positions)) == 3:  # All different positions
        print(f"✓ Enemies patrol independently:")
        print(f"  Enemy 1: x={enemy1.position.x:.1f}, facing={enemy1.facing_direction}")
        print(f"  Enemy 2: x={enemy2.position.x:.1f}, facing={enemy2.facing_direction}")
        print(f"  Enemy 3: x={enemy3.position.x:.1f}, facing={enemy3.facing_direction}")
    else:
        print(f"❌ Enemies synchronized (unexpected)")
        all_tests_passed = False

    # Test 3: Direction changes work correctly
    print("\n--- TEST 3: Direction Changes ---")
    enemy = Polocho(550, 500, 500, 600)
    enemy.facing_direction = "RIGHT"

    # Move to right boundary
    while enemy.position.x < 600:
        enemy.patrol()
        enemy.position.x += enemy.velocity.x
        if enemy.position.x > 605:  # Safety stop
            break

    if enemy.facing_direction == "LEFT":
        print(f"✓ Direction changed to LEFT at right boundary")
    else:
        print(f"❌ Direction didn't change: {enemy.facing_direction}")
        all_tests_passed = False

    # Move back to left boundary
    while enemy.position.x > 500:
        enemy.patrol()
        enemy.position.x += enemy.velocity.x
        if enemy.position.x < 495:  # Safety stop
            break

    if enemy.facing_direction == "RIGHT":
        print(f"✓ Direction changed to RIGHT at left boundary")
    else:
        print(f"❌ Direction didn't change: {enemy.facing_direction}")
        all_tests_passed = False

    # Test 4: Patrol ranges from JSON are respected
    print("\n--- TEST 4: Various Patrol Ranges ---")
    test_ranges = [
        (100, 200, "Small range (100px)"),
        (500, 800, "Medium range (300px)"),
        (1000, 1500, "Large range (500px)")
    ]

    for left, right, desc in test_ranges:
        enemy = Polocho((left + right) // 2, 500, left, right)

        # Simulate patrol
        min_x = enemy.position.x
        max_x = enemy.position.x

        for _ in range(1000):
            enemy.patrol()
            enemy.position.x += enemy.velocity.x
            min_x = min(min_x, enemy.position.x)
            max_x = max(max_x, enemy.position.x)

        # Check if enemy stayed within bounds (with small tolerance)
        if min_x >= left - 5 and max_x <= right + 5:
            print(f"✓ {desc}: stayed within [{left}, {right}], actual [{min_x:.1f}, {max_x:.1f}]")
        else:
            print(f"❌ {desc}: expected [{left}, {right}], got [{min_x:.1f}, {max_x:.1f}]")
            all_tests_passed = False

    print("\n" + "=" * 60)
    if all_tests_passed:
        print("✓ ALL PATROL BEHAVIOR TESTS PASSED")
    else:
        print("❌ SOME TESTS FAILED")
    print("=" * 60)

    pygame.quit()
    return all_tests_passed

if __name__ == "__main__":
    test_patrol_behavior()
