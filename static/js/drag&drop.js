var uploadContainer = document.getElementById("drag-section");
// var uploadContainer = document.getElementById('drag-section-2');

//event listener for click event
uploadContainer.addEventListener("click", handleClick, false);

function handleClick() {
  // Create an input element of type "file"
  var fileInput = document.createElement("input");
  fileInput.type = "file";
  fileInput.name = 'pdf';
  fileInput.setAttribute("multiple","");

  // event listener for change event
  fileInput.addEventListener("change", handleFileSelect, false);
  document.getElementById('dynamic_file').appendChild(fileInput);
  document.getElementById('dynamic_file').style.display = 'none';
  // event listener for change event
  fileInput.addEventListener("change", handleFileSelect, false);

  // Trigger the click event of the file input element
  fileInput.click();
}

function handleFileSelect(e) {
  var file = e.target.files[0];
  document.getElementById("uploadingData").innerHTML =
    "Ready to launch Chatbot";
  document.getElementById("uploaded").style.display = "none";
  document.getElementById("uploaded-image").style.display = "block";
  document.getElementById("uploadText").style.display = "flex";
  document.getElementById("pdf-container").style.height = "125vh";

  // Process the selected file here (e.g., upload to a server)
  // You can access the file details using the file object

  // Example: Display the file name
  uploadContainer.innerHTML = "Selected file: " + file.name;
}
var uploadContainer = document.getElementById("drag-section");
// var uploadContainer = document.getElementById('drag-section-2');

//event listener for click event
uploadContainer.addEventListener("click", handleClick, false);

// function handleClick() {
//   // Create an input element of type "file"
//   var fileInput = document.createElement("input");
//   fileInput.type = "file";

//   // event listener for change event
//   fileInput.addEventListener("change", handleFileSelect, false);

//   // Trigger the click event of the file input element
//   fileInput.click();
// }

// function handleFileSelect(e) {
//   var file = e.target.files[0];
//   document.getElementById("uploadingData").innerHTML =
//     "Ready to launch Chatbot";
//   document.getElementById("uploaded").style.display = "none";
//   document.getElementById("uploaded-image").style.display = "block";
//   document.getElementById("uploadText").style.display = "flex";
//   document.getElementById("pdf-container").style.height = "125vh";

//   // Process the selected file here (e.g., upload to a server)
//   // You can access the file details using the file object

//   // Example: Display the file name
//   uploadContainer.innerHTML = "Selected file: " + file.name;
// }

function newPage() {
  setTimeout(() => {
    window.location.href = "newfile.html";
  }, 10000);
  document.getElementById("uploadingData").innerHTML = "Launching Chat Bot";
  document.getElementById("uploaded").style.display = "none";
  document.getElementById("uploaded-image").style.display = "none";
  document.getElementById("uploadText").style.display = "none";
  document.getElementById("robot").style.display = "block";
  document.getElementById("robot-img").style.height = "600px";
  document.getElementById("robot-img").style.width = "580px";
  document.getElementById("robot-img").style.paddingBottom = "60px";
  document.getElementById("drag-section").style.display = "none";
}

$(document).ready(function () {
  // Show/hide main section and scroll to it
  $("#show-main").click(function () {
    $("#main-section").fadeIn("slow"); // Show main section with fade animation
    document.getElementById("body").style.overflowY = "visible";
    $("html, body").animate(
      {
        scrollTop: $("#main-section").offset().top, // Scroll to main section
      },
      100
    ); // Scroll animation duration (in milliseconds)
  });
});

let main = document.querySelector(".d_none");
function showmain() {
  main.classList.toggle("d-block");
}
