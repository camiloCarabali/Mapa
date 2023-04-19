///crea scripts para las diferentes actiones de los marker mostrar informacion al dar click, colocar coordenadas,acciones de eliminar y inabilitar
window.addEventListener('load', function() {
var markers = document.querySelectorAll('.marker');
var infoContainers = document.querySelectorAll('.info-container');

markers.forEach(function(marker) {
  var top = Math.floor(Math.random() * 100) + '%';
  var left =  Math.floor(Math.random() * 100) + '%';
  marker.style.top = top;
  marker.style.left = left;

  marker.addEventListener('click', function() {
    var id = this.getAttribute('id');
    var infoContainer = document.getElementById(id + '-info');

    // Ocultar todos los contenedores de información
    infoContainers.forEach(function(container) {
      container.style.display = 'none';
    });
    
var mapContainer = document.getElementById(id + '-info');
mapContainer.addEventListener('click', function() {
// Ocultar todos los contenedores de información
infoContainers.forEach(function(container) {
  container.style.display = 'none';
});
});

    // Mostrar el contenedor de información correspondiente
    infoContainer.style.display = 'block';



    // Agregar evento para el botón de editar
    var editButton = infoContainer.querySelector('.edit-button');
editButton.addEventListener('click', function() {
// Redirigir a la página de edición
window.location.href = "/actualizacionEmpresa/" + id;
});

    // Agregar evento para el botón de borrar
    var deleteButton = infoContainer.querySelector('.delete-button');
deleteButton.addEventListener('click', function() {
// Mostrar una ventana emergente de confirmación
var confirmDelete = confirm("¿Desea inactivar esta empresa?");

// Si el usuario confirma, redirigir a la página de inactivación
if (confirmDelete) {
  window.location.href = "/inactivarEmpresa/" + id;
}
});


  });
});
});