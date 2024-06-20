// Función para crear el slider de imágenes
function crearSlider() {
    var imageContainer = document.querySelector('.image-container');
    var images = imageContainer.getElementsByTagName('img');
    var currentIndex = 0;
    
    // Función para mostrar la imagen actual
    function showCurrentImage() {
        for (var i = 0; i < images.length; i++) {
        images[i].style.display = 'none';
        }
        images[currentIndex].style.display = 'block';
    }
    
    // Función para avanzar al siguiente slide
    function nextSlide() {
        currentIndex++;
        if (currentIndex >= images.length) {
        currentIndex = 0;
        }
        showCurrentImage();
    }
    
    // Iniciar el slider
    showCurrentImage();
    setInterval(nextSlide, 3000); // Cambiar la imagen cada 3 segundos
    }
    
  // Llamar a la función para crear el slider
    crearSlider();
    