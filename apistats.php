<?php
  $imageUrl = "https://www.brawltime.ninja/api/render/profile/299J9L9PR/bibi.png?background=cartoon_lobby.jpg";
  
  // Скачиваем изображение и отправляем его для скачивания
  $imageData = file_get_contents($imageUrl);
  header('Content-Type: application/octet-stream');
  header("Content-Transfer-Encoding: Binary"); 
  header("Content-disposition: attachment; filename=\"bibi_image.png\""); 
  echo $imageData;
?>
