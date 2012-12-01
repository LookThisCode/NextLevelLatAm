from gcmmod import GCM
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import json
import logging
class MainPage(webapp.RequestHandler):
    def post(self):
        gcm = GCM('AIzaSyD4S2STRZjjAlzg3CyJUOXyUUrbkt3xyBc')
        reg_ids = ['APA91bEuNsgB_0j-yV9RygkkTnQ7e63yMHXp29RbOuVr4aCaPOHhEei9DyAL0YaTniG8-8jkp5h5avmhq1Kb8HFtwKqDBRbmWUlAgcJUayUcH5nZE9DzNXA6cOBLa5B5bYLFGouDj2EAweEiX_UHhsmOiRQu6_9HwCn6sDmzCRJbXMM_Cb57u2I']

        # reg_ids = [str(self.request.get('registration_id'))]
        # data = {'text':'%s||%s||%s'}
        logging.info(self.request.body)
        data = {'text':str(self.request.get('text')),
                'code':str(self.request.get('code')),
                'level':str(self.request.get('level')),
                'victims':str(self.request.get('victims')),
                'scrapper':str(self.request.get('scrapper'))}
        logging.info(data)
        res = gcm.json_request(registration_ids=reg_ids, 
                               data=data,collapse_key='antibullying_notifier',
                               delay_while_idle=False, time_to_live=3600)  
        self.response.out.write(json.dumps(dict(results={'status':res}))) 
    
    # def get(self):
    #     data = {'text':self.request.get('text')}
    #     gcm = GCM('AIzaSyD4S2STRZjjAlzg3CyJUOXyUUrbkt3xyBc')
    #     reg_ids = ['APA91bEuNsgB_0j-yV9RygkkTnQ7e63yMHXp29RbOuVr4aCaPOHhEei9DyAL0YaTniG8-8jkp5h5avmhq1Kb8HFtwKqDBRbmWUlAgcJUayUcH5nZE9DzNXA6cOBLa5B5bYLFGouDj2EAweEiX_UHhsmOiRQu6_9HwCn6sDmzCRJbXMM_Cb57u2I']
    #     res=gcm.json_request(
    #     registration_ids=reg_ids, data=data,
    #     collapse_key='antibullying_notifier', delay_while_idle=False, time_to_live=3600)
    #     self.response.out.write(json.dumps(dict(results={'status':'ok'}))) 

application = webapp.WSGIApplication(
                                     [('/notifier/broadcast', MainPage)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
