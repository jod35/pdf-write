from PyPDF2 import PdfFileReader,PdfFileWriter
import os

base_dir = os.path.dirname(os.path.abspath(__file__))

pdf_file_path=os.path.join(base_dir, 'Chapter10.pdf')

pdf_reader=PdfFileReader(str(pdf_file_path))


pdf_writer=PdfFileWriter()

#adding pages to extract

for n in range(1,4):
    page=pdf_reader.getPage(n)
    pdf_writer.addPage(page)


with open('pages123.pdf','wb') as multi_page_pdf_file:
    pdf_writer.write(multi_page_pdf_file)
