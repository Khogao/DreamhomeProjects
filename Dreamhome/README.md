Convert Phan tich.md to Excel workbook with multiple sheets

Usage:

1. Create a Python environment (optional but recommended).

2. Install dependencies:

   pip install -r requirements.txt

3. Run the converter:

   python convert_md_to_xlsx.py "Phan tich.md"

The script will create `Phan tich.xlsx` in the same folder as the Markdown file. It splits the document by headings and attempts to convert Markdown tables to Excel sheets. Text blocks are written into single-column sheets.