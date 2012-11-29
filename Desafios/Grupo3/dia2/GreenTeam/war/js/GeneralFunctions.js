var positionInicio;
var geocoder;
var map;


function initialize() {
	var mapOptions = {
	  center: new google.maps.LatLng(-31.382139, -64.218334),
	  zoom: 8,
	  mapTypeId: google.maps.MapTypeId.ROADMAP
	};
	map = new google.maps.Map(document.getElementById("map_canvas"),
    	mapOptions);

	initializeMap();
}


function initializeMap(){

	positionInicio = new google.maps.LatLng(-31.382139, -64.218334);
	//positionFinal = new google.maps.LatLng(-31.427669, -64.185106);


	$('#loadingDiv').hide() // hide it initially
	.ajaxStart(function() {
		$(this).show();
	}).ajaxStop(function() {
		$(this).hide();
	});

	geocoder = new google.maps.Geocoder();

	markerInicio = new google.maps.Marker({
		map : map,
		draggable : true,
		animation : google.maps.Animation.DROP,
		position : positionInicio
	});

	google.maps.event.addListener(markerInicio, 'mousedown', function() {
		google.maps.event.trigger(map, "resize");
	});

	//resizeMap();

	google.maps.event.addListener(markerInicio, "dragend", function(event) {
		codeLatLng($("#search-from"), markerInicio.position.lat(), markerInicio.position.lng());
	});

	readPosition();
}

function success(position) {
	markerInicio.setPosition(new google.maps.LatLng(position.coords.latitude,
		position.coords.longitude));
	resizeMap();
}

function readPosition() {
	if (navigator.geolocation) {
		navigator.geolocation.getCurrentPosition(success);
	}
}

function resizeMap() {
	var bounds = new google.maps.LatLngBounds();
	bounds.extend(markerInicio.position);
	//bounds.extend(markerFinal.position);

	if (map != null) {
		map.fitBounds(bounds);
		map.panToBounds(bounds);
	}
}