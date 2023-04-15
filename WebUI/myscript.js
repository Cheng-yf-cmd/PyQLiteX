function upload() {
  const input = document.getElementById('fileInput');
  if (!input || !input.files || input.files.length === 0) {
    alert('Please select a file!');
    return;
  }
  var name = "File name:";
  if('name' in input.files[0]){
    name += input.files[0].name;
  }
  var size = "File size:";
  if('size' in input.files[0]){
    size += input.files[0].size;
  }
  const reader = new FileReader();
  reader.onload = function (event) {
    const text = event.target.result;
    const div = document.createElement('div');
    div.textContent = text;
    document.getElementById('showText').replaceChild(div,div);
  };
  reader.readAsText(input.files[0]);
  document.getElementById('Filename').style.display = '';
  document.getElementById('Filename').innerHTML = name;
  document.getElementById('Filesize').style.display = '';
  document.getElementById('Filesize').innerHTML = size + 'B';
}

function loadJSON(callback) {
  var xobj = new XMLHttpRequest();
      xobj.overrideMimeType("application/json");
  xobj.open('GET', 'demo.json', true);
  xobj.onreadystatechange = function () {
        if (xobj.readyState == 4 && xobj.status == "200") {
          callback(JSON.parse(xobj.responseText));
        }
  };
  xobj.send(null);
}

loadJSON(function(json) {
console.log(json);
});