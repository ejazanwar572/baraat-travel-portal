# Tasks: Website Color Architecture Revamp (Option 1: Royal Champagne & Rose Blush)

- [x] Inspect existing styling and inline styles in `make_companion.py`
- [x] Update CSS custom properties (:root variables) to Option 1 light luxury palette
- [x] Update component CSS rules (body, header, countdown, journey tabs, tables, coach pills, buttons, modals)
- [x] Update inline styles in JavaScript (e.g., `openLiveTicket()`, groom/father highlight)
- [x] Regenerate `baraat_travel_companion.html`, `baraat_travel_portal.html`, and `index.html`
- [x] Verify zero diff between `baraat_travel_companion.html` and `index.html`
- [x] Visually verify UI across Leg 1, Leg 2, Leg 3, and ticket modal via headless Chrome screenshots
- [x] Commit, push to `origin/main`, and verify GitHub Pages deployment status

## Review & Results
- **Color Palette Revamp Applied**:
  - Replaced heavy dark-green theme (`#07140e`) with Option 1: **Royal Champagne & Rose Blush**.
  - Warm alabaster/milk silk canvas (`#faf7f5` with radial gradient), pure crisp white cards (`#ffffff`), and soft rose-champagne gilded borders (`#eed9d0` / `#ebd8cf`).
  - Headings in deep royal espresso charcoal (`#1e1b18`) and burnished gold (`#b88a2b` / `#946b1d`).
  - Coach pills revamped into high-contrast pastel badges with dark readable text.
  - Ticket modals updated to crisp white container with soft dimmed backdrop and clean ticket display.
- **Verification Completed**:
  - Parity confirmed: 0 diff across `baraat_travel_companion.html`, `baraat_travel_portal.html`, and `index.html`.
  - Visual verification: Headless Chrome screenshots captured and inspected for Leg 1, Leg 2, Leg 3, tables, confirmed modal, and waitlisted live modal.
  - Deployment confirmed: GitHub Pages built successfully (`✓` status).
