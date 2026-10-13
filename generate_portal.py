import json

html_template = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>Baraat Travel Companion • Ejaz & Iqura Wedding</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg-primary: #0a110e;
      --bg-surface: #111e19;
      --bg-card: #162620;
      --bg-card-hover: #1c322a;
      --border-color: #274438;
      --border-highlight: #d4af37;
      --text-main: #f0fdf4;
      --text-muted: #94a3b8;
      --text-gold: #f5d77f;
      --gold-primary: #d4af37;
      --gold-gradient: linear-gradient(135deg, #f5d77f 0%, #d4af37 50%, #aa820a 100%);
      --emerald-gradient: linear-gradient(135deg, #0d281e 0%, #164232 100%);
      --accent-green: #10b981;
      --accent-blue: #38bdf8;
      --accent-amber: #f59e0b;
      --radius-sm: 8px;
      --radius-md: 14px;
      --radius-lg: 20px;
      --shadow-soft: 0 10px 30px -10px rgba(0,0,0,0.5);
      --shadow-gold: 0 4px 20px rgba(212, 175, 55, 0.25);
    }

    [data-theme="light"] {
      --bg-primary: #f8faf8;
      --bg-surface: #f0f4f1;
      --bg-card: #ffffff;
      --bg-card-hover: #f3f7f4;
      --border-color: #d1ded5;
      --border-highlight: #b89628;
      --text-main: #13241b;
      --text-muted: #5c6f64;
      --text-gold: #997300;
      --gold-primary: #b89628;
      --gold-gradient: linear-gradient(135deg, #d4af37 0%, #b89628 50%, #8c6d12 100%);
      --emerald-gradient: linear-gradient(135deg, #eaf2ed 0%, #d9e9df 100%);
      --shadow-soft: 0 10px 25px -5px rgba(20, 40, 30, 0.08);
      --shadow-gold: 0 4px 15px rgba(184, 150, 40, 0.2);
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-tap-highlight-color: transparent;
    }

    body {
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      background-color: var(--bg-primary);
      color: var(--text-main);
      line-height: 1.5;
      min-height: 100vh;
      overflow-x: hidden;
    }

    /* Header Banner */
    .hero-header {
      background: var(--emerald-gradient);
      border-bottom: 1px solid var(--border-color);
      padding: 32px 20px 24px;
      position: relative;
      overflow: hidden;
    }

    .hero-header::before {
      content: "";
      position: absolute;
      top: -50%;
      right: -20%;
      width: 400px;
      height: 400px;
      background: radial-gradient(circle, rgba(212, 175, 55, 0.15) 0%, transparent 70%);
      pointer-events: none;
    }

    .container {
      max-width: 1200px;
      margin: 0 auto;
      padding: 0 16px;
    }

    .top-bar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 20px;
    }

    .badge-royal {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 6px 14px;
      border-radius: 9999px;
      background: rgba(212, 175, 55, 0.15);
      border: 1px solid rgba(212, 175, 55, 0.35);
      color: var(--text-gold);
      font-size: 0.8rem;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .theme-toggle-btn {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      color: var(--text-main);
      padding: 8px 14px;
      border-radius: 9999px;
      cursor: pointer;
      font-size: 0.85rem;
      font-weight: 600;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s ease;
    }
    .theme-toggle-btn:hover {
      border-color: var(--gold-primary);
    }

    .wedding-title {
      font-family: 'Cinzel', serif;
      font-size: clamp(1.8rem, 4vw, 2.8rem);
      font-weight: 700;
      letter-spacing: 0.02em;
      background: var(--gold-gradient);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      margin-bottom: 6px;
      line-height: 1.2;
    }

    .wedding-subtitle {
      color: var(--text-muted);
      font-size: clamp(0.95rem, 2vw, 1.1rem);
      margin-bottom: 20px;
    }

    /* Countdown Grid */
    .countdown-bar {
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      padding: 14px 18px;
      border-radius: var(--radius-md);
      box-shadow: var(--shadow-soft);
      align-items: center;
      justify-content: space-between;
    }

    .countdown-timer {
      display: flex;
      gap: 12px;
      align-items: center;
    }

    .time-unit {
      text-align: center;
      min-width: 48px;
    }

    .time-num {
      font-size: 1.4rem;
      font-weight: 700;
      color: var(--gold-primary);
      display: block;
      line-height: 1.1;
    }

    .time-label {
      font-size: 0.65rem;
      text-transform: uppercase;
      color: var(--text-muted);
      font-weight: 600;
    }

    .quick-stats {
      display: flex;
      gap: 14px;
      font-size: 0.85rem;
      color: var(--text-muted);
      flex-wrap: wrap;
    }

    .stat-pill {
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .stat-pill strong {
      color: var(--text-main);
    }

    /* Sticky Search & Navigation Bar */
    .sticky-nav-container {
      position: sticky;
      top: 0;
      z-index: 100;
      background: var(--bg-surface);
      border-bottom: 1px solid var(--border-color);
      box-shadow: var(--shadow-soft);
      padding: 12px 0;
      backdrop-filter: blur(12px);
    }

    .search-row {
      display: flex;
      gap: 10px;
      margin-bottom: 12px;
    }

    .search-box-wrapper {
      position: relative;
      flex: 1;
    }

    .search-input {
      width: 100%;
      background: var(--bg-card);
      border: 1.5px solid var(--border-color);
      padding: 12px 16px 12px 42px;
      border-radius: var(--radius-md);
      color: var(--text-main);
      font-size: 0.95rem;
      outline: none;
      transition: all 0.2s ease;
    }

    .search-input:focus {
      border-color: var(--gold-primary);
      box-shadow: 0 0 0 3px rgba(212, 175, 55, 0.2);
    }

    .search-icon {
      position: absolute;
      left: 14px;
      top: 50%;
      transform: translateY(-50%);
      color: var(--gold-primary);
      font-size: 1.1rem;
      pointer-events: none;
    }

    .clear-search-btn {
      position: absolute;
      right: 12px;
      top: 50%;
      transform: translateY(-50%);
      background: none;
      border: none;
      color: var(--text-muted);
      cursor: pointer;
      font-size: 1rem;
      display: none;
    }

    /* Tabs Bar */
    .tabs-bar {
      display: flex;
      gap: 8px;
      overflow-x: auto;
      scrollbar-width: none;
      padding-bottom: 4px;
    }
    .tabs-bar::-webkit-scrollbar {
      display: none;
    }

    .tab-btn {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      color: var(--text-muted);
      padding: 8px 16px;
      border-radius: 9999px;
      font-size: 0.85rem;
      font-weight: 600;
      white-space: nowrap;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s ease;
    }

    .tab-btn:hover {
      color: var(--text-main);
      border-color: var(--border-highlight);
    }

    .tab-btn.active {
      background: var(--gold-gradient);
      color: #0d1e15;
      border-color: transparent;
      font-weight: 700;
      box-shadow: var(--shadow-gold);
    }

    /* Filter Pills */
    .filter-scroll {
      display: flex;
      gap: 8px;
      overflow-x: auto;
      scrollbar-width: none;
      margin-top: 10px;
    }
    .filter-scroll::-webkit-scrollbar {
      display: none;
    }

    .filter-chip {
      background: transparent;
      border: 1px solid var(--border-color);
      color: var(--text-muted);
      padding: 4px 12px;
      border-radius: 9999px;
      font-size: 0.75rem;
      font-weight: 500;
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.15s ease;
    }

    .filter-chip.active, .filter-chip:hover {
      border-color: var(--gold-primary);
      color: var(--text-gold);
      background: rgba(212, 175, 55, 0.1);
    }

    /* Main Tab Content Areas */
    .tab-pane {
      display: none;
      padding: 24px 0 60px;
    }
    .tab-pane.active {
      display: block;
    }

    /* Cards Grid */
    .cards-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
      gap: 16px;
      margin-top: 16px;
    }

    .guest-card {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      padding: 18px;
      box-shadow: var(--shadow-soft);
      transition: transform 0.2s ease, border-color 0.2s ease;
      position: relative;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }

    .guest-card:hover {
      transform: translateY(-3px);
      border-color: var(--border-highlight);
      background: var(--bg-card-hover);
    }

    .card-top {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 12px;
    }

    .guest-name-heading {
      font-size: 1.1rem;
      font-weight: 700;
      color: var(--text-main);
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .guest-meta {
      font-size: 0.8rem;
      color: var(--text-muted);
      margin-top: 2px;
    }

    .relation-tag {
      font-size: 0.7rem;
      font-weight: 600;
      padding: 2px 8px;
      border-radius: 9999px;
      background: rgba(16, 185, 129, 0.15);
      color: #34d399;
      border: 1px solid rgba(16, 185, 129, 0.3);
    }

    /* Journey Legs Mini Grid in Card */
    .leg-summary-box {
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-sm);
      padding: 10px 12px;
      margin-bottom: 8px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .leg-label {
      font-size: 0.75rem;
      font-weight: 600;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.03em;
    }

    .leg-train {
      font-size: 0.85rem;
      font-weight: 700;
      color: var(--text-main);
    }

    .leg-seat-badge {
      text-align: right;
    }

    .seat-pill {
      display: inline-block;
      background: rgba(212, 175, 55, 0.18);
      border: 1px solid rgba(212, 175, 55, 0.4);
      color: var(--text-gold);
      font-weight: 700;
      font-size: 0.85rem;
      padding: 2px 8px;
      border-radius: 6px;
    }

    .berth-type {
      font-size: 0.7rem;
      color: var(--text-muted);
      display: block;
      margin-top: 2px;
    }

    .card-actions {
      display: flex;
      gap: 8px;
      margin-top: 14px;
      padding-top: 12px;
      border-top: 1px solid var(--border-color);
    }

    .btn-action {
      flex: 1;
      padding: 8px 10px;
      border-radius: var(--radius-sm);
      font-size: 0.8rem;
      font-weight: 600;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      transition: all 0.15s ease;
      text-decoration: none;
    }

    .btn-pass {
      background: var(--gold-gradient);
      color: #0d1e15;
      border: none;
    }
    .btn-pass:hover {
      filter: brightness(1.1);
    }

    .btn-wa {
      background: #25D366;
      color: #ffffff;
      border: none;
    }
    .btn-wa:hover {
      background: #1da851;
    }

    .btn-outline {
      background: transparent;
      border: 1px solid var(--border-color);
      color: var(--text-muted);
    }
    .btn-outline:hover {
      color: var(--text-main);
      border-color: var(--border-highlight);
    }

    /* Modal Styles */
    .modal-overlay {
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: rgba(0, 0, 0, 0.75);
      backdrop-filter: blur(6px);
      z-index: 2000;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 16px;
    }

    .modal-overlay.active {
      display: flex;
    }

    .modal-content {
      background: var(--bg-card);
      border: 1px solid var(--gold-primary);
      border-radius: var(--radius-lg);
      max-width: 540px;
      width: 100%;
      max-height: 90vh;
      overflow-y: auto;
      box-shadow: 0 25px 50px -12px rgba(0,0,0,0.7);
      position: relative;
    }

    .modal-close-btn {
      position: absolute;
      top: 16px;
      right: 16px;
      background: rgba(255,255,255,0.1);
      border: none;
      color: var(--text-main);
      width: 32px;
      height: 32px;
      border-radius: 50%;
      cursor: pointer;
      font-size: 1.2rem;
      display: flex;
      align-items: center;
      justify-content: center;
    }

    /* Boarding Pass Styling */
    .boarding-pass-card {
      background: #ffffff;
      color: #0f172a;
      border-radius: var(--radius-lg);
      overflow: hidden;
      box-shadow: var(--shadow-soft);
      position: relative;
    }

    .pass-header {
      background: #0f382a;
      color: #ffffff;
      padding: 20px;
      border-bottom: 2px dashed #cbd5e1;
      position: relative;
    }

    .pass-header h3 {
      font-family: 'Cinzel', serif;
      font-size: 1.3rem;
      color: #f5d77f;
      margin-bottom: 4px;
    }

    .pass-header p {
      font-size: 0.8rem;
      color: #cbd5e1;
    }

    .pass-guest-name {
      font-size: 1.3rem;
      font-weight: 800;
      color: #0f172a;
      padding: 18px 20px 8px;
    }

    .pass-legs-list {
      padding: 0 20px 16px;
    }

    .pass-leg-item {
      border: 1px solid #e2e8f0;
      border-radius: 10px;
      padding: 12px;
      margin-bottom: 10px;
      background: #f8fafc;
    }

    .pass-leg-route {
      display: flex;
      justify-content: space-between;
      font-weight: 700;
      font-size: 0.95rem;
      color: #0f382a;
      margin-bottom: 6px;
    }

    .pass-leg-meta {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 8px;
      font-size: 0.75rem;
      color: #64748b;
    }

    .pass-leg-meta strong {
      display: block;
      color: #0f172a;
      font-size: 0.85rem;
    }

    .pass-barcode-area {
      background: #f1f5f9;
      padding: 16px;
      text-align: center;
      border-top: 2px dashed #cbd5e1;
    }

    .barcode-lines {
      height: 36px;
      background: repeating-linear-gradient(
        90deg,
        #000000 0px,
        #000000 2px,
        transparent 2px,
        transparent 4px,
        #000000 4px,
        #000000 7px,
        transparent 7px,
        transparent 9px
      );
      width: 80%;
      margin: 0 auto 8px;
    }

    /* Timeline Stepper */
    .timeline-container {
      position: relative;
      padding-left: 36px;
      margin-top: 24px;
    }

    .timeline-container::before {
      content: "";
      position: absolute;
      left: 14px;
      top: 10px;
      bottom: 20px;
      width: 3px;
      background: var(--gold-primary);
      opacity: 0.4;
    }

    .timeline-step {
      position: relative;
      margin-bottom: 32px;
    }

    .step-marker {
      position: absolute;
      left: -36px;
      top: 0;
      width: 30px;
      height: 30px;
      border-radius: 50%;
      background: var(--bg-card);
      border: 2px solid var(--gold-primary);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.8rem;
      color: var(--text-gold);
      font-weight: 700;
    }

    .timeline-card {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      padding: 18px 20px;
      box-shadow: var(--shadow-soft);
    }

    .step-title {
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--text-main);
      display: flex;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 8px;
    }

    .step-time-badge {
      background: rgba(212, 175, 55, 0.15);
      color: var(--text-gold);
      padding: 2px 10px;
      border-radius: 9999px;
      font-size: 0.75rem;
      font-weight: 600;
    }

    /* Coach Seating Maps */
    .coach-tabs {
      display: flex;
      gap: 8px;
      overflow-x: auto;
      margin-bottom: 16px;
      padding-bottom: 4px;
    }

    .coach-map-box {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      padding: 20px;
    }

    .seats-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(70px, 1fr));
      gap: 10px;
      margin-top: 14px;
    }

    .seat-cell {
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 10px 6px;
      text-align: center;
      font-size: 0.75rem;
      cursor: pointer;
      transition: all 0.15s ease;
    }

    .seat-cell.occupied {
      background: rgba(16, 185, 129, 0.15);
      border-color: #10b981;
      color: #34d399;
      font-weight: 700;
    }

    .seat-cell.groom {
      background: rgba(212, 175, 55, 0.25);
      border-color: var(--gold-primary);
      color: var(--text-gold);
      box-shadow: var(--shadow-gold);
    }

    .seat-cell:hover {
      transform: scale(1.05);
      border-color: var(--gold-primary);
    }

    /* Emergency Contact Cards */
    .contacts-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
      gap: 16px;
      margin-top: 16px;
    }

    .contact-card {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      padding: 18px;
      display: flex;
      align-items: center;
      gap: 14px;
    }

    .contact-icon {
      width: 44px;
      height: 44px;
      border-radius: 50%;
      background: rgba(212, 175, 55, 0.15);
      color: var(--text-gold);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.2rem;
    }

    .contact-info strong {
      display: block;
      font-size: 0.95rem;
      color: var(--text-main);
    }

    .contact-info span {
      font-size: 0.8rem;
      color: var(--text-muted);
    }

    .call-link {
      color: var(--gold-primary);
      font-weight: 700;
      text-decoration: none;
      display: inline-block;
      margin-top: 4px;
    }

    /* Print Styles */
    @media print {
      .sticky-nav-container, .top-bar, .card-actions, .theme-toggle-btn {
        display: none !important;
      }
      body {
        background: #ffffff !important;
        color: #000000 !important;
      }
      .modal-overlay {
        position: static !important;
        background: none !important;
        display: block !important;
      }
    }
  </style>
</head>
<body data-theme="dark">

  <!-- Header Banner -->
  <header class="hero-header">
    <div class="container">
      <div class="top-bar">
        <div class="badge-royal">
          <span>✨</span> Official Baraat Portal
        </div>
        <button class="theme-toggle-btn" id="themeToggleBtn" onclick="toggleTheme()">
          <span id="themeIcon">☀️</span> <span id="themeText">Light Mode</span>
        </button>
      </div>

      <h1 class="wedding-title">Ejaz & Iqura</h1>
      <p class="wedding-subtitle">Baraat Travel Companion • Gaya Jn ➔ New Delhi ➔ Rudrapur City ➔ Gaya Jn</p>

      <!-- Countdown & Quick Stats -->
      <div class="countdown-bar">
        <div class="countdown-timer">
          <div class="time-unit">
            <span class="time-num" id="cdDays">00</span>
            <span class="time-label">Days</span>
          </div>
          <span style="color:var(--gold-primary);font-weight:bold;">:</span>
          <div class="time-unit">
            <span class="time-num" id="cdHours">00</span>
            <span class="time-label">Hours</span>
          </div>
          <span style="color:var(--gold-primary);font-weight:bold;">:</span>
          <div class="time-unit">
            <span class="time-num" id="cdMinutes">00</span>
            <span class="time-label">Mins</span>
          </div>
          <span style="color:var(--gold-primary);font-weight:bold;">:</span>
          <div class="time-unit">
            <span class="time-num" id="cdSeconds">00</span>
            <span class="time-label">Secs</span>
          </div>
        </div>

        <div class="quick-stats">
          <div class="stat-pill">👥 <strong>30</strong> Travellers</div>
          <div class="stat-pill">🚆 <strong>3</strong> Train Legs</div>
          <div class="stat-pill">📍 <strong>Rudrapur</strong> Venue</div>
          <div class="stat-pill">📞 Helpline <strong>139</strong></div>
        </div>
      </div>
    </div>
  </header>

  <!-- Sticky Nav, Search & Filters -->
  <nav class="sticky-nav-container">
    <div class="container">
      <div class="search-row">
        <div class="search-box-wrapper">
          <span class="search-icon">🔍</span>
          <input type="text" id="searchInput" class="search-input" placeholder="Search by name, coach (C2, C3, M2), seat number, or PNR..." oninput="handleSearch()">
          <button id="clearSearchBtn" class="clear-search-btn" onclick="clearSearch()">✕</button>
        </div>
      </div>

      <!-- Navigation Tabs -->
      <div class="tabs-bar">
        <button class="tab-btn active" onclick="switchTab('roster', this)">👥 All Travellers (<span id="visibleCount">30</span>)</button>
        <button class="tab-btn" onclick="switchTab('timeline', this)">🗺️ Journey Schedule</button>
        <button class="tab-btn" onclick="switchTab('coach', this)">💺 Coach Seating</button>
        <button class="tab-btn" onclick="switchTab('pnr', this)">🎫 PNRs & Tickets</button>
        <button class="tab-btn" onclick="switchTab('wedding', this)">💍 Wedding Programme</button>
        <button class="tab-btn" onclick="switchTab('contacts', this)">📞 Helplines & SOS</button>
      </div>

      <!-- Quick Filter Pills for Roster Tab -->
      <div class="filter-scroll" id="filterPillsRow">
        <button class="filter-chip active" onclick="setFilter('all', this)">All (30)</button>
        <button class="filter-chip" onclick="setFilter('groom', this)">Groom & Family</button>
        <button class="filter-chip" onclick="setFilter('c2', this)">Coach C2 (Shatabdi)</button>
        <button class="filter-chip" onclick="setFilter('c3', this)">Coach C3 (Shatabdi)</button>
        <button class="filter-chip" onclick="setFilter('m2', this)">Coach M2 (Mahabodhi)</button>
        <button class="filter-chip" onclick="setFilter('b1', this)">Coach B1 (Mahabodhi)</button>
        <button class="filter-chip" onclick="setFilter('m3', this)">Coach M3 (Mahabodhi)</button>
        <button class="filter-chip" onclick="setFilter('1a', this)">First AC Return (1A)</button>
      </div>
    </div>
  </nav>

  <!-- Tab Contents -->
  <main class="container">

    <!-- TAB 1: PASSENGER ROSTER -->
    <section id="tab-roster" class="tab-pane active">
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
        <span style="font-size:0.85rem; color:var(--text-muted);">
          Showing <strong id="showingCount" style="color:var(--text-main);">30</strong> travelling guests
        </span>
        <button class="btn-outline" style="padding:4px 12px; font-size:0.75rem; border-radius:9999px; cursor:pointer;" onclick="shareFullListWhatsApp()">
          📲 Share Full List on WhatsApp
        </button>
      </div>

      <div class="cards-grid" id="passengersCardsGrid">
        <!-- Rendered by JavaScript -->
      </div>
    </section>

    <!-- TAB 2: JOURNEY TIMELINE -->
    <section id="tab-timeline" class="tab-pane">
      <div class="timeline-container">

        <!-- Leg 1 -->
        <div class="timeline-step">
          <div class="step-marker">1</div>
          <div class="timeline-card">
            <div class="step-title">
              <span>Gaya Jn ➔ New Delhi (Leg 1)</span>
              <span class="step-time-badge">22-Oct • 14:00 Dep</span>
            </div>
            <p style="color:var(--text-gold); font-weight:600; font-size:0.9rem; margin-top:4px;">
              Train 12397 / MAHABODHI EXP (Superfast)
            </p>
            <p style="font-size:0.85rem; color:var(--text-muted); margin-top:6px;">
              • <strong>Boarding:</strong> Gaya Junction (GAYA) Platform 1 / 2<br>
              • <strong>Departure:</strong> Thursday, 22-Oct-2026 at 14:00 hrs (2:00 PM)<br>
              • <strong>Arrival:</strong> Friday, 23-Oct-2026 at 04:10 hrs (4:10 AM) New Delhi (NDLS)<br>
              • <strong>Coaches:</strong> M2 (18 seats), B1 (9 seats), M3 (3 seats) — Total 30 passengers.
            </p>
          </div>
        </div>

        <!-- Transit Buffer -->
        <div class="timeline-step">
          <div class="step-marker" style="border-color:#38bdf8; color:#38bdf8;">☕</div>
          <div class="timeline-card" style="border-left: 3px solid #38bdf8;">
            <div class="step-title">
              <span>New Delhi Station Transit & Freshen Up</span>
              <span class="step-time-badge" style="background:rgba(56,189,248,0.15); color:#38bdf8;">2h 10m Buffer</span>
            </div>
            <p style="font-size:0.85rem; color:var(--text-muted); margin-top:6px;">
              • <strong>Window:</strong> 04:10 AM to 06:20 AM at New Delhi (NDLS)<br>
              • <strong>Luggage & Gathering:</strong> Group gathers near Platform 1 / Waiting Hall<br>
              • <strong>Breakfast:</strong> Light morning tea at NDLS; full hot breakfast served onboard Shatabdi after departure!<br>
              • <strong>Platform Notice:</strong> Check electronic displays 30 mins prior for Kathgodam Shatabdi platform.
            </p>
          </div>
        </div>

        <!-- Leg 2 -->
        <div class="timeline-step">
          <div class="step-marker">2</div>
          <div class="timeline-card">
            <div class="step-title">
              <span>New Delhi ➔ Rudrapur City (Leg 2)</span>
              <span class="step-time-badge">23-Oct • 06:20 Dep</span>
            </div>
            <p style="color:var(--text-gold); font-weight:600; font-size:0.9rem; margin-top:4px;">
              Train 12040 / KATHGODAM SHATABDI EXPRESS
            </p>
            <p style="font-size:0.85rem; color:var(--text-muted); margin-top:6px;">
              • <strong>Boarding:</strong> New Delhi (NDLS)<br>
              • <strong>Departure:</strong> Friday, 23-Oct-2026 at 06:20 hrs (6:20 AM)<br>
              • <strong>Arrival:</strong> Friday, 23-Oct-2026 at 10:08 hrs (10:08 AM) at Rudrapur City (RUPC)<br>
              • <strong>Class:</strong> AC Chair Car (Coaches C2 and C3)<br>
              • <strong>Catering:</strong> Complimentary hot tea, breakfast & snacks included.
            </p>
          </div>
        </div>

        <!-- Destination Event -->
        <div class="timeline-step">
          <div class="step-marker" style="border-color:#10b981; color:#10b981;">💍</div>
          <div class="timeline-card" style="border-left: 3px solid #10b981;">
            <div class="step-title">
              <span>Rudrapur City Arrival & Nikaah Ceremony</span>
              <span class="step-time-badge" style="background:rgba(16,185,129,0.15); color:#10b981;">Wedding Day!</span>
            </div>
            <p style="font-size:0.85rem; color:var(--text-muted); margin-top:6px;">
              • <strong>Arrival:</strong> 10:08 AM Rudrapur City<br>
              • Reception by Bride's family, transit to guest accommodation<br>
              • Solemnization of <strong>Nikaah of Ejaz & Iqura</strong> in Rudrapur!
            </p>
          </div>
        </div>

        <!-- Return Leg -->
        <div class="timeline-step">
          <div class="step-marker">3</div>
          <div class="timeline-card">
            <div class="step-title">
              <span>Return Journey to Gaya (Night Departure)</span>
              <span class="step-time-badge">24-Oct • 02:35 AM Dep</span>
            </div>
            <p style="color:var(--text-gold); font-weight:600; font-size:0.9rem; margin-top:4px;">
              Train 13010 / DOON EXPRESS
            </p>
            <p style="font-size:0.85rem; color:var(--text-muted); margin-top:6px;">
              • <strong>Boarding Point:</strong> Rampur Junction (RMU) [~45 mins cab from Rudrapur]<br>
              • <strong>Departure:</strong> Late night 23-Oct / Early morning 24-Oct at 02:35 AM<br>
              • <strong>Arrival:</strong> Saturday, 24-Oct-2026 at 20:45 hrs (8:45 PM) at Gaya Jn (GAYA)<br>
              • <strong>Classes:</strong> First AC (1A) and 3A booked.
            </p>
          </div>
        </div>

        <!-- Walima -->
        <div class="timeline-step">
          <div class="step-marker" style="border-color:var(--gold-primary); color:var(--gold-primary);">🎉</div>
          <div class="timeline-card" style="border: 1px solid var(--gold-primary);">
            <div class="step-title">
              <span>Grand Walima Reception (Gaya)</span>
              <span class="step-time-badge">25-Oct • 08:00 PM</span>
            </div>
            <p style="font-size:0.85rem; color:var(--text-muted); margin-top:6px;">
              • <strong>Venue:</strong> Palm Garden, Gaya - 823001<br>
              • <strong>Time:</strong> Sunday, 25-Oct-2026, 8:00 PM Onwards<br>
              • Hosted with love by the Anwar Family.
            </p>
          </div>
        </div>

      </div>
    </section>

    <!-- TAB 3: COACH SEATING LAYOUTS -->
    <section id="tab-coach" class="tab-pane">
      <div class="coach-tabs">
        <button class="tab-btn active" onclick="switchCoachView('c2', this)">Coach C2 (Shatabdi CC)</button>
        <button class="tab-btn" onclick="switchCoachView('c3', this)">Coach C3 (Shatabdi CC)</button>
        <button class="tab-btn" onclick="switchCoachView('m2', this)">Coach M2 (Mahabodhi 3E)</button>
        <button class="tab-btn" onclick="switchCoachView('b1', this)">Coach B1 (Mahabodhi 3A)</button>
        <button class="tab-btn" onclick="switchCoachView('m3', this)">Coach M3 (Mahabodhi 3E)</button>
      </div>

      <div class="coach-map-box">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
          <div>
            <h3 id="currentCoachTitle" style="font-size:1.1rem; color:var(--text-gold);">Coach C2 (Kathgodam Shatabdi)</h3>
            <span style="font-size:0.8rem; color:var(--text-muted);" id="currentCoachSubtitle">Groom's core cluster • Seats 33, 34, 40-45</span>
          </div>
          <div style="display:flex; gap:10px; font-size:0.75rem;">
            <span style="display:flex; align-items:center; gap:4px;"><span style="width:10px; height:10px; border-radius:2px; background:#10b981; display:inline-block;"></span> Booked</span>
            <span style="display:flex; align-items:center; gap:4px;"><span style="width:10px; height:10px; border-radius:2px; background:#d4af37; display:inline-block;"></span> Groom</span>
          </div>
        </div>

        <div class="seats-grid" id="coachSeatsGrid">
          <!-- Rendered by JavaScript -->
        </div>
      </div>
    </section>

    <!-- TAB 4: PNRS & TICKETS -->
    <section id="tab-pnr" class="tab-pane">
      <h3 style="font-size:1.2rem; color:var(--text-gold); margin-bottom:14px;">All Journey PNRs & Live Status</h3>
      <p style="font-size:0.85rem; color:var(--text-muted); margin-bottom:16px;">
        Click any PNR to view current booking & charting status directly:
      </p>

      <div style="display:grid; grid-template-columns:repeat(auto-fill, minmax(300px, 1fr)); gap:14px;" id="pnrListGrid">
        <!-- Rendered by JavaScript -->
      </div>
    </section>

    <!-- TAB 5: WEDDING PROGRAMME -->
    <section id="tab-wedding" class="tab-pane">
      <div class="timeline-card" style="margin-bottom:18px;">
        <h3 style="font-family:'Cinzel', serif; font-size:1.3rem; color:var(--gold-primary); margin-bottom:6px;">
          Wedding Celebrations • Ejaz & Iqura
        </h3>
        <p style="font-size:0.85rem; color:var(--text-muted);">
          "And We have created you in pairs." (Al Quran 78:8)
        </p>
      </div>

      <div style="display:grid; grid-template-columns:repeat(auto-fill, minmax(280px, 1fr)); gap:16px;">
        <div class="timeline-card">
          <div class="step-time-badge">20-Oct-2026 • 08:00 AM</div>
          <h4 style="font-size:1.1rem; color:var(--text-main); margin-top:8px;">Milad-Un-Nabi</h4>
          <p style="font-size:0.85rem; color:var(--text-muted); margin-top:4px;">Gaya Residence</p>
        </div>

        <div class="timeline-card">
          <div class="step-time-badge">20-Oct-2026 • After Maghrib</div>
          <h4 style="font-size:1.1rem; color:var(--text-main); margin-top:8px;">Rasm-e-Manjha</h4>
          <p style="font-size:0.85rem; color:var(--text-muted); margin-top:4px;">Gaya Residence</p>
        </div>

        <div class="timeline-card" style="border: 1px solid var(--gold-primary);">
          <div class="step-time-badge" style="background:var(--gold-gradient); color:#0d1e15; font-weight:700;">23-Oct-2026</div>
          <h4 style="font-size:1.1rem; color:var(--gold-primary); margin-top:8px;">The Nikaah (Baraat)</h4>
          <p style="font-size:0.85rem; color:var(--text-muted); margin-top:4px;">Rudrapur City, Uttarakhand</p>
        </div>

        <div class="timeline-card" style="border: 1px solid var(--accent-green);">
          <div class="step-time-badge" style="background:rgba(16,185,129,0.2); color:#34d399;">25-Oct-2026 • 8:00 PM Onwards</div>
          <h4 style="font-size:1.1rem; color:#34d399; margin-top:8px;">Grand Walima Dinner</h4>
          <p style="font-size:0.85rem; color:var(--text-muted); margin-top:4px;">
            <strong>Palm Garden</strong>, Gaya - 823001
          </p>
        </div>
      </div>
    </section>

    <!-- TAB 6: CONTACTS & SOS -->
    <section id="tab-contacts" class="tab-pane">
      <h3 style="font-size:1.2rem; color:var(--text-gold); margin-bottom:14px;">Emergency & Travel Helplines</h3>
      <div class="contacts-grid">
        <div class="contact-card">
          <div class="contact-icon">🤵</div>
          <div class="contact-info">
            <strong>Groom (Md Ejaz Anwar)</strong>
            <span>Lead Travel Coordinator</span>
            <a href="tel:+919852218098" class="call-link">📞 +91 98522 18098</a>
          </div>
        </div>

        <div class="contact-card">
          <div class="contact-icon">🏠</div>
          <div class="contact-info">
            <strong>Anwar Family (RSVP)</strong>
            <span>Gaya Coordination</span>
            <a href="tel:+919852218098" class="call-link">📞 +91 98522 18098</a>
          </div>
        </div>

        <div class="contact-card">
          <div class="contact-icon">🚂</div>
          <div class="contact-info">
            <strong>Rail Madad 24x7</strong>
            <span>National Railway Enquiry & Help</span>
            <a href="tel:139" class="call-link">📞 139 (Toll Free)</a>
          </div>
        </div>

        <div class="contact-card">
          <div class="contact-icon">🎫</div>
          <div class="contact-info">
            <strong>IRCTC Customer Care</strong>
            <span>E-Ticketing & Cancellation</span>
            <a href="tel:14646" class="call-link">📞 14646</a>
          </div>
        </div>
      </div>
    </section>

  </main>

  <!-- Boarding Pass Modal -->
  <div class="modal-overlay" id="boardingPassModal" onclick="closeModalOnOutsideClick(event)">
    <div class="modal-content" onclick="event.stopPropagation()">
      <button class="modal-close-btn" onclick="closeModal()">✕</button>
      <div id="modalPassBody">
        <!-- Injected by JS -->
      </div>
    </div>
  </div>

  <!-- Edit Name Modal -->
  <div class="modal-overlay" id="editNameModal" onclick="closeEditModalOnOutsideClick(event)">
    <div class="modal-content" style="padding:24px;" onclick="event.stopPropagation()">
      <h3 style="color:var(--text-gold); font-size:1.15rem; margin-bottom:12px;">Edit Guest Name</h3>
      <p style="font-size:0.8rem; color:var(--text-muted); margin-bottom:16px;">
        Update or assign this ticket to a specific family member or friend:
      </p>
      <input type="text" id="editGuestNameInput" class="search-input" style="padding-left:14px; margin-bottom:14px;" placeholder="Full Name">
      <input type="text" id="editGuestRelationInput" class="search-input" style="padding-left:14px; margin-bottom:18px;" placeholder="Relationship / Tag (e.g. Uncle, Friend)">
      <div style="display:flex; gap:10px; justify-content:flex-end;">
        <button class="btn-outline" style="padding:8px 16px; border-radius:var(--radius-sm); cursor:pointer;" onclick="closeEditModal()">Cancel</button>
        <button class="btn-pass" style="padding:8px 18px; border-radius:var(--radius-sm); cursor:pointer;" onclick="saveGuestName()">Save Changes</button>
      </div>
    </div>
  </div>

  <script>
    // PASSENGER DATABASE
    const defaultPassengers = PASSENGER_DATA_PLACEHOLDER;

    // Load custom names from localStorage if available
    let storedCustomNames = {};
    try {
      const saved = localStorage.getItem('baraat_custom_names');
      if (saved) storedCustomNames = JSON.parse(saved);
    } catch(e) {}

    let passengers = defaultPassengers.map(p => {
      if (storedCustomNames[p.id]) {
        return { ...p, name: storedCustomNames[p.id].name, relation: storedCustomNames[p.id].relation || p.relation };
      }
      return p;
    });

    let currentFilter = 'all';
    let currentCoach = 'c2';
    let editingPassengerId = null;

    // Initialize UI
    document.addEventListener('DOMContentLoaded', () => {
      startCountdown();
      renderCards();
      renderCoachSeats('c2');
      renderPNRGrid();
    });

    // Theme Toggle
    function toggleTheme() {
      const body = document.body;
      const current = body.getAttribute('data-theme');
      const newTheme = current === 'dark' ? 'light' : 'dark';
      body.setAttribute('data-theme', newTheme);
      document.getElementById('themeIcon').textContent = newTheme === 'dark' ? '☀️' : '🌙';
      document.getElementById('themeText').textContent = newTheme === 'dark' ? 'Light Mode' : 'Dark Mode';
    }

    // Countdown Timer (Departure: 22-Oct-2026 14:00:00 IST)
    function startCountdown() {
      const depDate = new Date('2026-10-22T14:00:00+05:30').getTime();
      function update() {
        const now = new Date().getTime();
        const diff = depDate - now;
        if (diff <= 0) {
          document.getElementById('cdDays').textContent = '00';
          document.getElementById('cdHours').textContent = '00';
          document.getElementById('cdMinutes').textContent = '00';
          document.getElementById('cdSeconds').textContent = '00';
          return;
        }
        const d = Math.floor(diff / (1000 * 60 * 60 * 24));
        const h = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const m = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
        const s = Math.floor((diff % (1000 * 60)) / 1000);
        document.getElementById('cdDays').textContent = String(d).padStart(2, '0');
        document.getElementById('cdHours').textContent = String(h).padStart(2, '0');
        document.getElementById('cdMinutes').textContent = String(m).padStart(2, '0');
        document.getElementById('cdSeconds').textContent = String(s).padStart(2, '0');
      }
      update();
      setInterval(update, 1000);
    }

    // Tab Switching
    function switchTab(tabId, btn) {
      document.querySelectorAll('.tab-pane').forEach(el => el.classList.remove('active'));
      document.querySelectorAll('.tab-btn').forEach(el => el.classList.remove('active'));
      const target = document.getElementById('tab-' + tabId);
      if (target) target.classList.add('active');
      if (btn) btn.classList.add('active');

      const filterRow = document.getElementById('filterPillsRow');
      if (tabId === 'roster') {
        filterRow.style.display = 'flex';
      } else {
        filterRow.style.display = 'none';
      }
    }

    // Filter Chips
    function setFilter(filter, btn) {
      currentFilter = filter;
      document.querySelectorAll('.filter-chip').forEach(el => el.classList.remove('active'));
      if (btn) btn.classList.add('active');
      handleSearch();
    }

    // Search and Filter logic
    function handleSearch() {
      const q = document.getElementById('searchInput').value.trim().toLowerCase();
      const clearBtn = document.getElementById('clearSearchBtn');
      clearBtn.style.display = q ? 'block' : 'none';

      const filtered = passengers.filter(p => {
        // Query match
        const matchesQuery = !q ||
          p.name.toLowerCase().includes(q) ||
          (p.leg1.coach + p.leg1.seat).toLowerCase().includes(q) ||
          (p.leg2.coach + p.leg2.seat).toLowerCase().includes(q) ||
          p.leg1.pnr.toLowerCase().includes(q) ||
          p.leg2.pnr.toLowerCase().includes(q) ||
          (p.leg1.berth || '').toLowerCase().includes(q) ||
          (p.leg2.berth || '').toLowerCase().includes(q);

        if (!matchesQuery) return false;

        // Filter chip match
        if (currentFilter === 'all') return true;
        if (currentFilter === 'groom') return p.relation.toLowerCase().includes('groom') || p.relation.toLowerCase().includes('father');
        if (currentFilter === 'c2') return p.leg2.coach.toLowerCase() === 'c2';
        if (currentFilter === 'c3') return p.leg2.coach.toLowerCase() === 'c3';
        if (currentFilter === 'm2') return p.leg1.coach.toLowerCase() === 'm2';
        if (currentFilter === 'b1') return p.leg1.coach.toLowerCase() === 'b1';
        if (currentFilter === 'm3') return p.leg1.coach.toLowerCase() === 'm3';
        if (currentFilter === '1a') return p.leg3 && p.leg3.coach.toLowerCase() === '1a';

        return true;
      });

      renderCards(filtered);
      document.getElementById('visibleCount').textContent = filtered.length;
      document.getElementById('showingCount').textContent = filtered.length;
    }

    function clearSearch() {
      document.getElementById('searchInput').value = '';
      document.getElementById('clearSearchBtn').style.display = 'none';
      handleSearch();
    }

    // Render Cards
    function renderCards(list = passengers) {
      const container = document.getElementById('passengersCardsGrid');
      if (list.length === 0) {
        container.innerHTML = `
          <div style="grid-column: 1/-1; text-align:center; padding:40px; color:var(--text-muted);">
            <p style="font-size:1.2rem; margin-bottom:8px;">🔍 No travelling partners found</p>
            <p style="font-size:0.85rem;">Try searching for coach names like "C2", "M2" or clear the search input.</p>
          </div>
        `;
        return;
      }

      container.innerHTML = list.map(p => {
        const isGroom = p.relation.toLowerCase().includes('groom');
        const borderColor = isGroom ? 'border-color: var(--gold-primary);' : '';

        return `
          <div class="guest-card" style="${borderColor}">
            <div>
              <div class="card-top">
                <div>
                  <div class="guest-name-heading">
                    ${p.name}
                  </div>
                  <div class="guest-meta">${p.age} Yrs • ${p.gender === 'M' ? 'Male' : 'Female'} • ${p.relation}</div>
                </div>
                <button onclick="openEditModal('${p.id}')" title="Edit Name" style="background:none; border:none; color:var(--text-muted); cursor:pointer; font-size:0.9rem;">✏️</button>
              </div>

              <!-- Leg 1 Info -->
              <div class="leg-summary-box">
                <div>
                  <div class="leg-label">Leg 1 • Gaya ➔ Delhi</div>
                  <div class="leg-train">${p.leg1.train}</div>
                </div>
                <div class="leg-seat-badge">
                  <span class="seat-pill">${p.leg1.coach} / ${p.leg1.seat}</span>
                  <span class="berth-type">${p.leg1.berth}</span>
                </div>
              </div>

              <!-- Leg 2 Info -->
              <div class="leg-summary-box">
                <div>
                  <div class="leg-label">Leg 2 • Delhi ➔ Rudrapur</div>
                  <div class="leg-train">${p.leg2.train}</div>
                </div>
                <div class="leg-seat-badge">
                  <span class="seat-pill" style="background:rgba(16,185,129,0.18); border-color:rgba(16,185,129,0.4); color:#34d399;">
                    ${p.leg2.coach} / ${p.leg2.seat}
                  </span>
                  <span class="berth-type">${p.leg2.berth}</span>
                </div>
              </div>

              <!-- Leg 3 Info -->
              <div class="leg-summary-box" style="margin-bottom:0;">
                <div>
                  <div class="leg-label">Leg 3 • Return to Gaya</div>
                  <div class="leg-train">${p.leg3.train}</div>
                </div>
                <div class="leg-seat-badge">
                  <span class="seat-pill" style="font-size:0.75rem;">
                    ${p.leg3.coach === '1A' ? '1A Confirmed' : (p.leg3.status === 'WL' ? p.leg3.seat : 'Pending')}
                  </span>
                </div>
              </div>
            </div>

            <div class="card-actions">
              <button class="btn-action btn-pass" onclick="openBoardingPass('${p.id}')">
                🎫 Boarding Pass
              </button>
              <button class="btn-action btn-wa" onclick="shareGuestWhatsApp('${p.id}')">
                📲 WhatsApp
              </button>
            </div>
          </div>
        `;
      }).join('');
    }

    // Coach Seat Layouts
    const coachConfigs = {
      'c2': { title: 'Coach C2 (Kathgodam Shatabdi - CC)', subtitle: 'Chair Car • 78 Seats (Groom Cluster in Seats 33, 34, 40-45)', total: 78 },
      'c3': { title: 'Coach C3 (Kathgodam Shatabdi - CC)', subtitle: 'Chair Car • 78 Seats (Elders & Family)', total: 78 },
      'm2': { title: 'Coach M2 (Mahabodhi Exp - 3E)', subtitle: '3-Tier Economy • 83 Berths', total: 83 },
      'b1': { title: 'Coach B1 (Mahabodhi Exp - 3A)', subtitle: '3-Tier AC • 72 Berths', total: 72 },
      'm3': { title: 'Coach M3 (Mahabodhi Exp - 3E)', subtitle: '3-Tier Economy • 83 Berths', total: 83 }
    };

    function switchCoachView(coachId, btn) {
      currentCoach = coachId;
      document.querySelectorAll('.coach-tabs .tab-btn').forEach(el => el.classList.remove('active'));
      if (btn) btn.classList.add('active');

      const conf = coachConfigs[coachId];
      document.getElementById('currentCoachTitle').textContent = conf.title;
      document.getElementById('currentCoachSubtitle').textContent = conf.subtitle;
      renderCoachSeats(coachId);
    }

    function renderCoachSeats(coachId) {
      const container = document.getElementById('coachSeatsGrid');
      const conf = coachConfigs[coachId];
      const isShatabdi = coachId.startsWith('c');

      // Map occupied seats in this coach
      const seatMap = {};
      passengers.forEach(p => {
        if (isShatabdi && p.leg2.coach.toLowerCase() === coachId) {
          const num = parseInt(p.leg2.seat);
          if (!isNaN(num)) seatMap[num] = p;
        } else if (!isShatabdi && p.leg1.coach.toLowerCase() === coachId) {
          const num = parseInt(p.leg1.seat);
          if (!isNaN(num)) seatMap[num] = p;
        }
      });

      let html = '';
      for (let s = 1; s <= conf.total; s++) {
        const guest = seatMap[s];
        if (guest) {
          const isGroom = guest.relation.toLowerCase().includes('groom');
          html += `
            <div class="seat-cell occupied ${isGroom ? 'groom' : ''}" onclick="openBoardingPass('${guest.id}')" title="${guest.name} (${guest.age})">
              <span style="font-weight:bold; font-size:0.85rem;">#${s}</span>
              <div style="font-size:0.65rem; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">${guest.short_name}</div>
            </div>
          `;
        } else {
          html += `
            <div class="seat-cell" style="opacity:0.35;">
              <span>#${s}</span>
            </div>
          `;
        }
      }
      container.innerHTML = html;
    }

    // PNR Grid
    const pnrData = [
      { pnr: '2957815277', leg: 'Leg 2 (Shatabdi)', coach: 'C3 (6 Seats)', status: 'CNF (Azad Anwar, Sarfaraz Khan, Aklimuddin, Mokhatib, Haider, Amjad)' },
      { pnr: '2361756513', leg: 'Leg 2 (Shatabdi)', coach: 'C3 (6 Seats)', status: 'CNF (Shami Akhtar, Shahil Anwar, Mustaq Alam, Naushad, Nedayur, Alatamas)' },
      { pnr: '2842448764', leg: 'Leg 2 (Shatabdi)', coach: 'C3 (6 Seats)', status: 'CNF (Irfan Alam, Minhaj Khan, Siraj Anwar, Imtiyaz, Maaz Khan, Shahrukh)' },
      { pnr: '2842449153', leg: 'Leg 2 (Shatabdi)', coach: 'C2 (6 Seats)', status: 'CNF (Ejaz Anwar [Groom], Masroor Jahan, Imran, Neyaz, Rizwan, Aftab)' },
      { pnr: '2461846773', leg: 'Leg 2 (Shatabdi)', coach: 'C2 (2 Seats)', status: 'CNF (Md Tarique, Ejaz Khan)' },
      { pnr: '650-8443973', leg: 'Leg 1 (Mahabodhi)', coach: 'M2 (6 Berths)', status: 'CNF (Seats 9, 10, 11, 12, 13, 14)' },
      { pnr: '640-8444042', leg: 'Leg 1 (Mahabodhi)', coach: 'M2 (6 Berths)', status: 'CNF (Seats 26, 27, 29, 30, 32, 48)' },
      { pnr: '654-8443673', leg: 'Leg 1 (Mahabodhi)', coach: 'M2 (6 Berths)', status: 'CNF (Seats 34, 35, 37, 38, 39, 40)' },
      { pnr: '694-8548028', leg: 'Leg 1 (Mahabodhi)', coach: 'B1 (6 Berths)', status: 'CNF (Seats 34, 35, 37, 38, 40, 16)' },
      { pnr: '660-8443705', leg: 'Leg 1 (Mahabodhi)', coach: 'B1 (3 Berths)', status: 'CNF (Seats 42, 43, 45)' },
      { pnr: '6208461284', leg: 'Leg 1 (Mahabodhi)', coach: 'M3 (3 Berths)', status: 'CNF (Shahrukh Khan, Imran Khan, Neyaz Apsar)' },
      { pnr: '2623649572', leg: 'Leg 3 (Doon Exp)', coach: '1A (2 Seats)', status: 'CNF (Sohail Akhtar, Azad Anwar - MMT)' },
      { pnr: '2461735759', leg: 'Leg 3 (Doon Exp)', coach: '1A (2 Seats)', status: 'CNF (Md Maaz Khan, Md Mustaq Alam - Rampur Boarding)' },
      { pnr: '2842426597', leg: 'Leg 3 (Doon Exp)', coach: '3A (5 Seats)', status: 'WL 243-247 (Amjad, Mustaq, Shahil, Shami, Maaz Khan)' }
    ];

    function renderPNRGrid() {
      const container = document.getElementById('pnrListGrid');
      container.innerHTML = pnrData.map(item => `
        <div class="timeline-card" style="padding:16px;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
            <strong style="color:var(--text-gold); font-size:1.05rem; letter-spacing:0.02em;">PNR: ${item.pnr}</strong>
            <span class="step-time-badge">${item.coach}</span>
          </div>
          <div style="font-size:0.8rem; color:var(--text-muted); margin-bottom:10px;">
            ${item.leg} • ${item.status}
          </div>
          <a href="https://www.confirmtkt.com/pnr-status/${item.pnr.replace('-', '')}" target="_blank" class="btn-action btn-outline" style="font-size:0.75rem; padding:6px 12px; display:inline-flex;">
            🔍 Check Live IRCTC Status ↗
          </a>
        </div>
      `).join('');
    }

    // Boarding Pass Modal
    function openBoardingPass(passengerId) {
      const p = passengers.find(item => item.id === passengerId);
      if (!p) return;

      const body = document.getElementById('modalPassBody');
      body.innerHTML = `
        <div class="boarding-pass-card">
          <div class="pass-header">
            <h3>BARAAT BOARDING PASS</h3>
            <p>Ejaz weds Iqura Wedding Delegation • Gaya ➔ Rudrapur</p>
          </div>

          <div class="pass-guest-name">
            ${p.name}
            <div style="font-size:0.8rem; color:#64748b; font-weight:500;">
              Age: ${p.age} • Gender: ${p.gender === 'M' ? 'Male' : 'Female'} • Status: ${p.relation}
            </div>
          </div>

          <div class="pass-legs-list">
            <!-- Leg 1 -->
            <div class="pass-leg-item">
              <div class="pass-leg-route">
                <span>1. Gaya Jn ➔ New Delhi</span>
                <span>${p.leg1.train}</span>
              </div>
              <div class="pass-leg-meta">
                <div><span>Coach/Seat</span><strong>${p.leg1.coach} / ${p.leg1.seat}</strong></div>
                <div><span>Berth</span><strong>${p.leg1.berth}</strong></div>
                <div><span>PNR</span><strong>${p.leg1.pnr}</strong></div>
              </div>
              <div style="font-size:0.75rem; color:#059669; font-weight:600; margin-top:4px;">
                Dep: 22-Oct 14:00 • Arr: 23-Oct 04:10
              </div>
            </div>

            <!-- Leg 2 -->
            <div class="pass-leg-item" style="border-color:#bbf7d0; background:#f0fdf4;">
              <div class="pass-leg-route">
                <span>2. New Delhi ➔ Rudrapur City</span>
                <span>${p.leg2.train}</span>
              </div>
              <div class="pass-leg-meta">
                <div><span>Coach/Seat</span><strong>${p.leg2.coach} / ${p.leg2.seat}</strong></div>
                <div><span>Berth</span><strong>${p.leg2.berth}</strong></div>
                <div><span>PNR</span><strong>${p.leg2.pnr}</strong></div>
              </div>
              <div style="font-size:0.75rem; color:#059669; font-weight:600; margin-top:4px;">
                Dep: 23-Oct 06:20 • Arr: 23-Oct 10:08 (Breakfast Onboard)
              </div>
            </div>

            <!-- Leg 3 -->
            <div class="pass-leg-item">
              <div class="pass-leg-route">
                <span>3. Return: Rampur ➔ Gaya</span>
                <span>${p.leg3.train}</span>
              </div>
              <div class="pass-leg-meta">
                <div><span>Coach/Seat</span><strong>${p.leg3.coach} / ${p.leg3.seat}</strong></div>
                <div><span>Status</span><strong>${p.leg3.status}</strong></div>
                <div><span>PNR</span><strong>${p.leg3.pnr}</strong></div>
              </div>
              <div style="font-size:0.75rem; color:#059669; font-weight:600; margin-top:4px;">
                Dep: 24-Oct 02:35 AM • Arr: 24-Oct 20:45 Gaya
              </div>
            </div>
          </div>

          <div class="pass-barcode-area">
            <div class="barcode-lines"></div>
            <div style="font-size:0.75rem; color:#64748b; font-family:monospace;">
              *EJAZ-IQURA-BARAAT-${p.id.toUpperCase()}-2026*
            </div>
            <div style="display:flex; gap:10px; margin-top:14px; justify-content:center;">
              <button class="btn-action btn-wa" style="padding:8px 18px; border-radius:8px;" onclick="shareGuestWhatsApp('${p.id}')">
                📲 Send on WhatsApp
              </button>
              <button class="btn-action btn-outline" style="padding:8px 18px; border-radius:8px; border-color:#cbd5e1; color:#0f172a;" onclick="window.print()">
                🖨️ Print Pass
              </button>
            </div>
          </div>
        </div>
      `;

      document.getElementById('boardingPassModal').classList.add('active');
    }

    function closeModal() {
      document.getElementById('boardingPassModal').classList.remove('active');
    }

    function closeModalOnOutsideClick(e) {
      if (e.target.id === 'boardingPassModal') closeModal();
    }

    // Edit Name
    function openEditModal(passengerId) {
      editingPassengerId = passengerId;
      const p = passengers.find(item => item.id === passengerId);
      if (!p) return;

      document.getElementById('editGuestNameInput').value = p.name;
      document.getElementById('editGuestRelationInput').value = p.relation;
      document.getElementById('editNameModal').classList.add('active');
    }

    function closeEditModal() {
      document.getElementById('editNameModal').classList.remove('active');
      editingPassengerId = null;
    }

    function closeEditModalOnOutsideClick(e) {
      if (e.target.id === 'editNameModal') closeEditModal();
    }

    function saveGuestName() {
      if (!editingPassengerId) return;
      const newName = document.getElementById('editGuestNameInput').value.trim();
      const newRelation = document.getElementById('editGuestRelationInput').value.trim();
      if (!newName) return;

      passengers = passengers.map(p => {
        if (p.id === editingPassengerId) {
          return { ...p, name: newName, short_name: newName.split(' ')[0], relation: newRelation || p.relation };
        }
        return p;
      });

      // Save to localStorage
      storedCustomNames[editingPassengerId] = { name: newName, relation: newRelation };
      try {
        localStorage.setItem('baraat_custom_names', JSON.stringify(storedCustomNames));
      } catch(e) {}

      closeEditModal();
      handleSearch();
      renderCoachSeats(currentCoach);
    }

    // WhatsApp Sharing
    function shareGuestWhatsApp(passengerId) {
      const p = passengers.find(item => item.id === passengerId);
      if (!p) return;

      const text = `💍 *Baraat Travel Pass • Ejaz weds Iqura*%0A` +
        `👤 *Passenger:* ${p.name} (${p.age} Yrs)%0A%0A` +
        `🚆 *LEG 1: Gaya ➔ New Delhi*%0A` +
        `• Train: ${p.leg1.train}%0A` +
        `• Coach: *${p.leg1.coach}* | Seat: *${p.leg1.seat}* (${p.leg1.berth})%0A` +
        `• Dep: 22-Oct 14:00 (Gaya) ➔ Arr: 23-Oct 04:10 (NDLS)%0A` +
        `• PNR: ${p.leg1.pnr}%0A%0A` +
        `🚆 *LEG 2: New Delhi ➔ Rudrapur City*%0A` +
        `• Train: ${p.leg2.train}%0A` +
        `• Coach: *${p.leg2.coach}* | Seat: *${p.leg2.seat}* (${p.leg2.berth})%0A` +
        `• Dep: 23-Oct 06:20 (NDLS) ➔ Arr: 23-Oct 10:08 (Rudrapur)%0A` +
        `• PNR: ${p.leg2.pnr}%0A%0A` +
        `🚆 *RETURN: Rampur ➔ Gaya*%0A` +
        `• Train: ${p.leg3.train} (24-Oct 02:35 AM)%0A` +
        `• Status: ${p.leg3.coach} / ${p.leg3.seat}%0A%0A` +
        `📞 *Emergency Helpline:* +91 9852218098 / 139`;

      window.open(`https://wa.me/?text=${text}`, '_blank');
    }

    function shareFullListWhatsApp() {
      const summary = `💍 *Baraat Travel Roster Summary (30 Travellers)*%0A` +
        `Gaya ➔ New Delhi ➔ Rudrapur (22-24 Oct 2026)%0A%0A` +
        `*Coaches Summary:*%0A` +
        `• Mahabodhi: M2 (18 pax), B1 (9 pax), M3 (3 pax)%0A` +
        `• Shatabdi: C2 (Groom + 7 pax), C3 (18 pax)%0A` +
        `• Return: Doon Exp from Rampur (1A & 3A)%0A%0A` +
        `Open the travel companion website link to search your name and seat!`;
      window.open(`https://wa.me/?text=${summary}`, '_blank');
    }
  </script>
</body>
</html>
'''

# Load passengers from previous step
from build_portal import passengers

final_html = html_template.replace('PASSENGER_DATA_PLACEHOLDER', json.dumps(passengers))

output_path = "/Users/ejazanwar/Documents/Ejaz's wedding/baraat_travel_portal.html"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(final_html)

print("Created baraat_travel_portal.html successfully!")
print("File size:", len(final_html), "bytes")
