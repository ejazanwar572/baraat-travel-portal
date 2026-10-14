import os
import subprocess
import shutil
from PIL import Image

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')
OUTPUT_DIR = os.path.join(BASE_DIR, 'invitation_variants')
DOWNLOADS_DIR = os.path.expanduser('~/Downloads')

CHROME_BIN = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# Base64 encode the perfected cards
import base64
def to_b64(path):
    with open(path, 'rb') as f:
        return "data:image/jpeg;base64," + base64.b64encode(f.read()).decode('utf-8')

b64_c1 = to_b64(os.path.join(ASSETS_DIR, 'card1_studio_perfect.jpg'))
b64_c2 = to_b64(os.path.join(ASSETS_DIR, 'card2_studio_perfect.jpg'))

# Load Italianno font
font_path = os.path.join(BASE_DIR, 'fonts', 'Italianno.woff2')
b64_font = ""
if os.path.exists(font_path):
    with open(font_path, 'rb') as f:
        b64_font = base64.b64encode(f.read()).decode('utf-8')

font_css = f"""
@font-face {{
  font-family: 'Italianno Local';
  src: url(data:font/woff2;base64,{b64_font}) format('woff2');
  font-weight: normal;
  font-style: normal;
}}
"""

# -------------------------------------------------------------
# 1. OPEN FOLIO SPREAD HTML (Side by Side)
# -------------------------------------------------------------
html_spread = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Wedding Invitation - Ejaz & Iqura</title>
<style>
{font_css}
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{
  background: #181410;
  font-family: 'Playfair Display', 'Cinzel', Georgia, serif;
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  padding: 0;
}}
.folio-sheet {{
  width: 1440px;
  height: 960px;
  background: radial-gradient(circle at 50% 50%, #fefcf9 0%, #ebe2d3 100%);
  border: 2px solid #c9b07d;
  position: relative;
  overflow: hidden;
  box-shadow: 0 25px 65px rgba(0,0,0,0.65);
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 30px 40px;
}}
.outer-border {{
  position: absolute;
  top: 14px; bottom: 14px; left: 14px; right: 14px;
  border: 1px solid #c9b07d;
  pointer-events: none;
}}
.inner-border {{
  position: absolute;
  top: 18px; bottom: 18px; left: 18px; right: 18px;
  border: 0.5px solid #dfcfad;
  pointer-events: none;
}}
.folio-header {{
  text-align: center;
  margin-bottom: 20px;
}}
.folio-title {{
  font-size: 24px;
  letter-spacing: 7px;
  font-weight: 700;
  color: #3b271b;
  text-transform: uppercase;
  margin-bottom: 3px;
}}
.folio-couple {{
  font-family: 'Italianno Local', cursive;
  font-size: 40px;
  color: #9c7b45;
  line-height: 1;
}}
.cards-container {{
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 36px;
  width: 100%;
}}
.card-pod {{
  width: 630px;
  height: 730px;
  background: #ffffff;
  border-radius: 6px;
  box-shadow: 0 18px 40px rgba(45, 30, 15, 0.28), 0 2px 6px rgba(45, 30, 15, 0.12);
  border: 1.5px solid #d4c09d;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
}}
.card-pod img {{
  width: 100%;
  height: 100%;
  object-fit: cover;
}}
@media print {{
  body {{ background: none; }}
  .folio-sheet {{ width: 100vw; height: 100vh; box-shadow: none; border: none; padding: 25px 35px; }}
}}
</style>
</head>
<body>
  <div class="folio-sheet">
    <div class="outer-border"></div>
    <div class="inner-border"></div>
    <div class="folio-header">
      <div class="folio-title">Wedding Invitation</div>
      <div class="folio-couple">Ejaz &amp; Iqura</div>
    </div>
    <div class="cards-container">
      <div class="card-pod">
        <img src="{b64_c1}" alt="Reception Card">
      </div>
      <div class="card-pod">
        <img src="{b64_c2}" alt="Programme Card">
      </div>
    </div>
  </div>
</body>
</html>
"""

spread_html_path = os.path.join(OUTPUT_DIR, 'variant2_spread_final.html')
with open(spread_html_path, 'w') as f:
    f.write(html_spread)

# -------------------------------------------------------------
# 2. 2-PAGE PORTRAIT SEQUENTIAL HTML
# -------------------------------------------------------------
html_2page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Wedding Invitation - Ejaz & Iqura</title>
<style>
{font_css}
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{
  background: #181410;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 30px 0;
}}
.portrait-sheet {{
  width: 794px;
  height: 1123px; /* A4 */
  background: radial-gradient(circle at 50% 50%, #fefcf9 0%, #ebe2d3 100%);
  position: relative;
  overflow: hidden;
  box-shadow: 0 20px 50px rgba(0,0,0,0.55);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 40px;
  margin-bottom: 40px;
  page-break-after: always;
}}
.outer-border {{
  position: absolute;
  top: 16px; bottom: 16px; left: 16px; right: 16px;
  border: 1.5px solid #c9b07d;
  pointer-events: none;
}}
.inner-border {{
  position: absolute;
  top: 20px; bottom: 20px; left: 20px; right: 20px;
  border: 0.8px solid #dfcfad;
  pointer-events: none;
}}
.card-frame {{
  width: 660px;
  height: 770px;
  background: #ffffff;
  border-radius: 6px;
  box-shadow: 0 20px 45px rgba(45, 30, 15, 0.28), 0 2px 6px rgba(45, 30, 15, 0.12);
  border: 2px solid #cbb58a;
  overflow: hidden;
}}
.card-frame img {{
  width: 100%;
  height: 100%;
  object-fit: cover;
}}
@media print {{
  body {{ background: none; padding: 0; }}
  .portrait-sheet {{ width: 100vw; height: 100vh; margin: 0; box-shadow: none; border: none; page-break-after: always; }}
}}
</style>
</head>
<body>
  <!-- PAGE 1: RECEPTION -->
  <div class="portrait-sheet">
    <div class="outer-border"></div>
    <div class="inner-border"></div>
    <div class="card-frame">
      <img src="{b64_c1}" alt="Reception Card">
    </div>
  </div>

  <!-- PAGE 2: PROGRAMME -->
  <div class="portrait-sheet">
    <div class="outer-border"></div>
    <div class="inner-border"></div>
    <div class="card-frame">
      <img src="{b64_c2}" alt="Programme Card">
    </div>
  </div>
</body>
</html>
"""

page2_html_path = os.path.join(OUTPUT_DIR, 'variant2_2page_final.html')
with open(page2_html_path, 'w') as f:
    f.write(html_2page)

print("Generated HTML sources. Compiling PDFs and PNG previews...")

# Render PDFs
pdf_spread = os.path.join(OUTPUT_DIR, 'Ejaz_Iqura_Wedding_Invitation_Spread.pdf')
pdf_2page = os.path.join(OUTPUT_DIR, 'Ejaz_Iqura_Wedding_Invitation_2Page.pdf')

subprocess.run([
    CHROME_BIN, '--headless', '--disable-gpu', '--no-pdf-header-footer',
    f'--print-to-pdf={pdf_spread}', f'file://{spread_html_path}'
], capture_output=True)

subprocess.run([
    CHROME_BIN, '--headless', '--disable-gpu', '--no-pdf-header-footer',
    f'--print-to-pdf={pdf_2page}', f'file://{page2_html_path}'
], capture_output=True)

# Render PNG Previews
png_spread = os.path.join(OUTPUT_DIR, 'Ejaz_Iqura_Wedding_Invitation_Spread.png')
subprocess.run([
    CHROME_BIN, '--headless', '--disable-gpu',
    f'--screenshot={png_spread}', '--window-size=1440,960',
    f'file://{spread_html_path}'
], capture_output=True)

# Standalone card image copies
shutil.copy2(os.path.join(ASSETS_DIR, 'card1_studio_perfect.jpg'), os.path.join(OUTPUT_DIR, 'Card_1_Reception_Ceremony.jpg'))
shutil.copy2(os.path.join(ASSETS_DIR, 'card2_studio_perfect.jpg'), os.path.join(OUTPUT_DIR, 'Card_2_Programme_Walima.jpg'))

# Sync to Downloads for user convenience
for fname in [
    'Ejaz_Iqura_Wedding_Invitation_Spread.pdf',
    'Ejaz_Iqura_Wedding_Invitation_2Page.pdf',
    'Ejaz_Iqura_Wedding_Invitation_Spread.png',
    'Card_1_Reception_Ceremony.jpg',
    'Card_2_Programme_Walima.jpg'
]:
    src = os.path.join(OUTPUT_DIR, fname)
    dst = os.path.join(DOWNLOADS_DIR, fname)
    if os.path.exists(src):
        shutil.copy2(src, dst)
        print(f" Synced: {fname} -> ~/Downloads/")

print("\nFinal Variant 2 deliverables ready!")
