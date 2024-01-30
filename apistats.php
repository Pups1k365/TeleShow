<?php
  $playerId = $_GET['player_id'];
  $imageType = $_GET['type'];
  $imageUrl = "https://www.brawltime.ninja/api/render/profile/{$playerId}/{$imageType}.png?background=cartoon_lobby.jpg";
  
  // Скачиваем изображение и отправляем его для скачивания
  $imageData = file_get_contents($imageUrl);
  header('Content-Type: application/octet-stream');
  header("Content-Transfer-Encoding: Binary"); 
  header("Content-disposition: attachment; filename=\"{$playerId}_{$imageType}.png\""); 
  echo $imageData;
?>
