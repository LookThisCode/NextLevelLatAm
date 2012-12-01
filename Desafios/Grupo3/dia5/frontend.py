import os
import logging
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import login_required
from models import *
from random import randint

class MainPage(webapp.RequestHandler):
    def get(self):
        user = users.get_current_user()
    
        #usuario = Watchers(federated_identity=user.federated_identity(), register_id='APA91bEuNsgB_0j-yV9RygkkTnQ7e63yMHXp29RbOuVr4aCaPOHhEei9DyAL0YaTniG8-8jkp5h5avmhq1Kb8HFtwKqDBRbmWUlAgcJUayUcH5nZE9DzNXA6cOBLa5B5bYLFGouDj2EAweEiX_UHhsmOiRQu6_9HwCn6sDmzCRJbXMM_Cb57u2I',notificacions=user.email,nickname='H4')
        #usuario.put()
        
        #@todo: Hay que verificar que el valor de federated_identity sea distint de None
        qs = Watchers.all()
        q = qs.filter('federated_identity =',user.federated_identity())[0]
        
        if user:
            #self.response.headers['Content-Type'] = 'text/plain'
            template_values = {
            	'nombre_usuario': q.nickname,
            	'supervisadas': ['cuenta%s' % randint(0,9) for i in range(randint(0,4))]
            }
            path = os.path.join(os.path.dirname(__file__), 'templates/anti-bullying.html')
            self.response.out.write(template.render(path, template_values))
        else:
            self.redirect(users.create_login_url(self.request.uri))