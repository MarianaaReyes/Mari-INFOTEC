// Script para el menú hamburguesa
const hamburgerBtn = document.getElementById('hamburgerBtn');
const menu = document.getElementById('menu');

// Verificar si el botón y el menú están presentes
if (hamburgerBtn && menu) {
  hamburgerBtn.addEventListener('click', function() {
    // Alternar la visibilidad del menú
    menu.classList.toggle('hidden');
  });
}
