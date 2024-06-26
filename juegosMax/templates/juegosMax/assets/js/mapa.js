<script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyDdv1mONGkKORSWGCcEe1L7p5atacKC0fQ&callback=initMap" async
        defer></script>

function initMap() {
    var coord = {lat: -33.4378243, lng: -70.6913352};
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 10,
        center: coord
    });
    var marker = new google.maps.Marker({
        position: coord,
        map: map
    });
}