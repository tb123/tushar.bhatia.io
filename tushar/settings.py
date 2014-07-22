
import os

import webapp2
import jinja2

# JINJA2 environment
JINJA_ENVIRONMENT = jinja2.Environment(
    # loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + './templates'),
    loader=jinja2.PackageLoader('blog', 'templates'),
    # loader=jinja2.FileSystemLoader('')
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

# URL Routes
routes = [(r'/', 'blog.views.MainPage'),]

# Webapp2 Config Settings
config = {}

application = webapp2.WSGIApplication(routes=routes, debug=True, config=config)
