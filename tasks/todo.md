# Tasks: Baraat Travel Portal & Ticket Management

- [x] Scan local Documents, Downloads, and Desktop directories for all wedding travel tickets
- [x] Scan Gmail booking confirmations for supplementary tickets and boarding station updates
- [x] Meticulously extract and cross-verify all passenger rosters, PNRs, coaches, and berth assignments
- [x] Present discovered ticket inventory to the user for validation and identify any missing tickets
- [x] Present 2-3 sample website concepts (mobile-first web app with search, journey breakdown, offline access)
- [x] Await user feedback and approval on implementation plan
- [x] Build the interactive Travel Hub web application (`baraat_travel_portal.html`)
- [x] Verify search, filters, mobile responsiveness, and export features

- [x] Update Leg 3 passenger dataset with initial and live Current Status fields and booking references
- [x] Add dynamic table headers to show "Current Status" column for Rudrapur to Gaya (Leg 3)
- [x] Implement interactive "Refresh Live Status" button with real-time API fetch and loading indicator
- [x] Update table row rendering for Leg 3 to show Current Status badges (CNF / GNWL) and booking details
- [x] Verify UI and functionality in browser with screenshot and live testing
- [x] Sync changes to both baraat_travel_companion.html and baraat_travel_portal.html

- [x] Remove 'RESERVED COMPARTMENT' text from coach divider rows in table
- [x] Highlight each Coach No with distinct, vibrant colors (B1, M2, M3, C2, C3, 1A, 3A)
- [x] Rebuild and verify across all 3 journey tabs with screenshot proof

- [x] Update build_custom_portal.py to point Leg 3 & Leg 2 tickets to official PDF and high-res preview images
- [x] Update openLiveTicket in make_companion.py to display the visual ticket copy preview and direct PDF download
- [x] Verify Leg 3 ticket modal in browser with screenshot proof for Md Azad Ahmad (PNR 2623649572)
- [x] Sync changes to both baraat_travel_companion.html and baraat_travel_portal.html

- [ ] Create index.html as an exact mirror of baraat_travel_companion.html
- [ ] Initialize git repo and commit all site assets (index.html, Tickets/, fonts/, favicon.png, manifest.json)
- [ ] Create GitHub remote repository on @ejazanwar572 using gh CLI
- [ ] Configure and enable GitHub Pages on main branch
- [ ] Verify live site deployment and test live URL

## Review & Results
- **Ticket Discovery Complete**: 11 tickets discovered (Gaya ➔ NDLS on Mahabodhi 12397, NDLS ➔ Rudrapur on Shatabdi 12040, and return on Doon Exp 13010).
- **Interactive App Created & Refined**: Synced across `/Users/ejazanwar/Documents/Ejaz's wedding/baraat_travel_companion.html` and `baraat_travel_portal.html`.
- **Leg 3 Dynamic Waitlist & Current Status**:
  - Dynamically displays the **Current Status** column specifically for Rudrapur to Gaya (Train 13010 Doon Express).
  - Confirmed 1A passengers show `✅ CNF`.
  - 3A waitlisted passengers show `⏳ GNWL 72–76` along with their live confirmation probability tags (`55%–76% Chance`).
  - Added dedicated **`🔄 Refresh Live Status`** button with real-time IRCTC API fetch, spinning animation, and automatic timestamping.
  - Ticket modal shows horizontal layout with booking status vs live status comparison and 1-tap live check button.

