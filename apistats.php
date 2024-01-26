<?php
// URL изображения для сохранения
$imageUrl = 'http://pups1k.000.pe/player_images/299J9L9PR_mico.png';

// Сохранение изображения в локальный файл
$localImage = 'saved_image.png';
file_put_contents($localImage, file_get_contents($imageUrl));

// Отображение сохраненного изображения
echo '<img src="' . $localImage . '" alt="Saved Image">';
?>
