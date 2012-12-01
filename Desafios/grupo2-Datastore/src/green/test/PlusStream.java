package green.test;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

public class PlusStream {

	public String getData() {
		String address = "https://www.googleapis.com/plus/v1/people/113015103406590069311";
        String queryString = "key=AIzaSyC1ktRXMsjvfjxOtCDB2K1r9h8vSndY_kU";
        		
		String result = null;
        if (address.startsWith("http://")){
            try {
                String urlStr = address;
                if (queryString != null && queryString.length () > 0)    urlStr += "?" + queryString;
                HttpURLConnection httpUrlConnection = (HttpURLConnection) (new URL(urlStr)).openConnection();
                
                // Get the response
                BufferedReader rd = new BufferedReader(new InputStreamReader(httpUrlConnection.getInputStream()));
                StringBuilder data = new StringBuilder(150);
                String line;
                while ((line = rd.readLine()) != null)    data.append(line);
                rd.close();
                result = data.toString();
                httpUrlConnection.disconnect();
            } catch (Exception e){
                e.printStackTrace();
            }
        }
        
        return result;
    }
}
