<script async
        src="https://maps.googleapis.com/maps/api/js?key=8HUHva85FBimn_ZS79U3M5EzLJQ=&callback=console.debug&libraries=maps,marker&v=beta">
</script>

function iniciarMap() {
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