function codeLatLng(textfield, Latitud, Longitud) {
    var lat = parseFloat(Latitud);
    var lng = parseFloat(Longitud);

    var latlng = new google.maps.LatLng(lat, lng);
    
    geocoder.geocode({
        'latLng' : latlng
    }, function(results, status) {
           if (status != "OK") {
               // Too fast, try again, with a small pause
               window.setTimeout(function(){window.setTimeout(codeLatLng(textfield, Latitud, Longitud), 500);}, 500);  
           } else {
                if (results[0]) {
                    var resultado = results[0].address_components[1].short_name
                    + "  " + results[0].address_components[0].short_name.split("-")[0];

                    if (textfield[0].type == "text") {
                        textfield.val(resultado);
                    } else {
                        $(textfield[0]).text(resultado);
                    }
                }
           }
    });
}

function getLatLng(marcador, address) {
    //address += ", Córdoba, Córdoba, Argentina";

    geocoder.geocode({
        'address' : address,
        'region' : 'AR'
    }, function(results, status) {
        if (status == google.maps.GeocoderStatus.OK) {
            marcador.setPosition(results[0].geometry.location);
            resizeMap();
        } else {
            alert("No se encontraron resultados.");
        }
    });
}