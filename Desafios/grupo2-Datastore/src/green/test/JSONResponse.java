package green.test;

import java.util.ArrayList;
import java.util.List;

import com.google.gson.annotations.Expose;

public class JSONResponse {

	@Expose private List<InterestPoint> resultados = new ArrayList<InterestPoint>();
	@Expose private int numberOfErrors = 0;
	@Expose private String errorDescription;
	 
	public void addResultado(InterestPoint resultado)
	{
		resultados.add(resultado);

		//Collections.sort(resultados);
	}
	
	public void setError(String s_Error)
	{
		numberOfErrors++;
		errorDescription = s_Error;
	}
	
	public boolean errorHappened()
	{
		return (numberOfErrors != 0 ? true : false);
	}
	
	public String getErrorDescription()
	{
		return errorDescription;
	}
	
	public boolean isEmpty()
	{
		return resultados.isEmpty();
	}
	
	public List<InterestPoint> getResultados()
	{
		return resultados;
	}
	
	public InterestPoint getResultado(int i)
	{
		return resultados.get(i);
	}
}
