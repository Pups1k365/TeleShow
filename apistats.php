<?php
  $imageUrl = "https://www.brawltime.ninja/api/render/profile/299J9L9PR/bibi.png?background=cartoon_lobby.jpg";
  
  // Скачиваем изображение и отправляем его для скачивания
  $imageData = file_get_contents($imageUrl);
  header('Content-Type: image/png');
  header('Content-Disposition: attachment; filename="bibi_image.png"');
  echo $imageData;
?>
