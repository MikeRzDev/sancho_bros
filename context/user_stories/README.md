# SANCHO BROS - USER STORIES

This directory contains all user stories organized by development phase for the Sancho Bros game implementation.

## Overview

**Total User Stories: 35**

The user stories follow the 7-phase development roadmap outlined in `game_implementation.md`. Each story includes:
- User story format (As a... I want... So that...)
- Priority and story points
- Detailed acceptance criteria
- Technical implementation notes
- Dependencies on other stories

## Phase Structure

### Phase 1: Setup (4 stories)
**Location:** `phase_1_setup/`

- **US001**: Project Structure Setup
- **US002**: Install Pygame and Dependencies
- **US003**: Game Constants Configuration
- **US004**: Basic Game Window and Main Loop

**Goal:** Establish project foundation and development environment.

### Phase 2: Level Generator (5 stories)
**Location:** `phase_2_level_generator/`

- **US005**: Level Generator Structure
- **US006**: Platform Generation Logic
- **US007**: Enemy Placement Logic
- **US008**: Power-Up and Pit Placement
- **US009**: Complete Level JSON Generation

**Goal:** Create tool to generate all 5 playable level files.

### Phase 3: Core Mechanics (5 stories)
**Location:** `phase_3_core_mechanics/`

- **US010**: Player Entity Class (Sancho)
- **US011**: Physics and Gravity System
- **US012**: Player Movement and Controls
- **US013**: Collision Detection System
- **US014**: Camera/Viewport System

**Goal:** Implement fundamental platforming mechanics.

### Phase 4: Level Loading (4 stories)
**Location:** `phase_4_level_loading/`

- **US015**: Level Loader and JSON Parser
- **US016**: Level Class Management
- **US017**: Integrate Level into Game Loop
- **US018**: Test All 5 Levels Playability

**Goal:** Load and play externally-defined levels.

### Phase 5: Enemies (5 stories)
**Location:** `phase_5_enemies/`

- **US019**: Enemy Entity Class (Polocho)
- **US020**: Enemy Patrol AI
- **US021**: Player-Enemy Collision Detection
- **US022**: Stomp Mechanic to Defeat Enemies
- **US023**: Enemy System Integration Testing

**Goal:** Add enemies with AI and combat mechanics.

### Phase 6: Power-Ups (5 stories)
**Location:** `phase_6_powerups/`

- **US024**: Power-Up Entity Class (La Arepa Dorada)
- **US025**: Power-Up Collection System
- **US026**: Laser Projectile Class
- **US027**: Laser Shooting Mechanics
- **US028**: Power-Up System Testing

**Goal:** Implement power-up collection and laser shooting ability.

### Phase 7: UI & Polish (7 stories)
**Location:** `phase_7_ui_polish/`

- **US029**: Game State Management
- **US030**: Main Menu UI
- **US031**: HUD Display
- **US032**: Pause Menu and Game Over Screens
- **US033**: Level Complete Screen and Transitions
- **US034**: Final Integration Testing
- **US035**: Documentation and Polish

**Goal:** Complete UI, menus, and final polish for release.

## Story Priority Levels

- **Critical**: Core functionality, blocks other work
- **High**: Important features, needed for MVP
- **Medium**: Nice-to-have features, enhances experience

## Story Points Scale

- **1 point**: Simple task, < 2 hours
- **2 points**: Straightforward task, 2-4 hours
- **3 points**: Moderate complexity, 4-8 hours
- **5 points**: Complex task, 8-16 hours
- **8 points**: Very complex, 16+ hours

## Dependencies

User stories are designed to be implemented in order within each phase. Cross-phase dependencies are explicitly noted in each story's "Dependencies" section.

### Critical Path

The following stories must be completed in order as they form the critical path:

1. US001 (Project Structure)
2. US002 (Install Pygame)
3. US003 (Constants)
4. US004 (Game Window)
5. US005-US009 (Level Generator - all must complete before game can run)
6. US010 (Player Class)
7. US011 (Physics)
8. US013 (Collision)
9. US015-US017 (Level Loading System)

After the critical path, other stories can be developed with more flexibility.

## Implementation Notes

### Suggested Development Flow

1. **Phase 1-2 (Days 1-2)**: Set up project and generate levels
   - Complete Phase 1 entirely
   - Complete Phase 2 entirely
   - **Checkpoint**: 5 valid level JSON files exist

2. **Phase 3 (Days 2-3)**: Build core platforming
   - Implement in story order
   - **Checkpoint**: Player can move, jump, and collide with platforms

3. **Phase 4 (Days 3-4)**: Load levels
   - Implement in story order
   - **Checkpoint**: Can play through all 5 levels

4. **Phase 5 (Days 4-5)**: Add enemies
   - Implement in story order
   - **Checkpoint**: Enemies patrol and can be defeated

5. **Phase 6 (Days 5-6)**: Add power-ups
   - Implement in story order
   - **Checkpoint**: Can shoot lasers and defeat enemies from distance

6. **Phase 7 (Days 6-7)**: Complete UI and polish
   - Implement in story order
   - **Checkpoint**: Complete game with all menus

### Testing Strategy

- Test each user story's acceptance criteria before marking complete
- Integration test at end of each phase
- Full regression test before Phase 7
- Final comprehensive test in US034

## Usage for Development

1. Read user story file
2. Implement according to acceptance criteria
3. Test all acceptance criteria
4. Check dependencies are met
5. Mark story as complete
6. Move to next story

## File Naming Convention

User stories follow the pattern:
```
US###_brief_description.md
```

Where:
- `###` = Zero-padded story number (001-035)
- `brief_description` = Snake_case summary

## Additional Resources

- **Game Implementation Spec**: `../game_implementation.md`
- **Development Guide**: `../../CLAUDE.md`
- **Problem Description**: `../../problem_description.md`

## Total Estimated Effort

Based on story points:
- **Phase 1**: 7 points (~14 hours)
- **Phase 2**: 19 points (~38 hours)
- **Phase 3**: 21 points (~42 hours)
- **Phase 4**: 16 points (~32 hours)
- **Phase 5**: 21 points (~42 hours)
- **Phase 6**: 19 points (~38 hours)
- **Phase 7**: 26 points (~52 hours)

**Total**: 129 story points (~258 hours)

*Note: Estimates assume solo developer, may vary with experience level.*

## Version History

- **v1.0** (2025-10-13): Initial user stories created covering full MVP
