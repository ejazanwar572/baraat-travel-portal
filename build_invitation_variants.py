import os
import subprocess
from PIL import Image
import numpy as np

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')
OUTPUT_DIR = os.path.join(BASE_DIR, 'invitation_variants')
os.makedirs(ASSETS_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

CHROME_BIN = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

print("1. Preparing cleaned physical card assets...")

# Clean Card 1 (Reception)
im1 = Image.open(os.path.join(BASE_DIR, 'wedding_card_1_reception.jpg')).convert('RGB')
card1 = im1.crop((372, 38, 1215, 878))
w1, h1 = card1.size
arr1 = np.array(card1, dtype=float)
backing_ivory = np.array([244, 238, 226], dtype=float)

for x1, x2 in [(0, int(w1 * 0.28)), (int(w1 * 0.75), w1)]:
    sub = arr1[:, x1:x2]
    lum = 0.299 * sub[:,:,0] + 0.587 * sub[:,:,1] + 0.114 * sub[:,:,2]
    is_hole = (lum < 132) | (sub[:,:,0] > sub[:,:,1] + 25) | ((sub[:,:,2] > sub[:,:,0] + 15) & (lum < 155))
    alpha = is_hole[:,:,None].astype(float)
    arr1[:, x1:x2] = arr1[:, x1:x2] * (1 - alpha) + backing_ivory * alpha

# Clean top edge ribbon area
for y in range(int(h1 * 0.05)):
    for x in range(w1):
        lum = 0.299 * arr1[y,x,0] + 0.587 * arr1[y,x,1] + 0.114 * arr1[y,x,2]
        if lum < 140:
            arr1[y,x] = backing_ivory

card1_clean = Image.fromarray(arr1.astype(np.uint8))
card1_clean_path = os.path.join(ASSETS_DIR, 'card1_studio_cleaned.jpg')
card1_clean.save(card1_clean_path, quality=95)

# Clean Card 2 (Programme)
im2 = Image.open(os.path.join(BASE_DIR, 'wedding_card_2_programme.jpg')).convert('RGB')
card2 = im2.crop((362, 32, 1205, 872))
w2, h2 = card2.size
arr2 = np.array(card2, dtype=float)
backing_sage = np.array([215, 230, 222], dtype=float)

for x1, x2 in [(0, int(w2 * 0.28)), (int(w2 * 0.75), w2)]:
    sub = arr2[:, x1:x2]
    lum = 0.299 * sub[:,:,0] + 0.587 * sub[:,:,1] + 0.114 * sub[:,:,2]
    is_hole = (lum < 132) | (sub[:,:,0] > sub[:,:,1] + 25) | ((sub[:,:,2] > sub[:,:,0] + 15) & (lum < 155))
    alpha = is_hole[:,:,None].astype(float)
    arr2[:, x1:x2] = arr2[:, x1:x2] * (1 - alpha) + backing_sage * alpha

# Clean top white tab/ribbon area
for y in range(int(h2 * 0.05)):
    for x in range(w2):
        arr2[y,x] = backing_sage

card2_clean = Image.fromarray(arr2.astype(np.uint8))
card2_clean_path = os.path.join(ASSETS_DIR, 'card2_studio_cleaned.jpg')
card2_clean.save(card2_clean_path, quality=95)

print("Card cleaning completed successfully!")
