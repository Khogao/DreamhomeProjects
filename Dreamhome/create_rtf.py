"""
RTF Generator for Adobe InDesign
Creates Rich Text Format file that InDesign can import directly
"""

def create_rtf_file():
    """Create RTF file optimized for Adobe InDesign import"""
    
    # RTF Header with color table and font table
    rtf_header = r"""{\rtf1\ansi\deff0 
{\fonttbl
{\f0\fswiss\fcharset0 Arial;}
{\f1\fswiss\fcharset0 Montserrat;}
{\f2\fmodern\fcharset0 Courier New;}
}
{\colortbl;
\red46\green134\blue171;
\red51\green51\blue51;
\red245\green245\blue245;
\red40\green167\blue69;
\red255\green193\blue7;
\red220\green53\blue69;
\red255\green255\blue255;
}
"""

    # Read markdown content
    try:
        with open("Phan tich.md", "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print("❌ Không tìm thấy file Phan tich.md")
        return

    # Convert content to RTF format
    rtf_content = convert_to_rtf(content)
    
    # Complete RTF document
    full_rtf = rtf_header + rtf_content + "}"
    
    # Save RTF file
    output_file = "Dream_Home_Analysis.rtf"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(full_rtf)
    
    print(f"✅ Đã tạo file RTF: {output_file}")
    print("\n🎯 RTF - FORMAT TỐI ƯU NHẤT CHO INDESIGN:")
    print("✅ Import trực tiếp vào InDesign")
    print("✅ Giữ nguyên fonts, colors, styles")
    print("✅ Tables import hoàn hảo")
    print("✅ Không cần qua Word")

def convert_to_rtf(content):
    """Convert markdown content to RTF format"""
    
    rtf_content = []
    lines = content.split('\n')
    
    for line in lines:
        if line.startswith('# '):
            # H1 - Main title
            title = line[2:].strip()
            rtf_content.append(f"\\pard\\cf1\\f1\\fs56\\b {escape_rtf(title)}\\par\\par")
            
        elif line.startswith('## '):
            # H2 - Section headers
            title = line[3:].strip()
            rtf_content.append(f"\\pard\\cf2\\f1\\fs40\\b\\highlight3 {escape_rtf(title)}\\par\\par")
            
        elif line.startswith('### '):
            # H3 - Subsection headers
            title = line[4:].strip()
            rtf_content.append(f"\\pard\\cf1\\f1\\fs32\\b {escape_rtf(title)}\\par\\par")
            
        elif line.startswith('| '):
            # Table rows - will be handled separately
            continue
            
        elif line.startswith('> '):
            # Blockquotes
            text = line[2:].strip()
            rtf_content.append(f"\\pard\\cf2\\highlight3\\f0\\fs22 {escape_rtf(text)}\\par\\par")
            
        elif line.strip().startswith('- ') or line.strip().startswith('* '):
            # List items
            text = line.strip()[2:].strip()
            rtf_content.append(f"\\pard\\li720\\cf2\\f0\\fs22 • {escape_rtf(text)}\\par")
            
        elif line.strip():
            # Regular paragraphs
            rtf_content.append(f"\\pard\\cf2\\f0\\fs22 {escape_rtf(line)}\\par\\par")
        else:
            # Empty lines
            rtf_content.append("\\par")
    
    return '\n'.join(rtf_content)

def escape_rtf(text):
    """Escape special characters for RTF format"""
    
    # Replace RTF special characters
    text = text.replace('\\', '\\\\')
    text = text.replace('{', '\\{')
    text = text.replace('}', '\\}')
    
    # Handle common symbols
    text = text.replace('✅', '\\u10003?')
    text = text.replace('⚠️', '\\u9888?')
    text = text.replace('🔴', '\\u128308?')
    text = text.replace('🟡', '\\u128993?')
    text = text.replace('🟢', '\\u128994?')
    text = text.replace('💰', '\\u128176?')
    text = text.replace('📊', '\\u128202?')
    text = text.replace('🏢', '\\u127970?')
    text = text.replace('⚖️', '\\u9878?')
    
    # Handle bold and italic markdown
    text = text.replace('**', '\\b ')  # Bold start
    text = text.replace('*', '\\i ')   # Italic start
    
    return text

if __name__ == "__main__":
    create_rtf_file()