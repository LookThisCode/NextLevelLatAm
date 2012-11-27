package com.uerugo;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.Date;
import java.util.HashSet;
import java.util.Iterator;
import java.util.List;
import javax.persistence.EntityManager;
import javax.persistence.EntityTransaction;
import javax.servlet.http.*;
import org.datanucleus.store.types.sco.backed.Set;

import com.google.appengine.api.datastore.DatastoreService;
import com.google.appengine.api.datastore.DatastoreServiceFactory;
import com.google.appengine.api.datastore.PreparedQuery;
import com.google.appengine.api.datastore.Query;
import com.google.appengine.api.datastore.Query.Filter;
import com.google.appengine.api.datastore.Query.FilterOperator;
import com.google.appengine.api.datastore.Query.FilterPredicate;
import com.google.appengine.api.datastore.TransactionOptions;
import com.uerugo.model.Dates;
import com.uerugo.model.Event;
import com.uerugo.model.Location;
import com.uerugo.model.Type;
import com.uerugo.model.User;

@SuppressWarnings("serial")
public class UerugoServlet extends HttpServlet {
	public void doGet(HttpServletRequest req, HttpServletResponse resp)
			throws IOException {
		
		resp.setContentType("text/plain");
		resp.getWriter().println("Hello, world");
		EntityManager em = EMF.get().createEntityManager();
		
		javax.persistence.Query q = em.createQuery("Select p FROM User p where p.userName='test'");
		
		User u = null;
		Iterator it = q.getResultList().iterator();
		while(it.hasNext()){
			u = (User) it.next();
		}
		HashSet<Type> types = new HashSet<Type>();
		List<Dates> dates = new ArrayList<Dates>();
		dates.add(new Dates(Calendar.getInstance().getTime(),Calendar.getInstance().getTime()));
		types.add(new Type("test", "dasda"));

//		User u = new User("test","test","test","test");
		Location l = new Location(0f, 0f);
		Event e = new Event(u, l,"testDesc",100f,types,dates);
		TransactionOptions.Builder.withXG(true);
		em.persist(e);
		em.close();
	}
}
