var myPosition;
var myMarker;
var geocoder;
var map;
var expandedNav;

function loadScript() {
  var script = document.createElement("script");
  script.type = "text/javascript";
  script.src = "http://maps.googleapis.com/maps/api/js?key=AIzaSyC1ktRXMsjvfjxOtCDB2K1r9h8vSndY_kU&sensor=false&callback=initialize";
  document.body.appendChild(script);
}

function initialize() {

	var mapOptions = {
	  center: new google.maps.LatLng(-31.382139, -64.218334),
	  zoom: 13,
	  panControl: false,
	  zoomControl: false,
	  mapTypeControl: false,
	  scaleControl: false,
	  streetViewControl: false,
	  mapTypeId: google.maps.MapTypeId.ROADMAP
	};

	map = new google.maps.Map(document.getElementById("map_canvas"),
    	mapOptions);

	initializeMap();

	$('#field_searchlocation').keypress(function(event) {
		if (event.which == 13) {
			var direccionAbuscar = $('#field_searchlocation').val();
			getLatLng(myMarker, direccionAbuscar);
		}
	});

	$('#btn_from').click(function() {
		var direccionAbuscar = $('#field_searchlocation').val();
		getLatLng(myMarker, direccionAbuscar);
	});


}


function initializeMap(){

	expandedNav = true;

	myPosition = new google.maps.LatLng(-31.382139, -64.218334);
	//positionFinal = new google.maps.LatLng(-31.427669, -64.185106);

	$('#loadingDiv').hide() // hide it initially
	.ajaxStart(function() {
		$(this).show();
	}).ajaxStop(function() {
		$(this).hide();
	});

	geocoder = new google.maps.Geocoder();

	myMarker = new google.maps.Marker({
		map : map,
		draggable : true,
		animation : google.maps.Animation.DROP,
		position : myPosition
	});

	google.maps.event.addListener(myMarker, "dragend", function(event) {
		codeLatLng($("#field_searchlocation"), myMarker.position.lat(), myMarker.position.lng());
		buscarLugares();
	});

	$("#btn_pilas").click(function() {
		click_pilas();
	});

	readPosition();
}

function success(position) {
	myMarker.setPosition(new google.maps.LatLng(position.coords.latitude,
		position.coords.longitude));
	
	buscarLugares();
	codeLatLng($("#field_searchlocation"), myMarker.position.lat(), myMarker.position.lng());

}

function readPosition() {
	if (navigator.geolocation) {
		navigator.geolocation.getCurrentPosition(success);
	}
}

function click_pilas() {
	

}

function resizeMap() {

	var bounds = new google.maps.LatLngBounds();

	bounds.extend(myMarker.position);

	for(var i = 0; i < gPosition.length; i++ )
	{


		bounds.extend(gPosition[i]);
	}

	if (map != null) {
		map.fitBounds(bounds);
		map.panToBounds(bounds);
	}
}