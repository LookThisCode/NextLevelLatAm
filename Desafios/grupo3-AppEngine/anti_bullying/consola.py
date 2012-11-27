import os
from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from random import randint

class MainPage(webapp.RequestHandler):
    def get(self):
        user = users.get_current_user()

        if user:
            #self.response.headers['Content-Type'] = 'text/plain'
            template_values = {
            'nombre_usuario': user,
            'supervisadas': [ 'cuenta%s' % randint(0,9) for i in range(randint(0,4))]
            }

            path = os.path.join(os.path.dirname(__file__), 'templates/anti-bullying.html')
            self.response.out.write(template.render(path, template_values))
        else:
            self.redirect(users.create_login_url(self.request.uri))

application = webapp.WSGIApplication(
                                     [('/', MainPage)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()