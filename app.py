from PyPDF2 import PdfFileReader
import os

base_dir=os.path.dirname(os.path.realpath(__file__))

pdf_path=os.path.join(base_dir,'Chapter10.pdf')

pdf=PdfFileReader(str(pdf_path))


# print(pdf.getNumPages())
first_page=pdf.getPage(30)


with open('document.txt',mode='w') as final_file:
    title=pdf.documentInfo.title
    num_pages=pdf.getNumPages()

    final_file.write(f"{title} \\n NUmber of pages {num_pages}")

    for page in pdf.pages:
        text=page.extractText()
        final_file.write(text)