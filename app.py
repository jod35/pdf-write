from flask import (
    Flask,
    render_template,
    redirect,
    request,
    url_for
)

from PyPDF2 import PdfFileReader,PdfFileWriter
import os


app=Flask(__name__)

app.config['UPLOAD_PATH']='uploads'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        if request.files:
            pdf_file=request.files['file']

            pdf_file_name=os.path.join(app.config['UPLOAD_PATH'],pdf_file.filename)

            pdf_file.save(pdf_file_name)

            return redirect('/')
        print("Hello")
        return redirect('/')
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)