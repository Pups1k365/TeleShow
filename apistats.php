<?php
  $playerId = $_GET['player_id'];
  $imageType = $_GET['type'];
  $imageUrl = "https://www.brawltime.ninja/api/render/profile/{$playerId}/{$imageType}.png?background=cartoon_lobby.jpg";
  
  // Сохраняем изображение на хостинге
  $imageData = file_get_contents($imageUrl);
  file_put_contents("player_images/{$playerId}_{$imageType}.png", $imageData);

  // Открываем изображение на новой странице
  echo "<html>";
  echo "<body>";
  echo "<img src='player_images/{$playerId}_{$imageType}.png'>";
  echo "</body>";
  echo "</html>";
?>
