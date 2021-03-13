from PyPDF2 import PdfFileReader
import os


base_dir=os.path.dirname(os.path.realpath(__file__))

# print(base_dir)

pdf_path=os.path.join(base_dir,'Chapter10.pdf')

# print(pdf_path)

pdf=PdfFileReader(str(pdf_path))

first=pdf.getPage(0)
print(first)

first_page_text=first.extractText()

print(f"\n {first_page_text}")

for page in pdf.pages:
    print(page.extractText())