# Tasks: Sync Passenger Rosters with Handwritten Family List (24 Guests)

- [x] Inspect Leg 1, Leg 2, and Leg 3 passenger arrays in `build_custom_portal.py`
- [x] Replace placeholders in Leg 1 (Seat B1-43, B1-40, B1-45, B2-39, etc.) with real names:
  - B1-43 (`M 60`): Md Shami Akhtar (60y)
  - B1-40 (`M 16`): Md Alatamas Khan (16y)
  - B1-45 (`M 19`): Md Shahid Anwar (19y)
  - B2-26 (`M 57`): Mahtab Alam (57y)
  - B2-11 (`M 54`): Md Azad Anwar (54y)
  - B2-37 (`M 47`): Md Maaz Khan (47y)
  - B2-30 (`M 40`): Sarfaraj Khan (40y)
  - B2-29 (`M 44`): Minhaj Khan (44y)
  - B2-48 (`M 29`): Mukhatib Alam (29y)
  - B2-35 (`M 30`): Md Danish Alam (30y)
  - B2-39 (`M 30`): Md Neyaz Anwar (28y)
- [x] Update Leg 2 names and exact ages to match handwritten list:
  - Md Azad Anwar (54y)
  - Sarfaraj Khan (40y)
  - Mukhatib Alam (29y)
  - Tariq Alam (30y) [Joining from New Delhi]
  - Sync all 24 ages
- [x] Clean up Leg 3 to reflect realistic return without forcing placeholders
- [x] Rebuild HTML files with `python3 make_companion.py`
- [x] Verify zero diff between `baraat_travel_companion.html` and `index.html`
- [x] Test and visually verify with Selenium screenshots
- [x] Commit, push to `origin/main`, and confirm GitHub Pages build

## Review & Results
- **100% Matching**: All 24 delegates from the handwritten list have been verified for exact spelling and ages.
- **Leg 1**: 23 delegates boarding at Gaya + 7 additional family/friends (30 berths confirmed). Md Danish Alam (30y) confirmed in B2-35. Zero placeholders.
- **Leg 2**: All 24 delegates present including Tariq Alam (30y) joining from New Delhi + 8 additional guests (32 seats confirmed in C2 and C3).
- **Leg 3**: 30 seats across 1A (4), B2 (8), 3A waitlist (8), and S4 Sleeper (10). Zero placeholders.
- **Parity**: `baraat_travel_companion.html` and `index.html` have 0 diff.
- **Visuals**: Verified via Selenium headless browser screenshots across all three tabs.
