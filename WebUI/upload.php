<?php
if(isset($_FILES['folder'])){
    $folderName = $_FILES['folder']['name'][0];
    $folderPath = './uploads/' . $folderName;

    if(move_uploaded_file($_FILES['folder']['tmp_name'][0], $folderPath)){
        echo "上传成功！";
    } else {
        echo "上传失败！";
    }
}
?>