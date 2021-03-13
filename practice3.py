from PyPDF2 import PdfFileReader,PdfFileWriter
import os

base_dir = os.path.dirname(os.path.abspath(__file__))

input_pdf_file=os.path.join(base_dir,'Chapter10.pdf')

pdf_reader=PdfFileReader(str(input_pdf_file))

#extract the pages we want to write to a pdf file


pdf_writer=PdfFileWriter()

for page_number in range(10,15):
    page=pdf_reader.getPage(page_number)

    pdf_writer.addPage(page)


#create a pdf adn write the pages to it

with open('pages10-14.pdf','wb') as multi_page_pdf_file:
    pdf_writer.write(multi_page_pdf_file)