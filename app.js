const playerId = window.location.pathname.split('/')[1];
const imageType = window.location.pathname.split('/')[2];

if (!playerId || !imageType) {
  console.error('Invalid player ID or image type');
  return;
}

const baseUrl = 'https://www.brawltime.ninja/api/render/profile/';
const params = `player_id=${playerId}/${image_type}.png?background=cartoon_lobby.jpg`;
const imageUrl = `${baseUrl}${params}`;

fetch(imageUrl)
  .then((response) => {
    if (!response.ok) {
      throw new Error('Error fetching image');
    }
    return response.blob();
  })
  .then((blob) => {
    const playerImage = document.getElementById('player-image');
    const imageUrl = URL.createObjectURL(blob);
    playerImage.innerHTML = `<img src="${imageUrl}" alt="Player ${playerId} - ${imageType} image">`;
  })
  .catch((error) => {
    console.error('Error:', error);
  });
