"""
guitarscalefinder.py:

Handler for GuitarScaleFinder

* Author:       Mitchell Bowden <mitchellbowden AT gmail DOT com>
* License:      MIT License: http://creativecommons.org/licenses/MIT/
"""

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

import os
import sys
import traceback
import time
import logging
import urllib

from guitar_scale_finder import GuitarScaleFinder
from lib.scale import get_scale_names
from lib.note import Note

class GSFHandler(webapp.RequestHandler):
  # GET
  def get(self):
    template_values = {
      'http_get': True,
      'scales': get_scale_names()
    }

    path = os.path.join(
      os.path.dirname(__file__), '..', 'templates', 'guitarscalefinder.html'
    )
    self.response.out.write(template.render(path, template_values))

  # POST
  def post(self):
    template_values = self.runGuitarScaleFinder(self.request.get('root'), self.request.get('scale'))

    path = os.path.join(
      os.path.dirname(__file__), '..', 'templates', 'guitarscalefinder.html'
    )
    self.response.out.write(template.render(path, template_values))

  def runGuitarScaleFinder(self, root, scale, tuning=None):
    try:
      gsf = GuitarScaleFinder(root, scale)
      print gsf.to_str()

      template_values = {
        'http_get': False,
        'root': root,
        'scale_used': scale,
        'scales': get_scale_names(),
        'vextab_codes': gsf.split_str(12)
      }
    except DeadlineExceededError:
      template_values = {
        'http_get': True,
        'error': "The request has timed out, please try another."
      }

    return template_values
