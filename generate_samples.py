import json

with open("/Users/ejazanwar/Documents/Ejaz's wedding/generate_portal.py", "r") as f:
    code = f.read()

from build_portal import passengers

# ==========================================
# 1. SAMPLE 1: THE POCKET BOARDING PASS (PWA / APP STYLE)
# ==========================================
sample1_html = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>Baraat Pass • Mobile Boarding Wallet</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg: #090d16;
      --card-bg: #111827;
      --card-border: #1f2937;
      --accent: #38bdf8;
      --accent-glow: rgba(56, 189, 248, 0.25);
      --text: #f8fafc;
      --text-muted: #94a3b8;
      --green: #10b981;
      --gold: #fbbf24;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: 'Inter', -apple-system, sans-serif;
      background: var(--bg);
      color: var(--text);
      padding: 16px;
      max-width: 520px;
      margin: 0 auto;
      min-height: 100vh;
    }
    .app-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 12px 0 20px;
    }
    .app-brand {
      font-family: 'Space Grotesk', sans-serif;
      font-weight: 700;
      font-size: 1.3rem;
      letter-spacing: -0.02em;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .badge-live {
      background: rgba(16, 185, 129, 0.2);
      color: var(--green);
      border: 1px solid var(--green);
      font-size: 0.7rem;
      padding: 2px 8px;
      border-radius: 9999px;
      font-weight: 700;
    }
    .search-bar-wrap {
      position: sticky;
      top: 10px;
      z-index: 50;
      margin-bottom: 20px;
    }
    .search-input {
      width: 100%;
      background: #1e293b;
      border: 2px solid #334155;
      padding: 14px 18px 14px 44px;
      border-radius: 16px;
      color: #fff;
      font-size: 1rem;
      outline: none;
      box-shadow: 0 10px 25px -5px rgba(0,0,0,0.5);
      transition: all 0.2s;
    }
    .search-input:focus {
      border-color: var(--accent);
      box-shadow: 0 0 0 4px var(--accent-glow);
    }
    .search-icon {
      position: absolute;
      left: 16px;
      top: 50%;
      transform: translateY(-50%);
      font-size: 1.1rem;
      color: var(--text-muted);
    }
    .quick-chips {
      display: flex;
      gap: 8px;
      overflow-x: auto;
      padding-bottom: 12px;
      margin-bottom: 16px;
      scrollbar-width: none;
    }
    .chip {
      background: #1e293b;
      border: 1px solid #334155;
      color: var(--text-muted);
      padding: 6px 14px;
      border-radius: 9999px;
      font-size: 0.8rem;
      font-weight: 600;
      cursor: pointer;
      white-space: nowrap;
    }
    .chip.active {
      background: var(--accent);
      color: #0f172a;
      border-color: var(--accent);
    }
    .wallet-card {
      background: #ffffff;
      color: #0f172a;
      border-radius: 24px;
      overflow: hidden;
      margin-bottom: 24px;
      box-shadow: 0 20px 40px -10px rgba(0,0,0,0.6);
      position: relative;
    }
    .card-notch-left, .card-notch-right {
      position: absolute;
      width: 24px;
      height: 24px;
      background: var(--bg);
      border-radius: 50%;
      top: 240px;
      z-index: 5;
    }
    .card-notch-left { left: -12px; }
    .card-notch-right { right: -12px; }
    .card-top {
      background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%);
      color: #ffffff;
      padding: 24px;
    }
    .card-top.groom-top {
      background: linear-gradient(135deg, #065f46 0%, #047857 100%);
    }
    .flight-route {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-top: 14px;
    }
    .stn-code {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 2rem;
      font-weight: 800;
      line-height: 1;
    }
    .stn-city {
      font-size: 0.8rem;
      opacity: 0.85;
      margin-top: 4px;
    }
    .plane-icon {
      font-size: 1.4rem;
      opacity: 0.8;
    }
    .card-middle {
      padding: 20px 24px;
      background: #ffffff;
    }
    .info-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 12px;
      margin-bottom: 16px;
    }
    .info-label {
      font-size: 0.7rem;
      text-transform: uppercase;
      color: #64748b;
      font-weight: 600;
    }
    .info-val {
      font-size: 0.95rem;
      font-weight: 700;
      color: #0f172a;
      margin-top: 2px;
    }
    .leg-badge-box {
      border: 1px dashed #cbd5e1;
      border-radius: 12px;
      padding: 12px;
      background: #f8fafc;
      margin-bottom: 12px;
    }
    .leg-badge-header {
      display: flex;
      justify-content: space-between;
      font-size: 0.75rem;
      font-weight: 700;
      color: #0284c7;
      margin-bottom: 4px;
    }
    .card-bottom {
      background: #f1f5f9;
      padding: 18px 24px;
      border-top: 2px dashed #cbd5e1;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }
    .barcode-sim {
      height: 42px;
      background: repeating-linear-gradient(90deg, #0f172a 0px, #0f172a 2px, transparent 2px, transparent 5px, #0f172a 5px, #0f172a 9px);
      border-radius: 4px;
    }
    .btn-wa-pass {
      background: #25D366;
      color: #ffffff;
      border: none;
      padding: 12px;
      border-radius: 12px;
      font-weight: 700;
      font-size: 0.9rem;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      width: 100%;
      text-decoration: none;
    }
  </style>
</head>
<body>

  <header class="app-header">
    <div class="app-brand">
      🎫 <span>Baraat Pass</span>
    </div>
    <span class="badge-live">LIVE DEPLOYMENT</span>
  </header>

  <div class="search-bar-wrap">
    <span class="search-icon">🔍</span>
    <input type="text" id="qInput" class="search-input" placeholder="Type your name or seat..." oninput="filterWallet()">
  </div>

  <div class="quick-chips">
    <button class="chip active" onclick="setChip('all', this)">All (30)</button>
    <button class="chip" onclick="setChip('c2', this)">Coach C2</button>
    <button class="chip" onclick="setChip('c3', this)">Coach C3</button>
    <button class="chip" onclick="setChip('m2', this)">Coach M2</button>
    <button class="chip" onclick="setChip('b1', this)">Coach B1</button>
  </div>

  <div id="walletList"></div>

  <script>
    const passengers = PASSENGER_DATA;
    let currentChip = 'all';

    function renderWallet(list = passengers) {
      const container = document.getElementById('walletList');
      if (!list.length) {
        container.innerHTML = '<div style="text-align:center; padding:40px; color:#64748b;">No boarding pass found</div>';
        return;
      }
      container.innerHTML = list.map(p => {
        const isGroom = p.relation.toLowerCase().includes('groom');
        return `
          <div class="wallet-card">
            <div class="card-notch-left"></div>
            <div class="card-notch-right"></div>

            <div class="card-top ${isGroom ? 'groom-top' : ''}">
              <div style="display:flex; justify-content:space-between; align-items:center; font-size:0.8rem; opacity:0.9;">
                <span>WEDDING TRAVEL PASS</span>
                <span>${p.relation.toUpperCase()}</span>
              </div>
              <div class="flight-route">
                <div>
                  <div class="stn-code">GAYA</div>
                  <div class="stn-city">Gaya Jn • 14:00</div>
                </div>
                <div class="plane-icon">➔ 🚆 ➔</div>
                <div style="text-align:right;">
                  <div class="stn-code">RUPC</div>
                  <div class="stn-city">Rudrapur • 10:08</div>
                </div>
              </div>
            </div>

            <div class="card-middle">
              <div style="margin-bottom:14px;">
                <div style="font-size:0.75rem; color:#64748b; text-transform:uppercase;">Passenger Name</div>
                <div style="font-size:1.25rem; font-weight:800; color:#0f172a;">${p.name}</div>
              </div>

              <!-- Leg 1 Mini -->
              <div class="leg-badge-box">
                <div class="leg-badge-header">
                  <span>LEG 1: MAHABODHI EXP (12397)</span>
                  <span>22-OCT</span>
                </div>
                <div style="display:flex; justify-content:space-between; font-size:0.85rem; font-weight:700;">
                  <span>COACH ${p.leg1.coach} • SEAT ${p.leg1.seat}</span>
                  <span style="color:#0284c7;">${p.leg1.berth}</span>
                </div>
              </div>

              <!-- Leg 2 Mini -->
              <div class="leg-badge-box" style="background:#f0fdf4; border-color:#86efac;">
                <div class="leg-badge-header" style="color:#16a34a;">
                  <span>LEG 2: KATHGODAM SHATABDI (12040)</span>
                  <span>23-OCT</span>
                </div>
                <div style="display:flex; justify-content:space-between; font-size:0.85rem; font-weight:700;">
                  <span>COACH ${p.leg2.coach} • SEAT ${p.leg2.seat}</span>
                  <span style="color:#16a34a;">${p.leg2.berth}</span>
                </div>
              </div>

              <div class="info-grid">
                <div>
                  <div class="info-label">Leg 1 PNR</div>
                  <div class="info-val">${p.leg1.pnr}</div>
                </div>
                <div>
                  <div class="info-label">Leg 2 PNR</div>
                  <div class="info-val">${p.leg2.pnr}</div>
                </div>
                <div>
                  <div class="info-label">Status</div>
                  <div class="info-val" style="color:#16a34a;">CONFIRMED</div>
                </div>
              </div>
            </div>

            <div class="card-bottom">
              <div class="barcode-sim"></div>
              <button class="btn-wa-pass" onclick="sharePass('${p.id}')">
                📲 Send Boarding Pass via WhatsApp
              </button>
            </div>
          </div>
        `;
      }).join('');
    }

    function setChip(c, btn) {
      currentChip = c;
      document.querySelectorAll('.chip').forEach(el => el.classList.remove('active'));
      btn.classList.add('active');
      filterWallet();
    }

    function filterWallet() {
      const q = document.getElementById('qInput').value.trim().toLowerCase();
      const filtered = passengers.filter(p => {
        const matchesQ = !q || p.name.toLowerCase().includes(q) || (p.leg1.coach + p.leg1.seat).toLowerCase().includes(q) || (p.leg2.coach + p.leg2.seat).toLowerCase().includes(q);
        if (!matchesQ) return false;
        if (currentChip === 'all') return true;
        if (currentChip === 'c2') return p.leg2.coach.toLowerCase() === 'c2';
        if (currentChip === 'c3') return p.leg2.coach.toLowerCase() === 'c3';
        if (currentChip === 'm2') return p.leg1.coach.toLowerCase() === 'm2';
        if (currentChip === 'b1') return p.leg1.coach.toLowerCase() === 'b1';
        return true;
      });
      renderWallet(filtered);
    }

    function sharePass(id) {
      const p = passengers.find(x => x.id === id);
      if (!p) return;
      const text = `🎫 *Baraat Boarding Pass • ${p.name}*%0A` +
        `• Leg 1 (Mahabodhi): Coach *${p.leg1.coach}* / Seat *${p.leg1.seat}* (${p.leg1.berth})%0A` +
        `• Leg 2 (Shatabdi): Coach *${p.leg2.coach}* / Seat *${p.leg2.seat}* (${p.leg2.berth})%0A` +
        `• Gaya Departure: 22-Oct 14:00 ➔ Rudrapur: 23-Oct 10:08%0A` +
        `Helpline: +91 9852218098`;
      window.open(`https://wa.me/?text=${text}`, '_blank');
    }

    renderWallet();
  </script>
</body>
</html>'''

# ==========================================
# 2. SAMPLE 2: JOURNEY COMMAND CENTER (OPERATIONS & LOGISTICS)
# ==========================================
sample2_html = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Baraat Operations & Command Center</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700&family=Plus+Jakarta+Sans:wght@400;600;700&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg: #0f172a;
      --panel: #1e293b;
      --border: #334155;
      --primary: #38bdf8;
      --accent: #f59e0b;
      --success: #10b981;
      --text: #f1f5f9;
      --text-dim: #94a3b8;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: 'Plus Jakarta Sans', sans-serif;
      background: var(--bg);
      color: var(--text);
      padding: 24px;
      max-width: 1300px;
      margin: 0 auto;
    }
    .header-ops {
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 2px solid var(--border);
      padding-bottom: 16px;
      margin-bottom: 24px;
    }
    .ops-title {
      font-family: 'JetBrains Mono', monospace;
      font-size: 1.5rem;
      font-weight: 700;
      color: var(--primary);
    }
    .kpi-row {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 16px;
      margin-bottom: 24px;
    }
    .kpi-card {
      background: var(--panel);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 16px;
    }
    .kpi-val {
      font-size: 1.8rem;
      font-weight: 700;
      color: var(--primary);
      font-family: 'JetBrains Mono', monospace;
    }
    .kpi-label {
      font-size: 0.8rem;
      color: var(--text-dim);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }
    .transit-guide-box {
      background: rgba(56, 189, 248, 0.08);
      border: 1px solid var(--primary);
      border-radius: 12px;
      padding: 18px 20px;
      margin-bottom: 24px;
    }
    .transit-guide-box h4 {
      color: var(--primary);
      margin-bottom: 8px;
      font-size: 1.1rem;
    }
    .table-panel {
      background: var(--panel);
      border: 1px solid var(--border);
      border-radius: 12px;
      overflow-x: auto;
      padding: 16px;
    }
    table {
      width: 100%;
      border-collapse: collapse;
      text-align: left;
      font-size: 0.9rem;
    }
    th {
      background: #0f172a;
      color: var(--text-dim);
      padding: 12px;
      border-bottom: 2px solid var(--border);
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.8rem;
    }
    td {
      padding: 12px;
      border-bottom: 1px solid var(--border);
    }
    tr:hover td {
      background: rgba(255,255,255,0.02);
    }
    .badge-cnf {
      background: rgba(16, 185, 129, 0.2);
      color: var(--success);
      padding: 2px 8px;
      border-radius: 4px;
      font-weight: 600;
      font-size: 0.75rem;
    }
    .btn-export {
      background: var(--primary);
      color: #0f172a;
      border: none;
      padding: 8px 16px;
      border-radius: 8px;
      font-weight: 700;
      cursor: pointer;
    }
  </style>
</head>
<body>

  <div class="header-ops">
    <div>
      <div class="ops-title">⚡ BARAAT OPS CONTROL CENTER</div>
      <div style="font-size:0.85rem; color:var(--text-dim);">Flight-Deck Railway Tracking • Gaya ➔ NDLS ➔ Rudrapur City</div>
    </div>
    <button class="btn-export" onclick="window.print()">🖨️ Print Dispatch Roster</button>
  </div>

  <div class="kpi-row">
    <div class="kpi-card">
      <div class="kpi-val">30</div>
      <div class="kpi-label">Manifest Passenger Count</div>
    </div>
    <div class="kpi-card">
      <div class="kpi-val" style="color:var(--success);">100%</div>
      <div class="kpi-label">Leg 1 & Leg 2 Confirmed Seats</div>
    </div>
    <div class="kpi-card">
      <div class="kpi-val" style="color:var(--accent);">02h 10m</div>
      <div class="kpi-label">NDLS Transit Transfer Window</div>
    </div>
    <div class="kpi-card">
      <div class="kpi-val">12040</div>
      <div class="kpi-label">Shatabdi Express Service No.</div>
    </div>
  </div>

  <div class="transit-guide-box">
    <h4>⚠️ CRITICAL TRANSIT PROTOCOL: NEW DELHI RAILWAY STATION (NDLS)</h4>
    <p style="font-size:0.9rem; color:var(--text-dim); line-height:1.6;">
      • <strong>04:10 AM:</strong> Train 12397 arrives at NDLS. All party members congregate at Coach M2 vestibule.<br>
      • <strong>Baggage Staging:</strong> Red-cap porters to transfer 35 luggage units to Platform 1 Executive Waiting Hall.<br>
      • <strong>05:40 AM:</strong> Shatabdi placement on platform. Coach captains to escort family to <strong>Coach C2</strong> (Groom) and <strong>Coach C3</strong>.<br>
      • <strong>06:20 AM:</strong> Sharp departure of 12040. Complimentary catering breakfast served onboard.
    </p>
  </div>

  <div class="table-panel">
    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:14px;">
      <h3 style="font-family:'JetBrains Mono'; font-size:1.1rem;">PASSENGER MANIFEST & COACH ASSIGNMENTS</h3>
      <input type="text" id="filterOps" placeholder="Filter roster..." oninput="filterOpsTable()" style="background:#0f172a; border:1px solid var(--border); color:#fff; padding:6px 12px; border-radius:6px;">
    </div>
    <table id="opsTable">
      <thead>
        <tr>
          <th>#</th>
          <th>PASSENGER NAME</th>
          <th>AGE/GEN</th>
          <th>ROLE</th>
          <th>LEG 1 (MAHABODHI)</th>
          <th>LEG 2 (SHATABDI)</th>
          <th>LEG 3 (RETURN)</th>
          <th>STATUS</th>
        </tr>
      </thead>
      <tbody>
        <!-- JS Injected -->
      </tbody>
    </table>
  </div>

  <script>
    const data = PASSENGER_DATA;

    function renderTable(list = data) {
      const tbody = document.querySelector('#opsTable tbody');
      tbody.innerHTML = list.map((p, i) => `
        <tr>
          <td>${i + 1}</td>
          <td><strong>${p.name}</strong></td>
          <td>${p.age} / ${p.gender}</td>
          <td><span style="color:var(--text-dim); font-size:0.8rem;">${p.relation}</span></td>
          <td><strong>Coach ${p.leg1.coach}</strong> • Berth ${p.leg1.seat} (${p.leg1.berth})</td>
          <td><strong>Coach ${p.leg2.coach}</strong> • Seat ${p.leg2.seat} (${p.leg2.berth})</td>
          <td>${p.leg3.coach === '1A' ? '1A Confirmed' : p.leg3.seat}</td>
          <td><span class="badge-cnf">CONFIRMED</span></td>
        </tr>
      `).join('');
    }

    function filterOpsTable() {
      const q = document.getElementById('filterOps').value.toLowerCase();
      renderTable(data.filter(p => p.name.toLowerCase().includes(q) || p.leg1.coach.toLowerCase().includes(q) || p.leg2.coach.toLowerCase().includes(q)));
    }

    renderTable();
  </script>
</body>
</html>'''

# ==========================================
# 3. SAMPLE 3: THE ROYAL WEDDING & BARAAT PORTAL (LUXURY EMERALD & GOLD)
# ==========================================
sample3_html = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>The Royal Baraat Delegation • Ejaz & Iqura</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Pinyon+Script&family=Playfair+Display:ital,wght@0,600;0,800;1,400&family=Plus+Jakarta+Sans:wght@400;500;600&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg: #091a13;
      --card-bg: #10291e;
      --border-gold: #d4af37;
      --text-gold: #f3e5ab;
      --text: #f9fbf9;
      --text-muted: #a3b8ad;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: 'Plus Jakarta Sans', sans-serif;
      background: radial-gradient(circle at 50% 0%, #163d2c 0%, #091a13 70%);
      color: var(--text);
      min-height: 100vh;
      padding: 30px 16px;
    }
    .royal-container {
      max-width: 900px;
      margin: 0 auto;
    }
    .bismillah {
      text-align: center;
      font-size: 1.6rem;
      color: var(--border-gold);
      letter-spacing: 0.1em;
      margin-bottom: 12px;
    }
    .royal-header {
      text-align: center;
      border: 1px solid rgba(212, 175, 55, 0.4);
      padding: 36px 20px;
      border-radius: 20px;
      background: rgba(16, 41, 30, 0.7);
      backdrop-filter: blur(10px);
      box-shadow: 0 15px 40px rgba(0,0,0,0.5);
      margin-bottom: 30px;
      position: relative;
    }
    .royal-header::before {
      content: "⚜️";
      position: absolute;
      top: -16px;
      left: 50%;
      transform: translateX(-50%);
      background: #091a13;
      padding: 0 12px;
      font-size: 1.2rem;
    }
    .royal-title {
      font-family: 'Playfair Display', serif;
      font-size: clamp(2.2rem, 5vw, 3.4rem);
      font-weight: 800;
      color: var(--border-gold);
      margin-bottom: 8px;
    }
    .royal-script {
      font-family: 'Pinyon Script', cursive;
      font-size: clamp(2rem, 4vw, 3rem);
      color: #ffffff;
      line-height: 1;
    }
    .quran-quote {
      font-style: italic;
      color: var(--text-gold);
      font-size: 0.95rem;
      margin-top: 14px;
    }
    .guest-royal-card {
      background: var(--card-bg);
      border: 1px solid rgba(212, 175, 55, 0.35);
      border-radius: 16px;
      padding: 20px;
      margin-bottom: 16px;
      box-shadow: 0 10px 25px rgba(0,0,0,0.3);
      display: flex;
      flex-direction: column;
      gap: 12px;
    }
    .guest-royal-top {
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid rgba(212, 175, 55, 0.2);
      padding-bottom: 10px;
    }
    .guest-royal-name {
      font-family: 'Playfair Display', serif;
      font-size: 1.3rem;
      color: #ffffff;
    }
    .journey-duo {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 12px;
    }
    .journey-box {
      background: rgba(0,0,0,0.25);
      border: 1px solid rgba(212, 175, 55, 0.2);
      border-radius: 10px;
      padding: 12px;
    }
    .box-heading {
      font-size: 0.75rem;
      text-transform: uppercase;
      color: var(--border-gold);
      font-weight: 600;
      margin-bottom: 4px;
    }
    .btn-royal-wa {
      background: linear-gradient(135deg, #d4af37 0%, #aa820a 100%);
      color: #091a13;
      border: none;
      padding: 10px;
      border-radius: 8px;
      font-weight: 700;
      cursor: pointer;
      text-align: center;
      text-decoration: none;
    }
  </style>
</head>
<body>

  <div class="royal-container">
    <div class="bismillah">بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ</div>

    <div class="royal-header">
      <div style="font-size:0.85rem; letter-spacing:0.15em; text-transform:uppercase; color:var(--border-gold); margin-bottom:8px;">
        The Anwar Family Welcomes The Honoured Baraatis
      </div>
      <h1 class="royal-title">The Baraat Delegation</h1>
      <div class="royal-script">Ejaz & Iqura</div>
      <p class="quran-quote">"And We have created you in pairs." (Al Quran 78:8)</p>
      <div style="margin-top:14px; font-size:0.85rem; color:var(--text-muted);">
        Journey to Rudrapur City (22-23 Oct) • Walima at Palm Garden, Gaya (25 Oct)
      </div>
    </div>

    <div style="margin-bottom:20px;">
      <input type="text" id="royalSearch" placeholder="Search honoured guest by name..." oninput="filterRoyal()" style="width:100%; padding:14px 18px; border-radius:12px; background:var(--card-bg); border:1px solid rgba(212, 175, 55, 0.4); color:#fff; font-size:1rem; outline:none;">
    </div>

    <div id="royalGuestList"></div>
  </div>

  <script>
    const guests = PASSENGER_DATA;

    function renderRoyal(list = guests) {
      const container = document.getElementById('royalGuestList');
      container.innerHTML = list.map(g => `
        <div class="guest-royal-card">
          <div class="guest-royal-top">
            <div>
              <div class="guest-royal-name">${g.name}</div>
              <div style="font-size:0.8rem; color:var(--text-muted);">${g.relation} • Age ${g.age}</div>
            </div>
            <div style="color:var(--border-gold); font-weight:bold; font-size:0.9rem;">
              ${g.relation.includes('Groom') ? '👑 Groom' : '✨ Baraati'}
            </div>
          </div>

          <div class="journey-duo">
            <div class="journey-box">
              <div class="box-heading">Leg 1 • Mahabodhi Exp</div>
              <div style="font-weight:700; font-size:1rem; color:#fff;">Coach ${g.leg1.coach} / Berth ${g.leg1.seat}</div>
              <div style="font-size:0.75rem; color:var(--text-muted);">${g.leg1.berth} • PNR: ${g.leg1.pnr}</div>
            </div>
            <div class="journey-box">
              <div class="box-heading">Leg 2 • Shatabdi Exp</div>
              <div style="font-weight:700; font-size:1rem; color:#fff;">Coach ${g.leg2.coach} / Seat ${g.leg2.seat}</div>
              <div style="font-size:0.75rem; color:var(--text-muted);">${g.leg2.berth} • PNR: ${g.leg2.pnr}</div>
            </div>
          </div>

          <button class="btn-royal-wa" onclick="shareRoyal('${g.id}')">
            📲 Share Official Travel Card on WhatsApp
          </button>
        </div>
      `).join('');
    }

    function filterRoyal() {
      const q = document.getElementById('royalSearch').value.toLowerCase();
      renderRoyal(guests.filter(g => g.name.toLowerCase().includes(q) || (g.leg1.coach + g.leg1.seat).toLowerCase().includes(q) || (g.leg2.coach + g.leg2.seat).toLowerCase().includes(q)));
    }

    function shareRoyal(id) {
      const g = guests.find(x => x.id === id);
      if (!g) return;
      const text = `⚜️ *Baraat Travel Invitation & Passes • ${g.name}*%0A` +
        `Warm greetings from the Anwar Family!%0A%0A` +
        `🚆 *Train 1 (Gaya ➔ NDLS):* Coach *${g.leg1.coach}*, Berth *${g.leg1.seat}* (${g.leg1.berth})%0A` +
        `🚆 *Train 2 (NDLS ➔ Rudrapur):* Coach *${g.leg2.coach}*, Seat *${g.leg2.seat}* (${g.leg2.berth})%0A` +
        `🎉 *Walima:* Palm Garden, Gaya (25-Oct, 8:00 PM)%0A` +
        `RSVP: +91 9852218098`;
      window.open(`https://wa.me/?text=${text}`, '_blank');
    }

    renderRoyal();
  </script>
</body>
</html>'''

# ==========================================
# 4. MASTER SHOWCASE LAUNCHPAD
# ==========================================
showcase_html = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Baraat Website Ideas Showcase • Ejaz & Iqura</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&family=Cinzel:wght@700&display=swap" rel="stylesheet">
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: 'Plus Jakarta Sans', sans-serif;
      background: #090e17;
      color: #f8fafc;
      padding: 36px 20px;
    }
    .wrap { max-width: 1100px; margin: 0 auto; }
    .header { text-align: center; margin-bottom: 40px; }
    .title {
      font-family: 'Cinzel', serif;
      font-size: 2.5rem;
      background: linear-gradient(135deg, #f5d77f 0%, #d4af37 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      margin-bottom: 10px;
    }
    .grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 24px;
      margin-bottom: 40px;
    }
    .card {
      background: #111827;
      border: 1px solid #1f2937;
      border-radius: 20px;
      padding: 24px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: transform 0.2s, border-color 0.2s;
    }
    .card:hover {
      transform: translateY(-5px);
      border-color: #d4af37;
    }
    .card-badge {
      display: inline-block;
      padding: 4px 10px;
      border-radius: 9999px;
      font-size: 0.75rem;
      font-weight: 700;
      margin-bottom: 12px;
    }
    .btn-open {
      display: block;
      background: linear-gradient(135deg, #d4af37 0%, #b89628 100%);
      color: #090e17;
      font-weight: 700;
      text-align: center;
      padding: 12px;
      border-radius: 12px;
      text-decoration: none;
      margin-top: 20px;
    }
  </style>
</head>
<body>
  <div class="wrap">
    <div class="header">
      <h1 class="title">Baraat Website Ideas Showcase</h1>
      <p style="color:#94a3b8; font-size:1.05rem;">
        3 distinct website concepts built for your 30 travelling guests (Gaya ➔ NDLS ➔ Rudrapur)
      </p>
    </div>

    <div class="grid">
      <!-- Idea 1 -->
      <div class="card">
        <div>
          <span class="card-badge" style="background:rgba(56,189,248,0.2); color:#38bdf8;">OPTION 1 • APP WALLET</span>
          <h2 style="font-size:1.4rem; margin-bottom:8px;">The Pocket Boarding Pass</h2>
          <p style="font-size:0.85rem; color:#94a3b8; line-height:1.6; margin-bottom:14px;">
            A sleek, mobile-first wallet experience. High-speed name search that generates realistic digital boarding passes with barcodes and 1-tap WhatsApp sharing.
          </p>
          <ul style="font-size:0.8rem; color:#cbd5e1; list-style-position:inside; line-height:1.8;">
            <li>⚡ Ultra-fast mobile wallet cards</li>
            <li>📲 Direct individual WhatsApp share buttons</li>
            <li>🎫 Barcode & seat highlights</li>
          </ul>
        </div>
        <a href="sample1_pocket_boarding_pass.html" class="btn-open">🚀 Open Option 1 (App Wallet) ↗</a>
      </div>

      <!-- Idea 2 -->
      <div class="card">
        <div>
          <span class="card-badge" style="background:rgba(245,158,11,0.2); color:#f59e0b;">OPTION 2 • COMMAND CENTER</span>
          <h2 style="font-size:1.4rem; margin-bottom:8px;">Journey Command Center</h2>
          <p style="font-size:0.85rem; color:#94a3b8; line-height:1.6; margin-bottom:14px;">
            Designed for group coordinators and operations. Detailed New Delhi transit survival guide, luggage transfer protocols, and interactive manifest tables.
          </p>
          <ul style="font-size:0.8rem; color:#cbd5e1; list-style-position:inside; line-height:1.8;">
            <li>⏰ 02h 10m NDLS transfer guide</li>
            <li>📋 Printable master dispatch manifest</li>
            <li>💼 Porter and baggage handling staging</li>
          </ul>
        </div>
        <a href="sample2_command_center.html" class="btn-open">🚀 Open Option 2 (Command Center) ↗</a>
      </div>

      <!-- Idea 3 -->
      <div class="card">
        <div>
          <span class="card-badge" style="background:rgba(16,185,129,0.2); color:#34d399;">OPTION 3 • ROYAL WEDDING</span>
          <h2 style="font-size:1.4rem; margin-bottom:8px;">Royal Baraat Portal</h2>
          <p style="font-size:0.85rem; color:#94a3b8; line-height:1.6; margin-bottom:14px;">
            A regal emerald & gold portal blending the wedding ceremony invitations (Nikaah & Palm Garden Walima) with dignified travel credentials for honoured elders.
          </p>
          <ul style="font-size:0.8rem; color:#cbd5e1; list-style-position:inside; line-height:1.8;">
            <li>👑 Matches wedding invitation styling</li>
            <li>🕌 Quranic verses & wedding events integration</li>
            <li>⚜️ Luxury gold invitation travel cards</li>
          </ul>
        </div>
        <a href="sample3_royal_baraat_portal.html" class="btn-open">🚀 Open Option 3 (Royal Portal) ↗</a>
      </div>
    </div>

    <!-- Master Unified Portal -->
    <div style="background:linear-gradient(135deg, #164232 0%, #0d281e 100%); border:1px solid #d4af37; border-radius:20px; padding:28px; text-align:center;">
      <h2 style="font-family:'Cinzel'; font-size:1.8rem; color:#f5d77f; margin-bottom:8px;">
        Unified All-in-One Baraat Portal
      </h2>
      <p style="color:#d1ded5; max-width:650px; margin:0 auto 18px; font-size:0.95rem;">
        The complete flagship version featuring live countdown, 2D interactive coach maps (C2, C3, M2, B1, M3), live PNR tracking, and in-browser guest editing.
      </p>
      <a href="baraat_travel_portal.html" style="display:inline-block; background:linear-gradient(135deg, #f5d77f 0%, #d4af37 100%); color:#091a13; font-weight:800; padding:12px 28px; border-radius:9999px; text-decoration:none; font-size:1.05rem;">
        🌟 Launch Flagship All-in-One Companion ↗
      </a>
    </div>
  </div>
</body>
</html>'''

# Write all files
import json

p_json = json.dumps(passengers)

with open("/Users/ejazanwar/Documents/Ejaz's wedding/sample1_pocket_boarding_pass.html", "w") as f:
    f.write(sample1_html.replace("PASSENGER_DATA", p_json))

with open("/Users/ejazanwar/Documents/Ejaz's wedding/sample2_command_center.html", "w") as f:
    f.write(sample2_html.replace("PASSENGER_DATA", p_json))

with open("/Users/ejazanwar/Documents/Ejaz's wedding/sample3_royal_baraat_portal.html", "w") as f:
    f.write(sample3_html.replace("PASSENGER_DATA", p_json))

with open("/Users/ejazanwar/Documents/Ejaz's wedding/website_options_showcase.html", "w") as f:
    f.write(showcase_html)

print("Generated all 3 sample websites and the master showcase launchpad successfully!")
