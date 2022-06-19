/*Web Developer needed for Rideshare App
Full Stack Development
Posted 1 day ago
Only freelancers located in the U.S. may apply.
Fully functioning website that collects users commuter 
information and stores in Database for route design. 
 Website will be selling bookable products. 
  Data Collected shall be pickup location,
   drop off location, Morning Arrival time, 
   Afternoon Pickup time.
   
   https://www.upwork.com/nx/jobs/search/details/~01866ee429607be712?q=java&sort=recency&user_location_match=1&t=1&amount=500-999&pageTitle=Job%20Detail&_navType=slider&_modalInfo=%5B%7B%22navType%22%3A%22slider%22,%22title%22%3A%22Job%20Detail%22,%22modalId%22%3A%221655584972837%22%7D%5D
   
   
   */

//RxJS
//AngularJS
//define a stream of data, and manipulate it to add a lambda function to store JSON data as parameter 
define storeStream = (stream, lambda) => {
    return stream.map(lambda);
}

//html
//display a map widget with google maps api , with key and save the location clicked to location.
<div id="map"></div>
<script>
    function initMap() {
        var map = new google.maps.Map(document.getElementById('map'), {
            center: { lat: -34.397, lng: 150.644 },
            zoom: 8
        });
        var infoWindow = new google.maps.InfoWindow({
            content: 'Click the map to save the location'
        });
        google.maps.event.addListener(map, 'click', function (event) {
            var lat = event.latLng.lat();
            var lng = event.latLng.lng();
            infoWindow.setPosition(event.latLng);
            infoWindow.open(map);
            document.getElementById('lat').value = lat;
            document.getElementById('lng').value = lng;
        });
    }
</script>

//html
//define a div section to display a label 'Arrival Time' a text input widget  with time variable and store the input as JSON data.
<div class="form-group">
    <label for="arrivalTime">Arrival Time</label>
    <input type="time" class="form-control" id="arrivalTime" name="arrivalTime" placeholder="Arrival Time">
</div>
//define function to store variable id arrivalTime as JSON data.as JSON object 'data'
function storeArrivalTime(id) {
    var data = {
        arrivalTime: document.getElementById(id).value
    };
    return data;
}

//html
//create a div section and display label, departure time and create text input for time variable and store the input as JSON data.
<div class="form-group">
    <label for="departureTime">Departure Time</label>   
    <input type="time" class="form-control" id="departureTime" name="departureTime" placeholder="Departure Time">

</div>
//javascript
//define function to store variable id departureTime , append JSON variable 'data'

function storeDepartureTime(id,data) {
    //define data as JSON type
    var data = {
        departureTime: document.getElementById(id).value
    };
    return data;
}


//javascript
//store JSON to a tinydb database on client browser
var db = new TinyDB('db.json');
db.save('location', { lat: lat, lng: lng });

//javascript
//define function to take a JSON as parameter and store on tinydb on server, with URI as parameter
function storeJSON(json, uri) {
    var xhr = new XMLHttpRequest();
    xhr.open('POST', uri, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify(json));
}

