// == SETUP ==
// Get an instance of the canvas
const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');

// Initialize the mouse position to 0.
var mouse = {x: 0, y: 0};

// Set up drawing parameters
ctx.lineWidth = 2;
ctx.lineJoin = 'round';
ctx.lineCap = 'round';
ctx.strokeStyle = '#ff0000';

// Also works on mobile by swapping calls to touchmove, touchstart, and touchend.
// Code adapted from: https://stackoverflow.com/questions/39050460/drawing-on-canvas-using-touchscreen-devices

// Variables to pass to addEventListener(), to detect mouse clicks and movements.
// These variables are changed to the mobile equivalent if on a mobile device.
var start = 'mousedown', move = 'mousemove', end = 'mouseup';

// Check if on mobile and change variables accordingly.
// Code adapted from: https://stackoverflow.com/questions/3514784/what-is-the-best-way-to-detect-a-mobile-device
if (/Mobi/.test(navigator.userAgent)) {
  start = 'touchstart';
  move = 'touchmove';
  end = 'touchend';
}

// == DRAWING ==
// Code for drawing is adapted from: https://www.html5canvastutorials.com/labs/html5-canvas-paint-application/
// Listener which is called when mouse movement is detected.
canvas.addEventListener(move, function(e) {
  mouse.x = e.pageX - this.offsetLeft;
  mouse.y = e.pageY - this.offsetTop;
}, false);

// Listener which is called when mouse button is held down.
canvas.addEventListener(start, function(e) {
  ctx.beginPath();
  ctx.moveTo(mouse.x, mouse.y);

  // Call mouse movement listener which will draw a line between each new mouse position.
  canvas.addEventListener(move, onPaint, false);
}, false);

// Listener which is called when mouse button is released.
// Stops drawing by passing false to touchmove.
canvas.addEventListener(end, function() {
  canvas.removeEventListener(move, onPaint, false);
}, false);

// Function to draw line from previous mouse position to new position.
var onPaint = function() {
  ctx.lineTo(mouse.x, mouse.y);
  ctx.stroke();
};

// == OTHER CANVAS FUNCTIONALITY ==
// To clear the canvas I research and found a simple way to do it using the clearRect function.
// Code adapted from: https://stackoverflow.com/questions/2142535/how-to-clear-the-canvas-for-redrawing
function clearCanvas() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  document.getElementById("result").innerHTML = "";
}

// returns true if every pixel's uint32 representation is 0 (or "blank")
// Used to check if canvas is blank before submitting request.
// Code adapted from: https://stackoverflow.com/questions/17386707/how-to-check-if-a-canvas-is-blank
function isCanvasBlank() {
  const pixelBuffer = new Uint32Array(
    ctx.getImageData(0, 0, canvas.width, canvas.height).data.buffer
  );

  return !pixelBuffer.some(color => color !== 0);
}

// Swap between drawing mode and eraser mode.
// E.g swaps the colour to white or red.
function eraseDraw() {
  if (ctx.strokeStyle == '#ff0000'){
    ctx.strokeStyle = '#ffffff';
    document.getElementById("mode").innerHTML = "Mode: Erase";
  }
  else {
    ctx.strokeStyle = '#ff0000';
    document.getElementById("mode").innerHTML = "Mode: Draw";
  }
}

// Set the size of the pen using the value from the slider.
function setSize() {
  ctx.lineWidth = document.getElementById("size").value;
  document.getElementById("sizeText").innerHTML = "Size: ".concat(document.getElementById("size").value);
}

// == SERVER CONNECTION ==
// Called when Predict button is clicked.
function predictImage() {

  // Check if canvas is blank, if so then output error message. If not send to server.
  if(isCanvasBlank()){
    document.getElementById("result").innerHTML = "Canvas is blank, please draw a digit from 0-9.";
  }
  else {
    // To convert the canvas to an image I found a built in method which converts it to base64 binary, 
    // which will allow me to send the image to the flask server using AJAX
    // https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement/toDataURL
    var dataURL = canvas.toDataURL();
    var obj = {'data': dataURL};

    // I wanted to create an asynchronous request to the server and from research I found that using 
    // an xhttp AJAX request would work well. This will send the image and return the result when ready.
    // Code adapted from: https://www.w3schools.com/xml/ajax_xmlhttprequest_send.asp

    var xhttp = new XMLHttpRequest();

    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
        document.getElementById("result").innerHTML = this.responseText;
        }
    };

    // Open request and sent base64 string, then wait for response above.
    xhttp.open("POST", "/predictImage", true);
    xhttp.setRequestHeader('Content-Type', 'application/json');
    xhttp.send(JSON.stringify(obj));
  }
}