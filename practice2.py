from PyPDF2 import PdfFileWriter,PdfFileReader
import os

base_dir = os.path.dirname(os.path.realpath(__file__))

pdf_file_to_read = os.path.join(base_dir,'Chapter10.pdf')

#pdf_reader_instance
pdf_reader=PdfFileReader(str(pdf_file_to_read))


page_extracted=pdf_reader.getPage(2)


# print(page_extracted.extractText())

# create a new PDF writer to add the extracted text to
pdf_writer=PdfFileWriter()

pdf_writer.addPage(page_extracted)

with open('second_page.pdf', 'wb') as second_page_pdf_file:
    pdf_writer.write(second_page_pdf_file)