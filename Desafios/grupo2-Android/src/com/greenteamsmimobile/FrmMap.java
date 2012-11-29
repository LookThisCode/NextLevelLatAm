package com.greenteamsmimobile;

import java.io.IOException;
import org.ksoap2.SoapEnvelope;
import org.ksoap2.serialization.SoapObject;
import org.ksoap2.serialization.SoapPrimitive;
import org.ksoap2.serialization.SoapSerializationEnvelope;
import org.ksoap2.transport.HttpTransportSE;
import org.xmlpull.v1.XmlPullParserException;
import com.google.android.maps.GeoPoint;
import com.google.android.maps.MapActivity;
import com.google.android.maps.MapController;
import com.google.android.maps.MapView;
import android.os.Bundle;
import android.view.View;
import android.widget.TextView;

public class FrmMap extends MapActivity {

	// Constantes para la invocacion del web service
	private static final String NAMESPACE = "http://green.team/";
	private static String URL = "http://green-team.appspot.com/greenteam";
	private static final String METHOD_NAME = "buscarLugar";
	private static final String SOAP_ACTION = "";

	// Declaracion de variables para consumir el web service
	private SoapObject request = null;
	private SoapSerializationEnvelope envelope = null;
	private SoapPrimitive resultsRequestSOAP = null;

	private MapView mvMap;
	private MapController mcMap;
	private final static int INIT_ZOOM = 15;
	private GeoPoint pointMapCenter;
	private final static double LATITUDE_TANDIL = -37.316728;
	private final static double LONGITUDE_TANDIL = -59.150398;
	private final static double EXP_MICRO = 1E6;
	private TextView lblInfo;

	@Override
	public void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		initComponents();
	}

	private void initComponents() {
		setContentView(R.layout.lyt_map);

		lblInfo = (TextView) this.findViewById(R.id.lblInfo);
		mvMap = (MapView) findViewById(R.id.mvRecyclingPoints);
		mvMap.setBuiltInZoomControls(true); // zoom

		pointMapCenter = new GeoPoint((int) (LATITUDE_TANDIL * EXP_MICRO),
				(int) (LONGITUDE_TANDIL * EXP_MICRO));

		mapCenter();
	}

	private void mapCenter() {
		mcMap = this.mvMap.getController(); // controler nos sirve para
													// hacer q se vea en
													// determinado lugar etc
		mcMap.setZoom(INIT_ZOOM);
		mcMap.animateTo(this.pointMapCenter);
	}

	public void btnRecycleSetOnClickListener(View button) {
		// Se crea un objeto SoapObject para poder realizar la peticion
		// para consumir el ws SOAP. El constructor recibe
		// el namespace. Por lo regular el namespace es el dominio
		// donde se encuentra el web service
		request = new SoapObject(NAMESPACE, METHOD_NAME);
		request.addProperty("arg0", "test");
		// Se crea un objeto SoapSerializationEnvelope para serealizar la
		// peticion SOAP y permitir viajar el mensaje por la nube
		// el constructor recibe la version de SOAP
		envelope = new SoapSerializationEnvelope(SoapEnvelope.VER11);
		envelope.dotNet = false; // se asigna true para el caso de que el WS sea
									// de dotNet

		// Se envuelve la peticion soap
		envelope.setOutputSoapObject(request);

		// Objeto que representa el modelo de transporte
		// Recibe la URL del ws
		HttpTransportSE transporte = new HttpTransportSE(URL);

		try {
			// Hace la llamada al ws
			transporte.call(SOAP_ACTION, envelope);

			// Se crea un objeto SoapPrimitive y se obtiene la respuesta
			// de la peticion
			resultsRequestSOAP = (SoapPrimitive) envelope.getResponse();
			lblInfo.setText("" + resultsRequestSOAP.toString());

		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (XmlPullParserException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	@Override
	protected boolean isRouteDisplayed() {
		return false;
	}
}
