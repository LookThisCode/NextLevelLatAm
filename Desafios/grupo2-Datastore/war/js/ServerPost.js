var url = '../soaptest';

var gPosition = new Array();
var gMarkers = new Array();

function buscarLugares() {


    //Example of a xml request probably put this is the parameter 
    //var soapMessage = "<?xml version='1.0' encoding='utf-8'?>"; 
    var soapMessage = "<v:Envelope xmlns:i='http://www.w3.org/2001/XMLSchema-instance' "; 
    soapMessage += "xmlns:d='http://www.w3.org/2001/XMLSchema' "; 
    soapMessage += "xmlns:c='http://schemas.xmlsoap.org/soap/encoding/' "; 
    soapMessage += "xmlns:v='http://schemas.xmlsoap.org/soap/envelope/'> "; 
    soapMessage += "<v:Header />"; 
    soapMessage += "<v:Body>"; 
    //[Add your xml here] 
    soapMessage += "<n0:BuscarPuntos id='o0' c:root='1' xmlns:n0='http://green.team/'><arg0 i:type='d:string'>{'appVersion':'1.0.0','fromPoint':{";
    soapMessage += "'lat':" + myMarker.getPosition().lat() + ",'long':" + myMarker.getPosition().lng() + "},";
    soapMessage += "'radious':1000.0 }";
    soapMessage += "</arg0></n0:BuscarPuntos>"; 

    // -----------------
    soapMessage += "</v:Body>"; 
    soapMessage += "</v:Envelope>"; 

     $.ajax({ 
    	 type: 'POST', 
    	 url: url, 
    	 cache: false, 
    	 success: function(data){
            var json_result = $(data).find('return').text();
            var objJSON = JSON.parse(json_result);

            clearMap();
            $('#lugares').empty();
            
            if(objJSON.resultados.length != 0){
                for(var i = 0; i < objJSON.resultados.length; i++ )
                {
                    addResultado(i, objJSON.resultados[i]);
                }

                resizeMap();

            }else{
                alert("No se encontraron resultados");
                //$.mobile.changePage('#popupDialog','pop',false,true);
                //$('#popupNoResults').dialog();
            }

    	}, 
    	error: function(data){ 
    		var xml = data.xml; 
             alert("No Funciono");
    		//$.mobile.hidePageLoadingMsg();
            //[do something with the xml] 
        }, 
        contentType: 'text/xml', 
        data: soapMessage 
    }); 
}


function addResultado(index, item)
{
    gPosition[index] = new google.maps.LatLng(item.GPSposition.lat, item.GPSposition.long);

    var image = new google.maps.MarkerImage("./Images/mark_blue.png",
        new google.maps.Size(27.0, 34.0),
        new google.maps.Point(0, 0),
        new google.maps.Point(13.0, 17.0)
    );

    var shadow = new google.maps.MarkerImage("./Images/mark_shadow.png",
        new google.maps.Size(45.0, 34.0),
        new google.maps.Point(0, 0),
        new google.maps.Point(13.0, 17.0)
    );

    gMarkers[index] = new google.maps.Marker({
        position : gPosition[index],
        draggable : false,
        map: this.map,
        icon: image,
        animation : google.maps.Animation.DROP,
        shadow: shadow
    });
    
    $('#lugares').append('<li id="Lugar' + index + '"">' +
                        ('<div class="Image"></div>') +
                        ('<div class="Titulo">' + item.Description + '</div>') +
                        ('<div class="Direccion">' +  + '</div>') +
                '</li>');

    $('#Lugar' + index).click(function(e) {
            //setAsSelected(item)
            $(gMarkers).each(function(index) {
                gMarkers[index].setAnimation(null);
            });

            $('#Lugar' + index).addClass('selected');

            gMarkers[index].setAnimation(google.maps.Animation.BOUNCE);
    });

    $('#Lugar' + index).animate({"margin-top": "0px"}, "normal");


}


function clearMap()
{
    if (gMarkers != null) {
        for ( var z in gMarkers) {
            gMarkers[z].setMap(null);
        }
    }
}