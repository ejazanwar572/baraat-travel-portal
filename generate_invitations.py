import os
import base64
import subprocess
from PIL import Image, ImageOps, ImageFilter
import numpy as np

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FONTS_DIR = os.path.join(BASE_DIR, 'fonts')
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')
OUTPUT_DIR = os.path.join(BASE_DIR, 'invitation_variants')
os.makedirs(ASSETS_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

CHROME_BIN = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

def to_base64_font(font_filename):
    path = os.path.join(FONTS_DIR, font_filename)
    if os.path.exists(path):
        with open(path, 'rb') as f:
            return base64.b64encode(f.read()).decode('utf-8')
    return ""

def to_base64_img(img_path):
    if os.path.exists(img_path):
        with open(img_path, 'rb') as f:
            ext = os.path.splitext(img_path)[1].lower().replace('.', '')
            if ext == 'jpg': ext = 'jpeg'
            return f"data:image/{ext};base64," + base64.b64encode(f.read()).decode('utf-8')
    return ""

# Fonts
b64_great_vibes = to_base64_font('Great_Vibes.woff2')
b64_pinyon = to_base64_font('Pinyon_Script.woff2')
b64_playfair = to_base64_font('Playfair_Display.woff2')
b64_alex_brush = to_base64_font('Alex_Brush.woff2')
b64_italianno = to_base64_font('Italianno.woff2')

# Calligraphy
b64_bismillah = to_base64_img(os.path.join(ASSETS_DIR, 'bismillah_exact.png'))
b64_walima = to_base64_img(os.path.join(ASSETS_DIR, 'walima_callig_exact.png'))

# --- STEP 1: Process Refined Physical Studio Cards for Variant 2 ---
def refine_physical_card(in_path, out_path, crop_box, is_green=False):
    im = Image.open(in_path).convert('RGB')
    card = im.crop(crop_box)
    w, h = card.size
    arr = np.array(card, dtype=float)
    
    if is_green:
        backing = np.array([218, 232, 225], dtype=float)
    else:
        backing = np.array([246, 240, 230], dtype=float)
        
    # ONLY clean cutouts in the outer wing columns, strictly keeping central text zone (220 to 620) untouched
    for x1, x2 in [(0, 195), (645, w)]:
        sub = arr[:, x1:x2]
        lum = 0.299 * sub[:,:,0] + 0.587 * sub[:,:,1] + 0.114 * sub[:,:,2]
        is_hole = (lum < 130) | (sub[:,:,0] > sub[:,:,1] + 25) | ((sub[:,:,2] > sub[:,:,0] + 15) & (lum < 150))
        alpha = is_hole[:,:,None].astype(float)
        arr[:, x1:x2] = arr[:, x1:x2] * (1 - alpha) + backing * alpha

    # Trim any dark top ribbon artifact
    for y in range(int(h * 0.045)):
        for x in range(w):
            lum = 0.299 * arr[y,x,0] + 0.587 * arr[y,x,1] + 0.114 * arr[y,x,2]
            if lum < 140:
                arr[y,x] = backing

    # Clip with rounded smooth mask to eliminate ragged edges
    res_im = Image.fromarray(arr.astype(np.uint8))
    res_im.save(out_path, quality=96)
    print(f"Refined physical card: {out_path} ({w}x{h})")

refine_physical_card(
    os.path.join(BASE_DIR, 'wedding_card_1_reception.jpg'),
    os.path.join(ASSETS_DIR, 'card1_studio_refined.jpg'),
    (375, 42, 1210, 875),
    False
)
refine_physical_card(
    os.path.join(BASE_DIR, 'wedding_card_2_programme.jpg'),
    os.path.join(ASSETS_DIR, 'card2_studio_refined.jpg'),
    (365, 36, 1200, 868),
    True
)

b64_card1_clean = to_base64_img(os.path.join(ASSETS_DIR, 'card1_studio_refined.jpg'))
b64_card2_clean = to_base64_img(os.path.join(ASSETS_DIR, 'card2_studio_refined.jpg'))

font_css = f"""
@font-face {{
  font-family: 'Great Vibes Local';
  src: url(data:font/woff2;base64,{b64_great_vibes}) format('woff2');
  font-weight: normal;
  font-style: normal;
}}
@font-face {{
  font-family: 'Pinyon Script Local';
  src: url(data:font/woff2;base64,{b64_pinyon}) format('woff2');
  font-weight: normal;
  font-style: normal;
}}
@font-face {{
  font-family: 'Playfair Display Local';
  src: url(data:font/woff2;base64,{b64_playfair}) format('woff2');
  font-weight: normal;
  font-style: normal;
}}
@font-face {{
  font-family: 'Italianno Local';
  src: url(data:font/woff2;base64,{b64_italianno}) format('woff2');
  font-weight: normal;
  font-style: normal;
}}
"""

# SVG Jali Patterns without percent encoding
svg_jali_sage = """<svg xmlns='http://www.w3.org/2000/svg' width='32' height='32' viewBox='0 0 32 32'>
<rect width='32' height='32' fill='#8faea2'/>
<path d='M16,4 C11,4 11,11 4,11 C4,16 4,21 4,21 C11,21 11,28 16,28 C21,28 21,21 28,21 C28,21 28,16 28,11 C21,11 21,4 16,4 Z' fill='#fffdf9' stroke='#7a9a8e' stroke-width='0.8'/>
<polygon points='0,0 5,0 0,5' fill='#fffdf9' stroke='#7a9a8e' stroke-width='0.8'/>
<polygon points='32,0 27,0 32,5' fill='#fffdf9' stroke='#7a9a8e' stroke-width='0.8'/>
<polygon points='0,32 5,32 0,27' fill='#fffdf9' stroke='#7a9a8e' stroke-width='0.8'/>
<polygon points='32,32 27,32 32,27' fill='#fffdf9' stroke='#7a9a8e' stroke-width='0.8'/>
</svg>"""
b64_jali_sage = "data:image/svg+xml;base64," + base64.b64encode(svg_jali_sage.encode()).decode()

svg_jali_sage_programme = """<svg xmlns='http://www.w3.org/2000/svg' width='32' height='32' viewBox='0 0 32 32'>
<rect width='32' height='32' fill='#84a498'/>
<path d='M16,4 C11,4 11,11 4,11 C4,16 4,21 4,21 C11,21 11,28 16,28 C21,28 21,21 28,21 C28,21 28,16 28,11 C21,11 21,4 16,4 Z' fill='#d9e7e1' stroke='#709084' stroke-width='0.8'/>
<polygon points='0,0 5,0 0,5' fill='#d9e7e1' stroke='#709084' stroke-width='0.8'/>
<polygon points='32,0 27,0 32,5' fill='#d9e7e1' stroke='#709084' stroke-width='0.8'/>
<polygon points='0,32 5,32 0,27' fill='#d9e7e1' stroke='#709084' stroke-width='0.8'/>
<polygon points='32,32 27,32 32,27' fill='#d9e7e1' stroke='#709084' stroke-width='0.8'/>
</svg>"""
b64_jali_programme = "data:image/svg+xml;base64," + base64.b64encode(svg_jali_sage_programme.encode()).decode()

# Elegant Corner Ornamental Flourish SVG
corner_gold_svg = """<svg xmlns='http://www.w3.org/2000/svg' width='50' height='50' viewBox='0 0 50 50' fill='none' stroke='#c2a368' stroke-width='1.5'>
<path d='M4,4 L28,4 M4,4 L4,28 M10,10 L22,10 M10,10 L10,22' stroke-linecap='round'/>
<circle cx='8' cy='8' r='2' fill='#c2a368'/>
<path d='M16,4 C22,12 36,12 44,4' stroke-width='1'/>
<path d='M4,16 C12,22 12,36 4,44' stroke-width='1'/>
</svg>"""
b64_corner_gold = "data:image/svg+xml;base64," + base64.b64encode(corner_gold_svg.encode()).decode()

# Elegant Vintage Peony & Rose Floral Spray SVG
floral_cluster_svg = """<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 120 220' width='120' height='220' fill='none'>
  <g opacity='0.92'>
    <path d='M95,20 C70,30 40,75 50,115 C58,155 30,185 15,200' stroke='#b8995a' stroke-width='1.5' stroke-linecap='round'/>
    <!-- Rose 1 -->
    <circle cx='50' cy='55' r='22' fill='#fbf5ed' stroke='#c2a468' stroke-width='1.3'/>
    <circle cx='50' cy='55' r='15' fill='#f3e7d8' stroke='#b8995a' stroke-width='1'/>
    <circle cx='50' cy='55' r='8' fill='#e2cfba' stroke='#a68444' stroke-width='0.8'/>
    <path d='M40,55 C45,45 55,45 60,55 C55,65 45,65 40,55 Z' fill='#d9c2a7'/>
    <!-- Rose 2 -->
    <circle cx='68' cy='135' r='26' fill='#fbf5ed' stroke='#c2a468' stroke-width='1.3'/>
    <circle cx='68' cy='135' r='18' fill='#f3e7d8' stroke='#b8995a' stroke-width='1'/>
    <circle cx='68' cy='135' r='10' fill='#e2cfba' stroke='#a68444' stroke-width='0.8'/>
    <path d='M58,135 C63,125 73,125 78,135 C73,145 63,145 58,135 Z' fill='#d9c2a7'/>
    <!-- Leaves in sage green -->
    <path d='M28,60 C15,55 8,40 20,30 C32,20 36,45 28,60 Z' fill='#8faea2' stroke='#7a9a8e' stroke-width='0.8'/>
    <path d='M75,95 C88,88 95,72 84,62 C72,52 68,76 75,95 Z' fill='#8faea2' stroke='#7a9a8e' stroke-width='0.8'/>
    <path d='M42,160 C25,165 20,180 32,190 C45,198 52,175 42,160 Z' fill='#8faea2' stroke='#7a9a8e' stroke-width='0.8'/>
    <path d='M95,150 C108,155 112,170 102,178 C90,185 86,168 95,150 Z' fill='#8faea2' stroke='#7a9a8e' stroke-width='0.8'/>
  </g>
</svg>"""
b64_floral_cluster = "data:image/svg+xml;base64," + base64.b64encode(floral_cluster_svg.encode()).decode()


# -------------------------------------------------------------
# BUILD VARIANT 1: Royal Digital Masterpiece (2-Page Folio)
# -------------------------------------------------------------
html_v1 = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Wedding Invitation - Ejaz & Iqura (Royal Digital Masterpiece)</title>
<style>
{font_css}
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{
  background: #251e18;
  font-family: 'Playfair Display Local', 'Cinzel', Georgia, serif;
  color: #382519;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 30px 0;
}}

/* Page Sheet (A4 Portrait at 96 DPI: 794px x 1123px) */
.page-sheet {{
  width: 794px;
  height: 1123px;
  background: radial-gradient(circle at 50% 50%, #faf8f3 0%, #ebe2d3 100%);
  display: flex;
  justify-content: center;
  align-items: center;
  box-shadow: 0 20px 50px rgba(0,0,0,0.5);
  margin-bottom: 40px;
  position: relative;
  page-break-after: always;
}}

/* Outer presentation border */
.sheet-gold-border {{
  position: absolute;
  top: 20px; bottom: 20px; left: 20px; right: 20px;
  border: 1px solid #c9b07d;
  pointer-events: none;
}}
.sheet-gold-border-inner {{
  position: absolute;
  top: 24px; bottom: 24px; left: 24px; right: 24px;
  border: 0.5px solid #dfcfad;
  pointer-events: none;
}}

/* The Wedding Invitation Card Container (matches physical card proportions: 710px x 780px) */
.invitation-card {{
  width: 710px;
  height: 780px;
  border-radius: 6px;
  overflow: hidden;
  display: flex;
  box-shadow: 0 16px 40px rgba(55, 40, 25, 0.25), 0 2px 6px rgba(55, 40, 25, 0.12);
  border: 2px solid #b89c62;
  position: relative;
}}

/* Jali Side Wings */
.card-wing {{
  width: 125px;
  height: 100%;
  position: relative;
  z-index: 2;
}}
.wing-left-cream {{
  background-image: url('{b64_jali_sage}');
  background-size: 32px 32px;
  border-right: 3px double #bda167;
}}
.wing-right-cream {{
  background-image: url('{b64_jali_sage}');
  background-size: 32px 32px;
  border-left: 3px double #bda167;
}}
.wing-left-sage {{
  background-image: url('{b64_jali_programme}');
  background-size: 32px 32px;
  border-right: 3px double #a88d55;
}}
.wing-right-sage {{
  background-image: url('{b64_jali_programme}');
  background-size: 32px 32px;
  border-left: 3px double #a88d55;
}}

/* Center Insert: Card 1 (Reception, Cream) */
.card-center-reception {{
  width: 460px;
  height: 100%;
  background: radial-gradient(circle at 50% 30%, #fffefc 0%, #f7f0e2 100%);
  position: relative;
  z-index: 3;
  padding: 42px 28px 28px;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}}

/* Center Insert: Card 2 (Programme, Sage Green) */
.card-center-programme {{
  width: 460px;
  height: 100%;
  background: radial-gradient(circle at 50% 35%, #e1ebe6 0%, #cee0d7 100%);
  position: relative;
  z-index: 3;
  padding: 38px 28px 25px;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}}

/* Subtle Center Card Hairline Border */
.card-inner-border {{
  position: absolute;
  top: 14px; bottom: 14px; left: 14px; right: 14px;
  border: 1px solid #d4c094;
  pointer-events: none;
}}

/* Floral Overlays on Wings */
.wing-floral-overlay {{
  position: absolute;
  width: 110px;
  height: 200px;
  pointer-events: none;
  z-index: 5;
}}
.wf-tl {{ top: 10px; left: 65px; }}
.wf-br {{ bottom: 10px; right: 65px; transform: rotate(180deg); }}

/* Calligraphy Images */
.callig-bismillah {{
  height: 52px;
  margin-bottom: 12px;
  filter: drop-shadow(0 1px 1px rgba(189,161,103,0.3));
}}
.callig-walima {{
  height: 52px;
  margin-bottom: 10px;
  filter: drop-shadow(0 1px 1px rgba(189,161,103,0.3));
}}

/* Reception Typography */
.sub-invocation {{
  font-size: 11px;
  letter-spacing: 2px;
  font-weight: 600;
  color: #4a3628;
  line-height: 1.5;
  margin-bottom: 16px;
  text-transform: uppercase;
}}
.family-name {{
  font-size: 16px;
  letter-spacing: 3.5px;
  font-weight: 700;
  color: #2b180d;
  margin-bottom: 6px;
  text-transform: uppercase;
}}
.invite-line {{
  font-size: 10.5px;
  letter-spacing: 2px;
  font-weight: 500;
  color: #584334;
  line-height: 1.6;
  margin-bottom: 18px;
  text-transform: uppercase;
}}
.reception-title {{
  font-family: 'Italianno Local', 'Great Vibes Local', cursive;
  font-size: 58px;
  color: #3b2416;
  line-height: 0.9;
  margin-bottom: 4px;
}}
.of-word {{
  font-size: 11px;
  letter-spacing: 3px;
  font-weight: 600;
  color: #725d4e;
  margin-bottom: 10px;
  text-transform: uppercase;
}}
.couple-name {{
  font-family: 'Great Vibes Local', cursive;
  font-size: 78px;
  color: #26140a;
  line-height: 0.95;
  margin: 2px 0;
}}
.parent-tag {{
  font-size: 12px;
  letter-spacing: 2.2px;
  font-weight: 700;
  color: #3e2a1b;
  margin-bottom: 6px;
  text-transform: uppercase;
}}
.ampersand {{
  font-family: 'Playfair Display Local', serif;
  font-style: italic;
  font-size: 32px;
  color: #9c7b45;
  margin: 0;
}}

/* Programme Page Typography */
.insha-allah {{
  font-size: 13px;
  letter-spacing: 3px;
  font-weight: 700;
  color: #26150a;
  margin: 4px 0 14px;
}}
.badge-prog {{
  font-size: 13px;
  letter-spacing: 3.5px;
  font-weight: 700;
  color: #fffdf9;
  background: #382416;
  padding: 4px 20px;
  border-radius: 4px;
  display: inline-block;
  margin-bottom: 14px;
}}
.event-box {{
  margin-bottom: 10px;
}}
.event-date-tag {{
  font-size: 11.5px;
  letter-spacing: 2px;
  font-weight: 700;
  color: #2b1c11;
  margin-bottom: 4px;
  text-transform: uppercase;
}}
.event-title-tag {{
  font-size: 15.5px;
  letter-spacing: 2.2px;
  font-weight: 800;
  color: #1a0e07;
  margin-bottom: 2px;
}}
.event-time-tag {{
  font-size: 12px;
  letter-spacing: 1.5px;
  font-weight: 600;
  color: #483426;
}}
.divider-flourish {{
  font-size: 15px;
  color: #a88a4e;
  margin: 6px 0;
  letter-spacing: 3px;
}}
.walima-box {{
  background: rgba(255,253,249,0.5);
  border: 1px solid #bf9d5c;
  border-radius: 6px;
  padding: 8px 24px;
  margin: 6px 0 14px;
}}
.venue-box {{
  margin-top: 2px;
  margin-bottom: 18px;
}}
.venue-header {{
  font-size: 11.5px;
  letter-spacing: 3px;
  font-weight: 700;
  color: #382315;
  margin-bottom: 2px;
}}
.venue-name {{
  font-size: 16px;
  letter-spacing: 2px;
  font-weight: 800;
  color: #170c06;
  margin-bottom: 1px;
}}
.venue-address {{
  font-size: 11.5px;
  letter-spacing: 1.8px;
  font-weight: 600;
  color: #443123;
}}
.footer-row {{
  width: 100%;
  display: flex;
  justify-content: space-between;
  margin-top: auto;
  border-top: 1px solid #b59f72;
  padding-top: 10px;
}}
.footer-col {{
  font-size: 10px;
  line-height: 1.6;
  letter-spacing: 1.2px;
}}
.footer-left {{ text-align: left; }}
.footer-right {{ text-align: right; }}

@media print {{
  body {{ background: none; padding: 0; }}
  .page-sheet {{ width: 100vw; height: 100vh; margin: 0; box-shadow: none; page-break-after: always; }}
}}
</style>
</head>
<body>

  <!-- PAGE 1: RECEPTION CEREMONY -->
  <div class="page-sheet">
    <div class="sheet-gold-border"></div>
    <div class="sheet-gold-border-inner"></div>

    <div class="invitation-card">
      <div class="card-wing wing-left-cream"></div>
      
      <div class="card-center-reception">
        <div class="card-inner-border"></div>
        
        

        <img src="{b64_bismillah}" class="callig-bismillah" alt="Bismillah">

        <div class="sub-invocation">
          IN THE NAME OF "ALLAH"<br>
          THE MOST BENEFICENT &amp; THE MOST MERCIFUL
        </div>

        <div class="family-name">THE ANWAR FAMILY</div>
        <div class="invite-line">
          CORDIALLY INVITES YOU TO CELEBRATE<br>
          THE AUSPICIOUS OCCASION OF THE
        </div>

        <div class="reception-title">Reception Ceremony</div>
        <div class="of-word">OF</div>

        <div class="couple-name">Ejaz</div>
        <div class="parent-tag">(S/O AZAD ANWAR)</div>

        <div class="ampersand">&amp;</div>

        <div class="couple-name">Iqura</div>
        <div class="parent-tag">(D/O JB. IQBAL AHMED SB.)</div>
      </div>

      <div class="card-wing wing-right-cream"></div>
    </div>
  </div>

  <!-- PAGE 2: PROGRAMME & WALIMA -->
  <div class="page-sheet">
    <div class="sheet-gold-border"></div>
    <div class="sheet-gold-border-inner"></div>

    <div class="invitation-card">
      <div class="card-wing wing-left-sage"></div>

      <div class="card-center-programme">
        <div class="card-inner-border"></div>
        
        

        <img src="{b64_walima}" class="callig-walima" alt="Daawat-e-Walima">

        <div class="sub-invocation">
          KINDLY GRACE THE OCCASION WITH<br>
          YOUR GRACIOUS PRESENCE &amp; BLESS THE COUPLE.
        </div>
        <div class="insha-allah">"INSHA ALLAH"</div>

        <div class="badge-prog">:: PROGRAMME ::</div>

        <div class="event-box">
          <div class="event-date-tag">ON TUESDAY, 20TH OCTOBER 2026</div>
          <div class="event-title-tag">❖ MILAD-UN-NABI ❖</div>
          <div class="event-time-tag">TIME : 08:00 A.M.</div>
          <div class="divider-flourish" style="margin: 3px 0;">&amp;</div>
          <div class="event-title-tag">❖ RASM-E-MANJHA ❖</div>
          <div class="event-time-tag">TIME : 06:30 P.M.</div>
        </div>

        <div class="divider-flourish">❦ ══════ •⊰❂⊱• ══════ ❦</div>

        <div class="walima-box">
          <div class="event-date-tag">ON SUNDAY, 25TH OCTOBER 2026</div>
          <div class="event-title-tag" style="font-size: 18px; color: #3b2416;">❖ WALIMA ❖</div>
          <div class="event-time-tag" style="font-weight: 700;">TIME : 08:00 P.M. ONWARDS</div>
        </div>

        <div class="venue-box">
          <div class="venue-header">:: VENUE ::</div>
          <div class="venue-name">HOTEL PALM GARDEN</div>
          <div class="venue-address">KATARI HILL ROAD, GAYA</div>
        </div>

        <div class="footer-row">
          <div class="footer-col footer-left">
            :: W.B.C.F. ::<br>
            <strong>NEAR &amp; DEAR ONES</strong>
          </div>
          <div class="footer-col footer-right">
            :: R.S.V.P ::<br>
            <strong>ANWAR FAMILY</strong><br>
            CONT. +91-9852218098
          </div>
        </div>

      </div>

      <div class="card-wing wing-right-sage"></div>
    </div>
  </div>

</body>
</html>
"""

path_v1_html = os.path.join(OUTPUT_DIR, 'variant1_royal_digital.html')
with open(path_v1_html, 'w') as f:
    f.write(html_v1)
print(f"Updated {path_v1_html}")


# -------------------------------------------------------------
# BUILD VARIANT 2: Studio Physical Keepsake Folio
# -------------------------------------------------------------
html_v2 = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Wedding Invitation - Studio Physical Folio</title>
<style>
{font_css}
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{
  background: #1e1915;
  font-family: 'Playfair Display Local', Georgia, serif;
  color: #382519;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 30px 0;
}}

/* OPEN FOLIO SPREAD (Side by Side) */
.spread-sheet {{
  width: 1420px;
  height: 960px;
  background: radial-gradient(circle at 50% 50%, #fefcf8 0%, #ebe1d1 100%);
  border: 2px solid #c9b07d;
  border-radius: 8px;
  position: relative;
  overflow: hidden;
  box-shadow: 0 25px 60px rgba(0,0,0,0.6);
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 35px 40px;
  margin-bottom: 40px;
  page-break-after: always;
}}
.spread-header {{
  text-align: center;
  margin-bottom: 20px;
}}
.spread-title {{
  font-size: 26px;
  letter-spacing: 6px;
  font-weight: 700;
  color: #382415;
  text-transform: uppercase;
  margin-bottom: 4px;
}}
.spread-subtitle {{
  font-family: 'Italianno Local', cursive;
  font-size: 38px;
  color: #9c7b45;
}}
.spread-row {{
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 40px;
  width: 100%;
}}
.card-frame {{
  width: 620px;
  height: 720px;
  background: #ffffff;
  border-radius: 6px;
  box-shadow: 0 18px 40px rgba(45, 30, 15, 0.28), 0 2px 6px rgba(45, 30, 15, 0.15);
  border: 1.5px solid #d4c09d;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
}}
.card-frame img {{
  width: 100%;
  height: 100%;
  object-fit: cover;
}}

.border-line-1 {{
  position: absolute;
  top: 15px; bottom: 15px; left: 15px; right: 15px;
  border: 1px solid #c9b07d;
  pointer-events: none;
}}
.border-line-2 {{
  position: absolute;
  top: 19px; bottom: 19px; left: 19px; right: 19px;
  border: 0.5px solid #dfcfad;
  pointer-events: none;
}}

/* 2-PAGE PORTRAIT SEQUENTIAL */
.page-sheet {{
  width: 794px;
  height: 1123px;
  background: radial-gradient(circle at 50% 50%, #fdfbf7 0%, #ede3d2 100%);
  position: relative;
  overflow: hidden;
  box-shadow: 0 20px 50px rgba(0,0,0,0.5);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 40px;
  margin-bottom: 40px;
  page-break-after: always;
}}
.single-frame {{
  width: 660px;
  height: 770px;
  background: #ffffff;
  border-radius: 6px;
  box-shadow: 0 20px 45px rgba(45, 30, 15, 0.28);
  border: 2px solid #cbb58a;
  overflow: hidden;
}}
.single-frame img {{
  width: 100%;
  height: 100%;
  object-fit: cover;
}}

@media print {{
  body {{ background: none; padding: 0; }}
  .spread-sheet {{ width: 100vw; height: 100vh; margin: 0; box-shadow: none; page-break-after: always; }}
  .page-sheet {{ width: 100vw; height: 100vh; margin: 0; box-shadow: none; page-break-after: always; }}
}}
</style>
</head>
<body>

  <!-- SPREAD VIEW (Open Folio) -->
  <div class="spread-sheet">
    <div class="border-line-1"></div>
    <div class="border-line-2"></div>
    <div class="spread-header">
      <div class="spread-title">Wedding Invitation</div>
      <div class="spread-subtitle">Ejaz &amp; Iqura</div>
    </div>
    <div class="spread-row">
      <div class="card-frame">
        <img src="{b64_card1_clean}" alt="Reception Card">
      </div>
      <div class="card-frame">
        <img src="{b64_card2_clean}" alt="Programme Card">
      </div>
    </div>
  </div>

  <!-- PAGE 1: RECEPTION CARD (Portrait) -->
  <div class="page-sheet">
    <div class="border-line-1"></div>
    <div class="border-line-2"></div>
    <div class="single-frame">
      <img src="{b64_card1_clean}" alt="Reception Card">
    </div>
  </div>

  <!-- PAGE 2: PROGRAMME CARD (Portrait) -->
  <div class="page-sheet">
    <div class="border-line-1"></div>
    <div class="border-line-2"></div>
    <div class="single-frame">
      <img src="{b64_card2_clean}" alt="Programme Card">
    </div>
  </div>

</body>
</html>
"""

path_v2_html = os.path.join(OUTPUT_DIR, 'variant2_studio_physical.html')
with open(path_v2_html, 'w') as f:
    f.write(html_v2)
print(f"Updated {path_v2_html}")


# -------------------------------------------------------------
# BUILD VARIANT 3: Royal WhatsApp Mobile Duo
# -------------------------------------------------------------
html_v3 = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Wedding Invitation - WhatsApp Mobile Duo</title>
<style>
{font_css}
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{
  background: #201a14;
  font-family: 'Playfair Display Local', Georgia, serif;
  color: #382519;
  display: flex;
  justify-content: center;
  padding: 25px 0;
}}

/* WhatsApp Mobile Story Ratio (width: 680px, height: 1200px) */
.mobile-card {{
  width: 680px;
  background: #fdfaf3;
  border-radius: 12px;
  box-shadow: 0 20px 55px rgba(0,0,0,0.55);
  border: 3px solid #c9b07d;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  position: relative;
}}

/* Jali Side Accents */
.mobile-jali-left {{
  position: absolute;
  top: 0; bottom: 0; left: 0;
  width: 28px;
  background-image: url('{b64_jali_sage}');
  background-size: 28px 28px;
  border-right: 2px solid #bda167;
  z-index: 2;
}}
.mobile-jali-right {{
  position: absolute;
  top: 0; bottom: 0; right: 0;
  width: 28px;
  background-image: url('{b64_jali_sage}');
  background-size: 28px 28px;
  border-left: 2px solid #bda167;
  z-index: 2;
}}

/* Top Section: Reception Card */
.section-reception {{
  background: radial-gradient(circle at 50% 30%, #fffdfa 0%, #f7f1e5 100%);
  padding: 32px 45px 22px;
  text-align: center;
  position: relative;
  z-index: 3;
  border-bottom: 2px dashed #c9b07d;
}}

/* Bottom Section: Programme Card */
.section-programme {{
  background: radial-gradient(circle at 50% 35%, #e1ebe6 0%, #cedfd6 100%);
  padding: 24px 45px 24px;
  text-align: center;
  position: relative;
  z-index: 3;
}}

.callig-header {{
  height: 46px;
  margin-bottom: 8px;
}}
.sub-tag {{
  font-size: 10px;
  letter-spacing: 2px;
  font-weight: 600;
  color: #4e3827;
  margin-bottom: 12px;
  text-transform: uppercase;
}}
.family-tag {{
  font-size: 15px;
  letter-spacing: 3.5px;
  font-weight: 700;
  color: #2b180d;
  margin-bottom: 4px;
}}
.invite-text {{
  font-size: 9.5px;
  letter-spacing: 1.8px;
  color: #554133;
  margin-bottom: 12px;
  line-height: 1.5;
}}
.reception-cursive {{
  font-family: 'Italianno Local', cursive;
  font-size: 48px;
  color: #3b2416;
  line-height: 0.95;
}}
.couple-script {{
  font-family: 'Great Vibes Local', cursive;
  font-size: 66px;
  color: #2b160b;
  line-height: 1;
  margin: 2px 0;
}}
.parent-names {{
  font-size: 11px;
  letter-spacing: 2px;
  font-weight: 700;
  color: #422f20;
}}
.amp {{
  font-style: italic;
  font-size: 26px;
  color: #9c7b45;
}}

/* Programme Section */
.prog-badge {{
  font-size: 12px;
  letter-spacing: 3px;
  font-weight: 700;
  color: #fffdfa;
  background: #382416;
  padding: 4px 18px;
  border-radius: 4px;
  display: inline-block;
  margin-bottom: 12px;
}}
.event-row {{
  background: rgba(255,255,255,0.45);
  border: 1px solid #bfd3c8;
  border-radius: 6px;
  padding: 8px 16px;
  margin-bottom: 10px;
}}
.date-highlight {{
  font-size: 11px;
  letter-spacing: 2px;
  font-weight: 700;
  color: #2b1c11;
}}
.event-name-bold {{
  font-size: 14px;
  letter-spacing: 2px;
  font-weight: 800;
  color: #1a0e07;
  margin: 2px 0;
}}
.time-bold {{
  font-size: 11.5px;
  font-weight: 600;
  color: #443123;
}}
.walima-highlight {{
  background: rgba(255, 252, 245, 0.75);
  border: 1.5px solid #c2a772;
  border-radius: 6px;
  padding: 10px 16px;
  margin-bottom: 12px;
}}
.venue-container {{
  margin: 8px 0 14px;
}}
.venue-label {{
  font-size: 11px;
  letter-spacing: 2px;
  font-weight: 700;
  color: #422e20;
}}
.venue-title {{
  font-size: 15px;
  letter-spacing: 2px;
  font-weight: 800;
  color: #170c06;
}}
.venue-sub {{
  font-size: 11px;
  letter-spacing: 1.5px;
  color: #483527;
}}
.mobile-footer {{
  display: flex;
  justify-content: space-between;
  border-top: 1px solid #b59f72;
  padding-top: 8px;
  font-size: 9.5px;
  line-height: 1.5;
  letter-spacing: 1px;
}}
</style>
</head>
<body>

  <div class="mobile-card">
    <div class="mobile-jali-left"></div>
    <div class="mobile-jali-right"></div>

    <!-- RECEPTION SECTION -->
    <div class="section-reception">
      <img src="{b64_bismillah}" class="callig-header" alt="Bismillah">
      <div class="sub-tag">IN THE NAME OF "ALLAH" • THE MOST BENEFICENT &amp; MERCIFUL</div>
      <div class="family-tag">THE ANWAR FAMILY</div>
      <div class="invite-text">CORDIALLY INVITES YOU TO CELEBRATE THE AUSPICIOUS OCCASION OF THE</div>
      <div class="reception-cursive">Reception Ceremony</div>
      <div class="sub-tag" style="margin: 2px 0 6px;">OF</div>
      <div class="couple-script">Ejaz</div>
      <div class="parent-names">(S/O AZAD ANWAR)</div>
      <div class="amp">&amp;</div>
      <div class="couple-script">Iqura</div>
      <div class="parent-names">(D/O JB. IQBAL AHMED SB.)</div>
    </div>

    <!-- PROGRAMME & WALIMA SECTION -->
    <div class="section-programme">
      <img src="{b64_walima}" class="callig-header" alt="Walima">
      <div class="sub-tag">KINDLY GRACE THE OCCASION WITH YOUR PRESENCE • "INSHA ALLAH"</div>
      
      <div class="prog-badge">:: PROGRAMME ::</div>

      <div class="event-row">
        <div class="date-highlight">TUESDAY, 20TH OCTOBER 2026</div>
        <div class="event-name-bold">❖ MILAD-UN-NABI ❖</div>
        <div class="time-bold">08:00 A.M.</div>
        <div style="font-size: 12px; color: #a88a4e; margin: 2px 0;">&amp;</div>
        <div class="event-name-bold">❖ RASM-E-MANJHA ❖</div>
        <div class="time-bold">06:30 P.M.</div>
      </div>

      <div class="walima-highlight">
        <div class="date-highlight" style="color: #6d4e1b;">SUNDAY, 25TH OCTOBER 2026</div>
        <div class="event-name-bold" style="font-size: 17px; color: #3b2416;">❖ WALIMA ❖</div>
        <div class="time-bold" style="font-size: 12.5px; font-weight: 700;">08:00 P.M. ONWARDS</div>
      </div>

      <div class="venue-container">
        <div class="venue-label">:: VENUE ::</div>
        <div class="venue-title">HOTEL PALM GARDEN</div>
        <div class="venue-sub">KATARI HILL ROAD, GAYA</div>
      </div>

      <div class="mobile-footer">
        <div style="text-align: left;">
          :: W.B.C.F. ::<br>
          <strong>NEAR &amp; DEAR ONES</strong>
        </div>
        <div style="text-align: right;">
          :: R.S.V.P ::<br>
          <strong>ANWAR FAMILY</strong><br>
          CONT. +91-9852218098
        </div>
      </div>
    </div>

  </div>

</body>
</html>
"""

path_v3_html = os.path.join(OUTPUT_DIR, 'variant3_whatsapp_mobile.html')
with open(path_v3_html, 'w') as f:
    f.write(html_v3)
print(f"Updated {path_v3_html}")


# -------------------------------------------------------------
# COMPILE HIGH QUALITY PDFs
# -------------------------------------------------------------
print("\nRe-compiling PDFs with Chrome Headless...")
variants = [
    ('Variant_1_Royal_Digital_Masterpiece.pdf', path_v1_html),
    ('Variant_2_Studio_Physical_Composite.pdf', path_v2_html),
    ('Variant_3_Royal_WhatsApp_Duo.pdf', path_v3_html)
]

for pdf_name, html_path in variants:
    pdf_out = os.path.join(OUTPUT_DIR, pdf_name)
    cmd = [
        CHROME_BIN,
        '--headless',
        '--disable-gpu',
        '--no-pdf-header-footer',
        f'--print-to-pdf={pdf_out}',
        f'file://{html_path}'
    ]
    subprocess.run(cmd, capture_output=True)
    if os.path.exists(pdf_out):
        print(f" Generated PDF: {pdf_name} ({os.path.getsize(pdf_out):,} bytes)")

# -------------------------------------------------------------
# GENERATE CRISP PNG PREVIEWS
# -------------------------------------------------------------
print("\nGenerating crisp PNG previews...")
previews = [
    ('Variant_1_Page1_Preview.png', path_v1_html, 840, 1160),
    ('Variant_2_Spread_Preview.png', path_v2_html, 1460, 1000),
    ('Variant_3_Mobile_Preview.png', path_v3_html, 720, 1260)
]

for png_name, html_path, w, h in previews:
    png_out = os.path.join(OUTPUT_DIR, png_name)
    cmd = [
        CHROME_BIN,
        '--headless',
        '--disable-gpu',
        f'--screenshot={png_out}',
        f'--window-size={w},{h}',
        f'file://{html_path}'
    ]
    subprocess.run(cmd, capture_output=True)
    if os.path.exists(png_out):
        print(f" Generated PNG: {png_name} ({os.path.getsize(png_out):,} bytes)")

# Copy PDFs to Downloads for 1-click user convenience as well
downloads_dir = os.path.expanduser('~/Downloads')
for pdf_name, _ in variants:
    src_pdf = os.path.join(OUTPUT_DIR, pdf_name)
    dst_pdf = os.path.join(downloads_dir, pdf_name)
    if os.path.exists(src_pdf):
        import shutil
        shutil.copy2(src_pdf, dst_pdf)

print("\nAll files compiled, previews created, and synced to Downloads!")
