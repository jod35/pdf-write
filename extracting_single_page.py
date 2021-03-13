from PyPDF2 import PdfFileReader,PdfFileWriter
import os

base_dir = os.path.dirname(os.path.abspath(__file__))

input_path=os.path.join(base_dir,'Chapter10.pdf')

input_pdf_file=PdfFileReader(str(input_path))

first_page=input_pdf_file.getPage(0)

#create a file writer instance and write the page to the pdf

pdf_writer=PdfFileWriter()

#create a blank page and add the first page to it
pdf_writer.addBlankPage(width=100,height=100)

with open('first_page.pdf','wb') as first_page_pdf_file:
    pdf_writer.write(first_page_pdf_file)



