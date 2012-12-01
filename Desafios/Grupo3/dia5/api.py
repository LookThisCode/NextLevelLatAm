from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import login_required
from google.appengine.ext import db
from models import *
import json
import logging



class BullyingHandler(webapp.RequestHandler):

	def get(self, supervisor_id=None):
		#w = db.GqlQuery('SELECT * FROM watcher WHERE __key__ = '+supervisor_id)
		qs = Bullying.all().filter('watcher =', supervisor_id)
		reports = []
		for q in qs:
			reports.append({
					'code': q.code,
					'victimas': q.victimas,
					'contenido': q.contenido,
					'status': q.status,
					'level': q.level
				})
		self.response.headers['Content-Type'] = 'application/javascript'
		self.response.out.write(json.dumps({'results': reports}))

	def post(self):
		code = self.request.get('code')
		content = self.request.get('content')
		victims = self.request.get('victims').split(',')
		scrapper = self.request.get('scrapper')
		level = self.request.get('level')
		try:
			scrap = Scrappers.all().filter('uid',str(scrapper)).get()[0]
		except:
			scrap = Scrappers(uid=scrapper,ranking=0.0)
			scrap.put()

		for s in Supervisados.all().filter('uid IN', victims):
			b = Bullying(code=code,
                		victimas=[s.uid],
                		contenido=content, 
                		agresores=scrap,
                		supervisado=s,
                		level=int(level),
                		watcher=s.watcher)
			b.put()
		self.response.out.write(json.dumps({'results':'ok'}))

	def put(self, code):
		q = Bullying.all().filter('code =',code)[0]
		q.status = 1
		q.level = self.request.get('level')
		q.put()
		self.response.headers['Content-Type'] = 'application/javascript'
		self.response.out.write(json.dumps({'results':'ok'}))


class SupervisorHandler(webapp.RequestHandler):

	def get(self):
		qs = Supervisados.all()
		response = []
		for w in qs:
			response.append(w.uid)
		self.response.out.write(json.dumps({'results':response}))

		
	def post(self):
		user = users.get_current_user()
		try:
			w = Watchers.all()[0]
		except:
			w = Watchers(federated_identity=user.federated_identity(), register_id='APA91bEuNsgB_0j-yV9RygkkTnQ7e63yMHXp29RbOuVr4aCaPOHhEei9DyAL0YaTniG8-8jkp5h5avmhq1Kb8HFtwKqDBRbmWUlAgcJUayUcH5nZE9DzNXA6cOBLa5B5bYLFGouDj2EAweEiX_UHhsmOiRQu6_9HwCn6sDmzCRJbXMM_Cb57u2I',notificacions=user.email,nickname='H4')
        	w.put()
		uid = self.request.get('uid')
		# s = SocialNetworks(code=1,name='twitter')
		# s.put()
		sup = Supervisados(uid=str(uid),watcher=w)
		sup.put()
		self.response.out.write(json.dumps({'results':'ok'}))


	def delete(self, bullying_id):
		raise NotImplementedError()

class ScrappersHandler(webapp.RequestHandler):

	def get(self, scrapper_id):
		qs = Scrappers.all().filter('uid =', supervisor_id)[0]
		self.response.headers['Content-Type'] = 'application/javascript'
		self.response.out.write({'results':dict(ranking=qs.ranking)})

		
