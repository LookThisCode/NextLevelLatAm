from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import login_required
from google.appengine.ext import db
from models import *


class BullyingHandler(webapp.RequestHandler):

	def get(self, supervisor_id):
		w = db.GqlQuery('SELECT * FROM watcher WHERE __key__ = ')
		qs = Bullying.all().filter('watcher =', supervisor_id).get()
		reports = []
		for q in qs:
			reports.append({
					'code': q.code,
					'victimas': q.victimas,
					'contenido': q.contenido,
					'status': q.status,
					'level': q.level
				})

	def put(self, bullying_id):
		raise NotImplementedError()

class SupervisorHandler(webapp.RequestHandler):

	def get(self, supervisor_id):
		raise NotImplementedError()

	def post(self):
		raise NotImplementedError()

	def delete(self, bullying_id):
		raise NotImplementedError()

class ScrappersHandler(webapp.RequestHandler):

	def get(self, supervisor_id):
		raise NotImplementedError()
