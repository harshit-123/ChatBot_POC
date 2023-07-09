var uploadContainer = document.getElementById('drag-section');
// var uploadContainer = document.getElementById('drag-section-2');
    //event listener for click event
    uploadContainer.addEventListener('click', handleClick, false);

    function handleClick() {
      // Create an input element of type "file"
      var fileInput = document.createElement('input');
      fileInput.type = 'file';
      fileInput.name = 'pdf';

      // event listener for change event
      fileInput.addEventListener('change', handleFileSelect, false);
      document.getElementById('dynamic_file').appendChild(fileInput);
      document.getElementById('dynamic_file').style.display = 'none';
      // Trigger the click event of the file input element
      fileInput.click();
    }
    
    function handleFileSelect(e) {
      var file = e.target.files[0];
      // console.log("fsfsd", file)
      document.getElementById('uploadingData').innerHTML = 'Ready to launch Chatbot'
      document.getElementById('uploaded').style.display = 'none'
      document.getElementById('uploaded-image').style.display = 'block'
      document.getElementById('uploadText').style.display = 'flex'
      document.getElementById('pdf-container').style.height = '125vh'

      // Process the selected file here (e.g., upload to a server)
      // You can access the file details using the file object

      // Example: Display the file name
      uploadContainer.innerHTML = 'Selected file: ' + file.name;
      // console.log(file.name);
      // document.getElementById('pdf').value = file.name
    }

    function newPage(){
      
      setTimeout(() => {
        window.location.href = "newfile.html";
      }, 10000);
      document.getElementById('uploadingData').innerHTML = 'Launching Chat Bot'
      document.getElementById('uploaded').style.display = 'none'
      document.getElementById('uploaded-image').style.display = 'none'
      document.getElementById('uploadText').style.display = 'none'
      document.getElementById('robot').style.display = 'block'
      document.getElementById('robot-img').style.height = '600px'
      document.getElementById('robot-img').style.width = '580px'
      document.getElementById('robot-img').style.paddingBottom = '60px'
      document.getElementById('drag-section').style.display='none'

    }
    
    
    
    