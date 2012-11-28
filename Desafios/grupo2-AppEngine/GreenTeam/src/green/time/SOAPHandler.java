package green.time;
import java.util.Iterator;

import javax.xml.bind.JAXB;
import javax.xml.namespace.QName;
import javax.xml.soap.MessageFactory;
import javax.xml.soap.SAAJResult;
import javax.xml.soap.SOAPBody;
import javax.xml.soap.SOAPElement;
import javax.xml.soap.SOAPException;
import javax.xml.soap.SOAPFault;
import javax.xml.soap.SOAPMessage;
import javax.xml.transform.dom.DOMSource;


public class SOAPHandler {

  private static final String NAMESPACE_URI = "http://green.team/";
  private static final QName SAY_HELLO_QNAME = new QName(NAMESPACE_URI, "buscarLugares");

  private static MessageFactory messageFactory;
  private static SearchAdapter searchAdapter;

  public SOAPHandler() throws SOAPException {
    messageFactory = MessageFactory.newInstance();
    searchAdapter = new SearchAdapter();
  }

  public static SOAPMessage handleSOAPRequest(SOAPMessage request) throws SOAPException {
    SOAPBody soapBody = request.getSOAPBody();
    Iterator iterator = soapBody.getChildElements();
    Object responsePojo = null;
    while (iterator.hasNext()) {
      Object next = iterator.next();
      if (next instanceof SOAPElement) {
        SOAPElement soapElement = (SOAPElement) next;
        QName qname = soapElement.getElementQName();
          if (SAY_HELLO_QNAME.equals(qname)) {
            responsePojo = handleSayHelloRequest(soapElement);
            break;
          } 
      }
    }
    SOAPMessage soapResponse = messageFactory.createMessage();
    soapBody = soapResponse.getSOAPBody();
    if (responsePojo != null) {
      JAXB.marshal(responsePojo, new SAAJResult(soapBody));
    } else {
      SOAPFault fault = soapBody.addFault();
      fault.setFaultString("Unrecognized SOAP request.");
    }
    return soapResponse;
  }

  private static Object handleSayHelloRequest(SOAPElement soapElement) {
    BuscarPuntos sayHelloRequest = JAXB.unmarshal(new DOMSource(soapElement), BuscarPuntos.class);
    return searchAdapter.buscarPuntos();
  }
}