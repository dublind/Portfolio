#!/usr/bin/env python3
"""
Convert the Data Engineering Learning Path markdown to PDF
Requires: pip install markdown weasyprint
"""

import markdown
from weasyprint import HTML, CSS
from pathlib import Path

def create_pdf():
    # Read the markdown file
    md_file = Path("Data_Engineering_Learning_Path.md")
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # Convert markdown to HTML
    html_content = markdown.markdown(
        md_content,
        extensions=['extra', 'codehilite', 'toc', 'tables']
    )

    # Create full HTML document with styling
    full_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Data Engineering Learning Path</title>
        <style>
            @page {{
                size: A4;
                margin: 2cm;
                @bottom-right {{
                    content: "Page " counter(page) " of " counter(pages);
                    font-size: 9pt;
                    color: #666;
                }}
            }}
            body {{
                font-family: 'Segoe UI', Arial, sans-serif;
                line-height: 1.6;
                color: #333;
                max-width: 100%;
            }}
            h1 {{
                color: #2c3e50;
                border-bottom: 3px solid #3498db;
                padding-bottom: 10px;
                page-break-before: always;
                margin-top: 0;
            }}
            h1:first-of-type {{
                page-break-before: avoid;
            }}
            h2 {{
                color: #34495e;
                border-bottom: 2px solid #95a5a6;
                padding-bottom: 5px;
                margin-top: 30px;
            }}
            h3 {{
                color: #16a085;
                margin-top: 20px;
            }}
            h4 {{
                color: #27ae60;
            }}
            code {{
                background-color: #f4f4f4;
                padding: 2px 6px;
                border-radius: 3px;
                font-family: 'Courier New', monospace;
                font-size: 0.9em;
            }}
            pre {{
                background-color: #f8f8f8;
                border: 1px solid #ddd;
                border-radius: 5px;
                padding: 15px;
                overflow-x: auto;
            }}
            blockquote {{
                border-left: 4px solid #3498db;
                padding-left: 15px;
                margin-left: 0;
                color: #555;
                font-style: italic;
            }}
            ul, ol {{
                margin-left: 20px;
            }}
            li {{
                margin-bottom: 8px;
            }}
            table {{
                border-collapse: collapse;
                width: 100%;
                margin: 20px 0;
            }}
            th, td {{
                border: 1px solid #ddd;
                padding: 12px;
                text-align: left;
            }}
            th {{
                background-color: #3498db;
                color: white;
            }}
            tr:nth-child(even) {{
                background-color: #f9f9f9;
            }}
            a {{
                color: #3498db;
                text-decoration: none;
            }}
            strong {{
                color: #2c3e50;
            }}
            hr {{
                border: none;
                border-top: 2px solid #ecf0f1;
                margin: 30px 0;
            }}
            .page-break {{
                page-break-after: always;
            }}
        </style>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """

    # Convert HTML to PDF
    output_file = "Data_Engineering_Learning_Path.pdf"
    HTML(string=full_html).write_pdf(output_file)

    print(f"✅ PDF created successfully: {output_file}")
    print(f"📄 File size: {Path(output_file).stat().st_size / 1024:.1f} KB")

if __name__ == "__main__":
    try:
        create_pdf()
    except ImportError as e:
        print("❌ Missing required libraries!")
        print("\nPlease install them with:")
        print("  pip install markdown weasyprint")
        print("\nNote: weasyprint requires additional system dependencies:")
        print("  - On Ubuntu/Debian: sudo apt-get install python3-dev python3-pip python3-cffi libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info")
        print("  - On macOS: brew install python cairo pango gdk-pixbuf libffi")
        print("  - On Windows: Install GTK+ from https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer")
    except Exception as e:
        print(f"❌ Error creating PDF: {e}")
