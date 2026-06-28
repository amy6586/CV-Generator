import markdown
from weasyprint import HTML
import sys
import os
import base64
import re

md_file = sys.argv[1]
pdf_file = sys.argv[2]
photo_path = sys.argv[3] if len(sys.argv) > 3 else None

with open(md_file, 'r') as f:
    md_content = f.read()

# Extract h1 name and contact line to build a custom header
name_match = re.match(r'^# (.+)', md_content, re.MULTILINE)
name = name_match.group(1) if name_match else ''

# Remove the h1 so it doesn't duplicate in the body
md_content_body = re.sub(r'^# .+\n', '', md_content, count=1)

html_body = markdown.markdown(md_content_body, extensions=['tables'])

# Build photo tag if photo exists
photo_html = ''
if photo_path and os.path.exists(photo_path):
    with open(photo_path, 'rb') as f:
        photo_b64 = base64.b64encode(f.read()).decode('utf-8')
    ext = os.path.splitext(photo_path)[1].lower().lstrip('.')
    mime = 'jpeg' if ext in ('jpg', 'jpeg') else ext
    photo_html = f'<img src="data:image/{mime};base64,{photo_b64}" class="photo" />'

html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  @page {{
    margin: 15mm 18mm 15mm 18mm;
    size: A4;
  }}
  body {{
    font-family: Georgia, 'Times New Roman', serif;
    font-size: 10.5pt;
    color: #1a1a1a;
    line-height: 1.45;
  }}
  .cv-header {{
    display: flex;
    align-items: center;
    gap: 18px;
    margin-bottom: 16px;
    border-bottom: 2px solid #1a1a1a;
    padding-bottom: 12px;
  }}
  .photo {{
    width: 80px;
    height: 80px;
    border-radius: 50%;
    object-fit: cover;
    object-position: center top;
    flex-shrink: 0;
  }}
  .cv-header-text h1 {{
    font-size: 22pt;
    font-weight: bold;
    margin: 0 0 2px 0;
    letter-spacing: 0.5px;
    color: #0a0a0a;
  }}
  .cv-header-text p {{
    font-size: 9.5pt;
    color: #444;
    margin: 0;
    font-style: italic;
  }}
  h2 {{
    font-size: 10.5pt;
    font-weight: bold;
    text-transform: uppercase;
    letter-spacing: 1px;
    border-bottom: 1.5px solid #333;
    padding-bottom: 2px;
    margin: 16px 0 7px 0;
    color: #0a0a0a;
  }}
  h3 {{
    font-size: 10.5pt;
    font-weight: bold;
    margin: 10px 0 1px 0;
    color: #0a0a0a;
  }}
  h3 + p {{
    font-size: 9.5pt;
    color: #555;
    margin: 0 0 5px 0;
    font-style: italic;
  }}
  ul {{
    margin: 4px 0 8px 0;
    padding-left: 16px;
  }}
  li {{
    margin-bottom: 3px;
    font-size: 10pt;
  }}
  p {{
    margin: 4px 0 8px 0;
    font-size: 10pt;
  }}
  table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 9pt;
    margin: 8px 0;
  }}
  th, td {{
    border: 1px solid #ccc;
    padding: 4px 7px;
    text-align: left;
    vertical-align: top;
  }}
  th {{
    background: #f0f0f0;
    font-weight: bold;
  }}
  hr {{
    border: none;
    border-top: 1px solid #ccc;
    margin: 10px 0;
  }}
</style>
</head>
<body>
<div class="cv-header">
  {photo_html}
  <div class="cv-header-text">
    <h1>{name}</h1>
  </div>
</div>
{html_body}
</body>
</html>"""

HTML(string=html).write_pdf(pdf_file, stylesheets=[])
print(f"PDF written to {pdf_file}")
