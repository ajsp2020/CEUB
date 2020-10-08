document.addEventListener('DOMContentLoaded', function(){
    fetch("http://www.geoplugin.net/json.gp?")
    .then(response => response.json())
    .then(data => {
        const rate = data.geoplugin_city;
        document.querySelector('#loc').innerHTML = rate;
    });
    
});

document.addEventListener('DOMContentLoaded', function(){
    fetch("http://www.geoplugin.net/json.gp?")
    .then(response => response.json())
    .then(data => {
        const rate = data.geoplugin_regionCode;
        document.querySelector('#reg').innerHTML = rate;
    });
    
});

/* Fazer imagem mudar
var picPaths = ["static/web/imagens/foto1.jpg"];
var imageIndex = 1;
var bannerImage;

function startInterval() {
    setInterval(displayNextImage, 20000);

}

function displayNextImage() {
    bannerImage.src = picPaths[imageIndex];
    if(imageIndex === (picPaths.length -1)) {
        imageIndex = 0;
    }
    else {
        imageIndex = imageIndex + 1;
    }
}


window.onload=function() {
    bannerImage = document.getElementById('imgBanner');
    startInterval();
}
*/

