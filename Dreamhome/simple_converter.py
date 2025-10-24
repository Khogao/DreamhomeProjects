"""
Simple HTML Generator for Adobe InDesign Import
Creates Word-compatible HTML from Markdown content
"""

import re
import os

def create_html_for_word():
    """Create HTML file that Word can import with styles"""
    
    # Read the markdown file
    try:
        with open("Phan tich.md", "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print("❌ Không tìm thấy file Phan tich.md")
        return
    
    # Simple markdown to HTML conversion
    html_content = convert_markdown_to_html(content)
    
    # Create complete HTML document with styles
    full_html = create_styled_html(html_content)
    
    # Save HTML file
    output_file = "Dream_Home_Analysis_for_Word.html"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(full_html)
    
    print(f"✅ Đã tạo file: {output_file}")
    print("\n📋 HƯỚNG DẪN SỬ DỤNG:")
    print("1. Mở file HTML bằng Microsoft Word")
    print("2. Save As → Word Document (.docx)")
    print("3. Import file .docx vào Adobe InDesign")
    print("4. Styles và màu sắc sẽ được giữ nguyên!")

def convert_markdown_to_html(content):
    """Convert basic markdown syntax to HTML"""
    
    # Headers
    content = re.sub(r'^# (.+)$', r'<h1>\1</h1>', content, flags=re.MULTILINE)
    content = re.sub(r'^## (.+)$', r'<h2>\1</h2>', content, flags=re.MULTILINE)
    content = re.sub(r'^### (.+)$', r'<h3>\1</h3>', content, flags=re.MULTILINE)
    
    # Bold and italic
    content = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', content)
    content = re.sub(r'\*(.+?)\*', r'<em>\1</em>', content)
    
    # Code blocks
    content = re.sub(r'`(.+?)`', r'<code>\1</code>', content)
    
    # Blockquotes
    content = re.sub(r'^> (.+)$', r'<blockquote>\1</blockquote>', content, flags=re.MULTILINE)
    
    # Convert tables
    content = convert_tables(content)
    
    # Convert lists
    content = convert_lists(content)
    
    # Line breaks
    content = content.replace('\n\n', '</p><p>')
    content = '<p>' + content + '</p>'
    
    return content

def convert_tables(content):
    """Convert markdown tables to HTML tables"""
    
    # Find table patterns
    table_pattern = r'(\|.+\|\n)+(\|[-:\s]+\|\n)(\|.+\|\n)+'
    
    def table_replacer(match):
        lines = match.group(0).strip().split('\n')
        
        # Skip header separator line
        header_line = lines[0]
        data_lines = lines[2:]
        
        # Create table HTML
        html = '<table border="1" style="border-collapse: collapse; width: 100%;">\n'
        
        # Header row
        header_cells = [cell.strip() for cell in header_line.split('|')[1:-1]]
        html += '<tr>'
        for cell in header_cells:
            html += f'<th style="background-color: #2E86AB; color: white; padding: 8pt;">{cell}</th>'
        html += '</tr>\n'
        
        # Data rows
        for i, line in enumerate(data_lines):
            cells = [cell.strip() for cell in line.split('|')[1:-1]]
            bg_color = "#F5F5F5" if i % 2 == 1 else "white"
            html += f'<tr style="background-color: {bg_color};">'
            for cell in cells:
                # Check if cell contains financial data
                if any(x in cell for x in ['tỷ', 'triệu', 'VND', '₫']) or re.search(r'[\d,]+\.?\d*', cell):
                    html += f'<td style="padding: 6pt; text-align: right; font-family: monospace; color: #2E86AB;">{cell}</td>'
                else:
                    html += f'<td style="padding: 6pt;">{cell}</td>'
            html += '</tr>\n'
        
        html += '</table>'
        return html
    
    return re.sub(table_pattern, table_replacer, content, flags=re.MULTILINE)

def convert_lists(content):
    """Convert markdown lists to HTML lists"""
    
    # Unordered lists
    content = re.sub(r'^\* (.+)$', r'<li>\1</li>', content, flags=re.MULTILINE)
    content = re.sub(r'^\- (.+)$', r'<li>\1</li>', content, flags=re.MULTILINE)
    
    # Wrap consecutive list items in <ul>
    content = re.sub(r'(<li>.*</li>\n?)+', r'<ul>\g<0></ul>', content, flags=re.MULTILINE | re.DOTALL)
    
    return content

def create_styled_html(content):
    """Create complete HTML document with InDesign-friendly styles"""
    
    return f"""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Báo Cáo Phân Tích Dự Án Dream Home</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            font-size: 11pt;
            line-height: 1.6;
            color: #333333;
            max-width: 210mm;
            margin: 0 auto;
            padding: 20mm;
            background-color: white;
        }}
        
        h1 {{
            color: #2E86AB;
            font-size: 28pt;
            font-weight: bold;
            margin-bottom: 20pt;
            text-align: center;
            border-bottom: 3pt solid #2E86AB;
            padding-bottom: 10pt;
        }}
        
        h2 {{
            color: #333333;
            font-size: 20pt;
            font-weight: 600;
            margin: 25pt 0 15pt 0;
            background: linear-gradient(135deg, #F0F8FF, #E6F3FF);
            padding: 12pt;
            border-left: 5pt solid #2E86AB;
            border-radius: 5pt;
        }}
        
        h3 {{
            color: #2E86AB;
            font-size: 16pt;
            font-weight: 600;
            margin: 20pt 0 12pt 0;
            border-bottom: 1pt solid #E0E0E0;
            padding-bottom: 5pt;
        }}
        
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 15pt 0;
            box-shadow: 0 2pt 4pt rgba(0,0,0,0.1);
        }}
        
        th {{
            background-color: #2E86AB;
            color: white;
            font-weight: bold;
            padding: 10pt 8pt;
            text-align: left;
            border: 1pt solid #2E86AB;
        }}
        
        td {{
            padding: 8pt;
            border: 1pt solid #E0E0E0;
            vertical-align: top;
        }}
        
        tr:nth-child(even) {{
            background-color: #F9F9F9;
        }}
        
        tr:nth-child(odd) {{
            background-color: white;
        }}
        
        strong {{
            color: #2E86AB;
            font-weight: bold;
        }}
        
        em {{
            color: #666666;
            font-style: italic;
        }}
        
        code {{
            background-color: #F5F5F5;
            padding: 2pt 4pt;
            border-radius: 3pt;
            font-family: 'Courier New', monospace;
            font-size: 10pt;
        }}
        
        blockquote {{
            background-color: #F8F9FA;
            border-left: 4pt solid #2E86AB;
            margin: 15pt 0;
            padding: 12pt 16pt;
            border-radius: 0 5pt 5pt 0;
            font-style: italic;
        }}
        
        ul {{
            margin: 10pt 0;
            padding-left: 20pt;
        }}
        
        li {{
            margin: 5pt 0;
            line-height: 1.5;
        }}
        
        p {{
            margin: 10pt 0;
            text-align: justify;
        }}
        
        /* Special styling for financial numbers */
        .financial {{
            font-family: 'Courier New', monospace;
            font-weight: bold;
            color: #2E86AB;
            text-align: right;
        }}
        
        /* Status indicators */
        .status-success {{ color: #28A745; font-weight: bold; }}
        .status-warning {{ color: #FFC107; font-weight: bold; }}
        .status-danger {{ color: #DC3545; font-weight: bold; }}
        .status-info {{ color: #007BFF; font-weight: bold; }}
        
        /* Print styles */
        @media print {{
            body {{ margin: 0; padding: 15mm; }}
            h1 {{ page-break-after: avoid; }}
            h2, h3 {{ page-break-after: avoid; }}
            table {{ page-break-inside: avoid; }}
        }}
    </style>
</head>
<body>
    {content}
</body>
</html>"""

if __name__ == "__main__":
    create_html_for_word()