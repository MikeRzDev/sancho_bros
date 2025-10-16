# Known Issues

## Current Issues

### Minor Issues

**Issue #1**: Debug Commands Still Active
- **Severity**: Low
- **Description**: Debug commands (K, L, I, T, 1-5 keys) are available during gameplay even with DEBUG=False
- **Workaround**: Simply don't use them; they're not documented in user-facing materials
- **Status**: Accepted - useful for development/testing
- **Fix**: Could gate these commands behind DEBUG flag if needed for production

**Issue #2**: No Sound Effects or Music
- **Severity**: Low (Expected)
- **Description**: Game uses placeholder graphics and has no audio
- **Workaround**: None - this is a prototype/learning project
- **Status**: Accepted - audio not in scope for current phase
- **Future**: See FUTURE_IMPROVEMENTS.md for audio plans

**Issue #3**: Test Files in Repository
- **Severity**: Low
- **Description**: test_enemy_spawning.py and test_patrol_behavior.py are development test files
- **Workaround**: N/A - moved to tests/ directory
- **Status**: Resolved - files organized in tests/ folder

## Fixed Issues

**Issue**: Camera Attribute Error (CRITICAL)
- **Fixed**: 2025-10-16
- **Description**: Game crashed when advancing levels due to `camera.offset.x` instead of `camera.x`
- **Resolution**: Changed all references from `camera.offset` to `camera.x/y` in game.py:134-135, 176-177, 196-197

## Issue Reporting

If you find additional issues, please note:
- What you were doing when the issue occurred
- Expected behavior vs actual behavior
- Steps to reproduce
- Your Python version and OS
