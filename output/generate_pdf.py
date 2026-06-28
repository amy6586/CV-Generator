import markdown
from weasyprint import HTML, CSS
import sys

md_file = sys.argv[1]
pdf_file = sys.argv[2]

with open(md_file, 'r') as f:
    md_content = f.read()

html_body = markdown.markdown(md_content, extensions=['tables'])

html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  @page {{
    margin: 18mm 18mm 18mm 18mm;
    size: A4;
  }}
  body {{
    font-family: Georgia, 'Times New Roman', serif;
    font-size: 10.5pt;
    color: #1a1a1a;
    line-height: 1.45;
  }}
  h1 {{
    font-size: 20pt;
    font-weight: bold;
    margin: 0 0 2px 0;
    letter-spacing: 0.5px;
    color: #0a0a0a;
  }}
  h1 + p {{
    font-size: 10pt;
    color: #444;
    margin: 0 0 14px 0;
    font-style: italic;
  }}
  h2 {{
    font-size: 11pt;
    font-weight: bold;
    text-transform: uppercase;
    letter-spacing: 1px;
    border-bottom: 1.5px solid #333;
    padding-bottom: 2px;
    margin: 18px 0 8px 0;
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
{html_body}
</body>
</html>"""

HTML(string=html).write_pdf(pdf_file, stylesheets=[])
print(f"PDF written to {pdf_file}")
