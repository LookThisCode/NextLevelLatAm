#!/usr/bin/env python
#
# Copyright 2012 Google Inc.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Author: Marc Cohen

'''Configures all page handlers for the application.'''

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from home import BackendPage
from home import AuthHandler
from home import Reset 
from api import *
from frontend import *
from predict import PredictAPI

application = webapp.WSGIApplication(
  [ ('/',ScrappersHandler),
    (r'/scrappers/(P?<agresor_id>)/',ScrappersHandler),
    (r'/supervisados/(P?<supervisado_id>)/', SupervisorHandler),
    (r'/supervisados/(P?<supervisado_id>)/bullying', BullyingHandler),
    (r'/bullying/(P?<bullying_id>)/', BullyingHandler),
    ('/backend/', BackendPage),
    ('/backend/reset', Reset),
    ('/backend/auth_return', AuthHandler),
    ('/backend/predict', PredictAPI),
  ],
  debug=True)

def main():
  '''Runs the application.'''
  run_wsgi_app(application)

if __name__ == '__main__':
  main()

