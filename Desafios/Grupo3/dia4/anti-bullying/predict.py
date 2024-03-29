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
#

'''Implementation of prediction request API.'''

import httplib2
import json
import logging
import urllib
from apiclient.discovery import build
from google.appengine.ext import webapp
from home import parse_json_file
from home import USER_AGENT
from oauth2client.appengine import CredentialsModel
from oauth2client.appengine import StorageByKeyName
from oauth2client.file import Storage

ERR_TAG = '<HttpError>'
ERR_END = '</HttpError>'

class PredictAPI(webapp.RequestHandler):
  '''This class handles Ajax prediction requests, i.e. not user initiated
     web sessions but remote procedure calls initiated from the Javascript
     client code running the browser.
  '''

  def get(self):
    try:
      # Read server-side OAuth 2.0 credentials from datastore and
      # raise an exception if credentials not found.
      credentials = StorageByKeyName(CredentialsModel, USER_AGENT, 
                                    'credentials').locked_get()
      if not credentials or credentials.invalid:
        raise Exception('missing OAuth 2.0 credentials')

      # Authorize HTTP session with server credentials and obtain  
      # access to prediction API client library.
      http = credentials.authorize(httplib2.Http())
      service = build('prediction', 'v1.5', http=http)
      papi = service.trainedmodels()
    
      # Build prediction data (csvInstance) dynamically based on form input.
      vals = []
      body = {'input' : {'csvInstance' : [str(self.request.get('text'))] }}

      # Make a prediction and return JSON results to Javascript client.
      ret = papi.predict(id='bullying', body=body).execute()
      self.response.out.write(json.dumps(ret))

    except Exception, err:
      # Capture any API errors here and pass response from API back to
      # Javascript client embedded in a special error indication tag.
      err_str = str(err)
      if err_str[0:len(ERR_TAG)] != ERR_TAG:
        err_str = ERR_TAG + err_str + ERR_END
      self.response.out.write(err_str)
