from flask import (
    Flask,
    render_template,
    redirect,
    request,
    url_for
)

from PyPDF2 import PdfFileReader,PdfFileWriter
import os
import json


app=Flask(__name__)

app.config['UPLOAD_PATH']='static/uploads'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        if request.files:
            pdf_file=request.files['file']

            pdf_file_name=os.path.join(app.config['UPLOAD_PATH'],pdf_file.filename)

            pdf_file.save(pdf_file_name)

            return redirect('/')


        return redirect('/')
    return render_template('index.html')


@app.route('/<filename>')
def show_file_content(filename):


    pdf_file_name=os.path.join(app.config['UPLOAD_PATH'],filename)

    pdf_file = PdfFileReader(pdf_file_name)


    pages=pdf_file.getNumPages()

    text=json.dumps(str(pdf_file_name))


    context={
        'pages':pages,
        'file_name':filename,
        'text':text
    }
    return render_template('fileview.html',**context)






if __name__ == '__main__':
    app.run(debug=True,port=8000)