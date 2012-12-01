package green.test;

import com.google.gson.annotations.Expose;
import com.google.gson.annotations.SerializedName;

public class gpsPoint {
	
	@Expose @SerializedName("lat") private Float mLatitude;
	@Expose @SerializedName("long") private Float mLongitude;
	
	public gpsPoint()
	{
		mLatitude = (float) 0;
		mLongitude = (float) 0;
	}
	
	public gpsPoint(String latitude,String longitude)
	{
		mLatitude = new Float(latitude);
		mLongitude = new Float(longitude);
	}
	
	public gpsPoint(String point)
	{
		String[] a = point.split("\\,");
		mLatitude = new Float(a[0].toString());
		mLongitude = new Float(a[1].toString());
	}
	
	public Float getLatitude()
	{
		return mLatitude;
	}
	
	public Float getLongitude()
	{
		return mLongitude;
	}
	
	public double distanceTo(gpsPoint pointTo) {
		float pk = (float) (180/3.14169);

		float a1 = mLatitude / pk;
		float a2 = mLongitude / pk;
		float b1 = pointTo.getLatitude() / pk;
		float b2 = pointTo.getLongitude() / pk;

		double t1 = Math.cos(a1)*Math.cos(a2)*Math.cos(b1)*Math.cos(b2);
		double t2 = Math.cos(a1)*Math.sin(a2)*Math.cos(b1)*Math.sin(b2);
		double t3 = Math.sin(a1)*Math.sin(b1);
		double tt = Math.acos(t1 + t2 + t3);

		return 6366000*tt;
	}
	
	@Override
	public String toString()
	{
		return mLatitude + "|" + mLongitude;
	}
}
