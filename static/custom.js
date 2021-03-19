const pdfWindow=document.querySelector('.text');

PDFObject.embed(`/uploads/${pdfWindow.innerText}`,'#pdfwindow')
