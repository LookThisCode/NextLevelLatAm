package nextlevel.desafio2;

import android.os.Bundle;
import com.google.android.maps.MapActivity;
import com.google.android.maps.MapView;

public class Desafio_2Activity extends MapActivity {
    
	MapView mapView;
	
    @Override
    protected void onCreate(Bundle icicle) {
        super.onCreate(icicle);
        setContentView(R.layout.main);
        
      //puntero al mapview
        mapView =(MapView)findViewById(R.id.map_view);
        
        mapView.setBuiltInZoomControls(true);
                
        //puntero al mapcontroller
        MapController myMapController = mapView.getController();
                
        List<Overlay> mapOverlays = mapView.getOverlays();
        
        Drawable drawable = this.getResources().getDrawable(R.drawable.logo_mapa);
    }
    
    @Override
    protected boolean isRouteDisplayed() {
        return false;
    }
}