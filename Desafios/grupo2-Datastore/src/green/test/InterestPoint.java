package green.test;

import com.google.gson.annotations.Expose;

public class InterestPoint {
	private String id;
	@Expose private String Description;
	@Expose private String Direccion;
	@Expose private String Category;
	@Expose private gpsPoint GPSposition;
	
	public InterestPoint(){
	}
	
	public void setDescription(String d_description){
		Description = d_description;
	}
	
	public String getDescription(){
		return Description;
	}
	
	public void setDireccion(String d_direccion){
		Direccion = d_direccion;
	}
	
	public String getDireccion(){
		return Direccion;
	}
	
	public void setPosition(gpsPoint d_position){
		GPSposition = d_position;
	}
	
	public gpsPoint getPosition(){
		return GPSposition;
	}
	
	
	
}
