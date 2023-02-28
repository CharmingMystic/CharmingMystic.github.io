function showAlert() {
  alert('Hello, world!');
}

window.onload = function() {
  // Initialize map
  var map = L.map('map').setView([53.7531, 15.6229], 9);

  // Add tile layer to map
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors',
    maxZoom: 18,
  }).addTo(map);

  // Add marker to map
  var marker = L.marker([53.4289, 14.5528]).addTo(map);
  marker.bindPopup("<b>Stargard</b><br>Zachodniopomorskie");

  // Add circle to map
  var circle = L.circle([53.5804, 16.6378], {
    color: 'red',
    fillColor: '#f03',
    fillOpacity: 0.5,
    radius: 5000
  }).addTo(map);
  circle.bindPopup("Koszalin<br>Zachodniopomorskie");
};
