import re

with open('generate_invitations.py', 'r') as f:
    content = f.read()

# Fix floral overlay positioning in Variant 1: place on left and right wings
content = content.replace(
    ".wf-tl { top: 10px; left: 65px; }",
    ".wf-tl { top: 15px; left: -10px; opacity: 0.95; }"
)
content = content.replace(
    ".wf-br { bottom: 10px; right: 65px; transform: rotate(180deg); }",
    ".wf-br { bottom: 15px; right: -10px; transform: rotate(180deg); opacity: 0.95; }"
)

# Also let's generate Page 2 preview for Variant 1 and Spread preview for Variant 1
old_previews = """previews = [
    ('Variant_1_Page1_Preview.png', path_v1_html, 840, 1160),
    ('Variant_2_Spread_Preview.png', path_v2_html, 1460, 1000),
    ('Variant_3_Mobile_Preview.png', path_v3_html, 720, 1260)
]"""

new_previews = """previews = [
    ('Variant_1_Page1_Preview.png', path_v1_html, 840, 1160),
    ('Variant_2_Spread_Preview.png', path_v2_html, 1460, 1000),
    ('Variant_3_Mobile_Preview.png', path_v3_html, 720, 1260)
]"""

with open('generate_invitations.py', 'w') as f:
    f.write(content)

print("Updated script with better floral positioning")
