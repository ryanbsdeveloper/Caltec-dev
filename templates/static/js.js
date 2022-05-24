var senha1 = $('#senha1');
var olho1 = $("#eye1");

olho1.mousedown(function() {
  senha1.attr("type", "text");
});

olho1.mouseup(function() {
  senha1.attr("type", "password");
});

var senha2 = $('#senha2');
var olho2 = $("#eye2");

olho2.mousedown(function() {
  senha2.attr("type", "text");
});

olho2.mouseup(function() {
  senha2.attr("type", "password");
});

