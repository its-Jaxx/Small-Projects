let counter = 0; let frames = [
  // Each image will be one (1) frame, going top to bottom
  'image1.png',
  'image2.png',
  'image3.png',
  'image4.png',
  'image5.png'
]
window.onload = function() {
  setInterval(function() {
    document.getElementById('icon').href = frames[counter];
    if (counter < frames.length - 1)
      counter++
    else
      counter = 1;
  }, 5); // The number is the amount of ms each frame is displayed for.
};
