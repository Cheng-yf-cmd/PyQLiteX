function upload() {
  var fileInput = document.getElementById("fileInput");
  var files = fileInput.files;
  var formData = new FormData();
  for (var i = 0; i < files.length; i++) {
      formData.append("file", files[i]);
  }
  var xhr = new XMLHttpRequest();
  xhr.upload.addEventListener("progress", function (evt) {
      if (evt.lengthComputable) {
          var percentComplete = evt.loaded / evt.total;
          percentComplete = parseInt(percentComplete * 100);
          var progressBar = document.getElementById("progressBar");
          progressBar.style.width = percentComplete + "%";
          progressBar.innerHTML = percentComplete + "%";
      }
  }, false);
  xhr.addEventListener("load", function () {
      alert("上传完成！");
  }, false);
  xhr.addEventListener("error", function () {
      alert("上传失败！");
  }, false);
  xhr.open("POST", "upload.php");
  xhr.send(formData);
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

loadJSON(function (json) {
  console.log(json);
});