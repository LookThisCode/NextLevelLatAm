package green.test;

import green.test.jaxws.*;

public class BuscadorAdapter {
	  private Buscador buscador = new Buscador();

	  public BuscarPuntosResponse sayHello(BuscarPuntos request){
	    String name = request.getArg0();
	    String responseGreeting = buscador.BuscarPuntos(name);
	    BuscarPuntosResponse response = new BuscarPuntosResponse();
	    response.setReturn(responseGreeting);
	    return response;
	  }
}
