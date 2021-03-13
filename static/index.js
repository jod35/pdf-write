const resultDisplaySection=document.querySelector('.result');

Dropzone.options.myAwesomeDropzone = {
    init: function() {


      this.on("success", function (file,response){
          setTimeout(() => {
            resultDisplaySection.style.display ="block";
          }, 2000);

          let file_name=file.name;

          let fileLink=document.querySelector('.file-link');

          fileLink.setAttribute('href',file_name);
      })
    }
  };