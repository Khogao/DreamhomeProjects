#!/usr/bin/env python3
"""
Convert Markdown to HTML for Adobe InDesign Import via Word
Simple conversion without external dependencies
"""

import re
import os

def markdown_to_html_with_styles(md_file_path):
    """Convert Markdown to HTML with inline styles for Word import"""
    
    # Read markdown file
    with open(md_file_path, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # Convert markdown to HTML
    md = markdown.Markdown(extensions=['tables', 'codehilite', 'fenced_code'])
    html_content = md.convert(md_content)
    
    # Parse HTML with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Style mappings for InDesign compatibility
    styles = {
        'h1': 'color: #2E86AB; font-family: Montserrat, Arial; font-size: 24pt; font-weight: bold; margin-bottom: 20pt;',
        'h2': 'color: #333333; font-family: Montserrat, Arial; font-size: 20pt; font-weight: 600; margin-bottom: 15pt; background-color: #F0F8FF; padding: 8pt;',
        'h3': 'color: #2E86AB; font-family: Montserrat, Arial; font-size: 16pt; font-weight: 600; margin-bottom: 12pt;',
        'table': 'border-collapse: collapse; width: 100%; margin-bottom: 20pt; font-family: Source Sans Pro, Arial;',
        'th': 'background-color: #2E86AB; color: white; font-weight: bold; padding: 8pt 12pt; border: 1pt solid #2E86AB; text-align: left;',
        'td': 'padding: 6pt 8pt; border: 1pt solid #E0E0E0; vertical-align: top;',
        'tr:nth-child(even)': 'background-color: #F5F5F5;',
        'tr:nth-child(odd)': 'background-color: white;',
        'blockquote': 'background-color: #F8F9FA; border-left: 4pt solid #2E86AB; padding: 12pt 16pt; margin: 15pt 0; border-radius: 4pt;',
        'code': 'font-family: Roboto Mono, Consolas; background-color: #F5F5F5; padding: 2pt 4pt; border-radius: 3pt; font-size: 9pt;',
        'strong': 'font-weight: bold; color: #2E86AB;',
        'em': 'font-style: italic; color: #666666;'
    }
    
    # Apply styles to elements
    for tag, style in styles.items():
        if ':nth-child' not in tag:
            elements = soup.find_all(tag.split(':')[0])
            for element in elements:
                element['style'] = style
    
    # Handle special formatting for financial data
    # Find cells with currency values
    for td in soup.find_all('td'):
        text = td.get_text().strip()
        if any(char in text for char in ['₫', 'VND', 'tỷ', 'triệu']) or re.match(r'[\d,]+\.?\d*', text):
            td['style'] = td.get('style', '') + ' font-family: Roboto Mono, Consolas; font-weight: 500; color: #2E86AB; text-align: right;'
    
    # Handle status indicators
    status_patterns = {
        '✅': 'color: #28A745; font-weight: bold;',
        '⚠️': 'color: #FFC107; font-weight: bold;',
        '🔴': 'color: #DC3545; font-weight: bold;',
        '🟡': 'color: #FD7E14; font-weight: bold;',
        '🟢': 'color: #007BFF; font-weight: bold;'
    }
    
    for pattern, style in status_patterns.items():
        for element in soup.find_all(text=re.compile(re.escape(pattern))):
            if element.parent:
                element.parent['style'] = element.parent.get('style', '') + style
    
    # Add alternating row colors to tables
    for table in soup.find_all('table'):
        rows = table.find_all('tr')[1:]  # Skip header row
        for i, row in enumerate(rows):
            if i % 2 == 0:
                row['style'] = 'background-color: #FFFFFF;'
            else:
                row['style'] = 'background-color: #F5F5F5;'
    
    # Create complete HTML document
    html_doc = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Dream Home Project Analysis</title>
        <style>
            body {{
                font-family: 'Source Sans Pro', Arial, sans-serif;
                font-size: 11pt;
                line-height: 1.4;
                color: #333333;
                max-width: 210mm;
                margin: 0 auto;
                padding: 20mm;
            }}
            .financial-highlight {{
                background-color: #E6F3FF;
                border: 1pt solid #2E86AB;
                border-radius: 6pt;
                padding: 15pt;
                margin: 12pt 0;
            }}
            .section-divider {{
                height: 2pt;
                background: linear-gradient(to right, #2E86AB, #F5F5F5);
                margin: 25pt 0;
                border: none;
            }}
        </style>
    </head>
    <body>
        {soup.prettify()}
    </body>
    </html>
    """
    
    return html_doc

def save_for_word_import(html_content, output_path):
    """Save HTML that Word can import with styles preserved"""
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

def create_word_compatible_html():
    """Main function to create Word-compatible HTML from Markdown"""
    
    md_file = "Phan tich.md"
    html_output = "Dream_Home_Analysis_for_InDesign.html"
    
    print("🔄 Converting Markdown to HTML with InDesign-optimized styles...")
    
    try:
        # Convert markdown to styled HTML
        html_content = markdown_to_html_with_styles(md_file)
        
        # Save HTML file
        save_for_word_import(html_content, html_output)
        
        print(f"✅ Successfully created: {html_output}")
        print("\n📋 NEXT STEPS:")
        print("1. Open the HTML file in Microsoft Word")
        print("2. Save as .docx format")
        print("3. Import the .docx file into Adobe InDesign")
        print("4. Styles will be preserved and ready for further customization")
        print("\n🎨 COLOR PALETTE USED:")
        print("- Primary Blue: #2E86AB")
        print("- Success Green: #28A745") 
        print("- Warning Orange: #FFC107")
        print("- Danger Red: #DC3545")
        print("- Light Gray: #F5F5F5")
        
    except FileNotFoundError:
        print(f"❌ Error: Could not find {md_file}")
        print("Make sure the Markdown file is in the same directory")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    create_word_compatible_html()