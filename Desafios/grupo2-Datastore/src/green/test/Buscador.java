package green.test;

import javax.jws.WebMethod;
import javax.jws.WebService;

import java.util.Date;
import com.google.appengine.api.datastore.DatastoreService;
import com.google.appengine.api.datastore.DatastoreServiceFactory;
import com.google.appengine.api.datastore.Entity;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.sun.tools.javac.util.Log;

@WebService
public class Buscador {
	DatastoreService datastore;

	public Buscador() {
		datastore = DatastoreServiceFactory.getDatastoreService();
	}

	@WebMethod
	public String BuscarPuntos(String postInfo) {

		JSONPost postData = null;
		gpsPoint gpsFrom = null;
		String categories = null;
		Double radious = (double) 1000;

		try {
			Gson gsonPost = new Gson();
			postData = gsonPost.fromJson(postInfo.toString(), JSONPost.class);

			gpsFrom = postData.getFromPoint();
			radious = postData.getRadious();
			categories = postData.getCategories();

			guardarBusqueda(gpsFrom, radious, categories);

		} catch (Exception exception) {
			return exceptionHandler(exception);
		}

		try {
			Gson gsonResponse = new GsonBuilder()
					.excludeFieldsWithoutExposeAnnotation().create();
			JSONResponse objRespuesta = new JSONResponse();

			objRespuesta = BuscarResultados(gpsFrom, radious);

			if (objRespuesta.isEmpty()) {

			}

			return gsonResponse.toJson(objRespuesta);

		} catch (Exception exception) {
			return exceptionHandler(exception);
		}

	}

	@SuppressWarnings("finally")
	private JSONResponse BuscarResultados(gpsPoint gpsFrom, Double radious)
			throws Exception {

		JSONResponse objRespuesta = new JSONResponse();

		try {

			InterestPoint interestPoint1 = new InterestPoint();
			interestPoint1.setDescription("Centro de reciclaje 1");
			interestPoint1.setDireccion("Vicente L—pez  600, Tandil");
			interestPoint1
					.setPosition(new gpsPoint("-37.303508", "-59.145309"));

			objRespuesta.addResultado(interestPoint1);

			InterestPoint interestPoint2 = new InterestPoint();
			interestPoint2.setDescription("Centro de reciclaje 2");
			interestPoint2.setDireccion("Roser 1200, Tandil");
			interestPoint2
					.setPosition(new gpsPoint("-37.328765", "-59.122135"));

			objRespuesta.addResultado(interestPoint2);

			InterestPoint interestPoint3 = new InterestPoint();
			interestPoint3.setDescription("Centro de reciclaje 3");
			interestPoint3.setDireccion("Vigil  1599");
			interestPoint3.setPosition(new gpsPoint("-37.29511", "-59.125912"));

			objRespuesta.addResultado(interestPoint3);

		} catch (Throwable t) {
			// TODO Auto-generated catch block
			throw new Exception("Error BuscarResultados: "
					+ t.getStackTrace().toString());
		} finally {
			return objRespuesta;
		}
	}

	private String exceptionHandler(Exception exception) {
		JSONResponse obj = new JSONResponse();
		Gson gsonResponse = new Gson();
		obj.setError(exception.toString());

		// log.severe("Error: " + exception.toString());

		return gsonResponse.toJson(obj);
	}

	private void guardarBusqueda(gpsPoint gpsFrom, Double radious, String categories) 
	{
		try {
			Entity busqueda = new Entity("BusquedasRealizadas");

			busqueda.setProperty("Ubicacion", gpsFrom);
			busqueda.setProperty("Radio", radious);
			busqueda.setProperty("Categorias", categories);

			Date date = new Date();
			busqueda.setProperty("Fecha", date);

			datastore.put(busqueda);
			
		} catch (Exception exception) {
		}
	}

}
