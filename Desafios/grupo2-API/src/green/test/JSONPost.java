package green.test;

public class JSONPost {
	private String appVersion;
	private gpsPoint fromPoint;
	private Double radious;
	
	//Creator
	public void newPost(String s_appVersion, String s_fromPoint, Double d_radious)
	{
		appVersion = s_appVersion;
		fromPoint = new gpsPoint(s_fromPoint);
		radious = d_radious;
	}
	
	//Geters
	public String getAppVersion()
	{
		return appVersion;
	}
	
	public gpsPoint getFromPoint()
	{
		return fromPoint;
	}
	
	public Double getRadious()
	{
		return radious;
	}
}
