
canvas.addEventListener('mousedown', function (e) {
    context.moveTo(mouse.x, mouse.y);
    context.beginPath();
    canvas.addEventListener('mousemove', onPaint, false);
}, false); var onPaint = function () {
    context.lineTo(mouse.x, mouse.y);
    context.stroke();
};
  
canvas.addEventListener('mouseup', function () {
    $('#number').html('<img id="spinner" src="spinner.gif"/>');
    canvas.removeEventListener('mousemove', onPaint, false);
    var img = new Image();
    img.onload = function () {
        context.drawImage(img, 0, 0, 28, 28);
        data = context.getImageData(0, 0, 28, 28).data;
        var input = [];
        for (var i = 0; i < data.length; i += 4) {
            input.push(data[i + 2] / 255);
        }
        predict(input);
    };
    img.src = canvas.toDataURL('image/png');
}, false);
  
// Setting up tfjs with the model we downloaded
tf.loadLayersModel(' model.json')
    .then(function (model) {
        window.model = model;
    });
  
// Predict function
var predict = function (input) {
    if (window.model) {
        window.model.predict([tf.tensor(input)
            .reshape([1, 28, 28, 1])])
            .array().then(function (scores) {
                scores = scores[0];
                predicted = scores
                    .indexOf(Math.max(...scores));
                $('#number').html(predicted);
            });
    } else {
  
        // The model takes a bit to load, 
        // if we are too fast, wait
        setTimeout(function () { predict(input) }, 50);
    }
}