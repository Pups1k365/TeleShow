<?php
// URL изображения для сохранения
$imageUrl = 'http://pups1k.000.pe/player_images/299J9L9PR_mico.png';

// Имя файла, в котором будет сохранено изображение
$fileName = 'saved_image.png';

// Сохранение изображения из указанного URL
file_put_contents($fileName, file_get_contents($imageUrl));

// Показ изображения
echo '<img src="' . $fileName . '" alt="Saved Image">';
?>
