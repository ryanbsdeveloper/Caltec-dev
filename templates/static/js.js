var senha1 = $('#senha1');
var olho1 = $("#eye1");

olho1.mousedown(function() {
  senha1.attr("type", "text");
});

olho1.mouseup(function() {
  senha1.attr("type", "password");
});
