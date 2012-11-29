import datetime
from google.appengine.ext import db


class SocialNetworks(db.Model):
    code = db.IntegerProperty(required=True)
    name = db.StringProperty(required=True)

class Scrappers(db.Model):
	#Agresores
    uid = db.StringProperty()
    ranking = db.FloatProperty()
    social_network = db.ReferenceProperty(SocialNetworks)
    
class Watchers(db.Model):
	#Padre
    federated_identity = db.StringProperty()
    register_id = db.StringProperty()
    notifications = db.EmailProperty()
    nickname = db.StringProperty()

class Supervisados(db.Model):
	#Hijo
    watcher = db.ReferenceProperty(Watchers)
    uid = db.StringProperty()
    social_network = db.ReferenceProperty(SocialNetworks)

class Bullying(db.Model):
	#reporte
    code = db.StringProperty()
    victimas = db.StringListProperty() 
    contenido = db.StringProperty()
    agresores = db.ReferenceProperty(Scrappers)
    supervisado = db.ReferenceProperty(Supervisados)
    status = db.IntegerProperty(default=0)
    level = db.IntegerProperty(default=0)
    dateTime = db.DateTimeProperty(auto_now_add=True)
    modif = db.DateTimeProperty(auto_now=True)
    watcher = db.ReferenceProperty(Watchers)