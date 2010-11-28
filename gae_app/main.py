"""
main.py:
Entry point for GAE non-admin.

* Author:       Mitchell Bowden <mitchellbowden AT gmail DOT com>
* License:      MIT License: http://creativecommons.org/licenses/MIT/
"""

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), 'lib'))
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util

import handlers.guitarscalefinder
import handlers.about

def main():
    application = webapp.WSGIApplication([
      ('/', handlers.guitarscalefinder.GSFHandler),
      ('/gsf', handlers.guitarscalefinder.GSFHandler),
      ('/about', handlers.about.AboutHandler)
    ], debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
