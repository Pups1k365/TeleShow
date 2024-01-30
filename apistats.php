<?php
    $file = 'https://www.brawltime.ninja/api/render/profile/299J9L9PR/kit.png?background=brawl_stars_lobby.jpg';
    header('Content-Description: File Transfer');
    header('Content-Type: application/octet-stream');
    header('Content-Disposition: attachment; filename="'.basename($file).'"');
    readfile($file);
?>
