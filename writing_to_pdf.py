from PyPDF2 import PdfFileWriter
import os

base_dir=os.path.dirname(os.path.realpath(__file__))

pdf_path=os.path.join(base_dir,'Chapter10.pdf')

pdf_writer=PdfFileWriter()

page=pdf_writer.addBlankPage(width=72,height=72)

print(type(page))


with open('mypdf.pdf','wb') as final_pdf_file:
    pdf_writer.write(final_pdf_file)

    