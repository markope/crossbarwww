import os
import re
import sys
import uuid
import mimetypes

from twisted.python import log
from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.wsgi import WSGIResource

from flask import Flask, Request, request, session, \
    g, url_for, abort, render_template, flash


# make sure we have MIME types defined for all the
# file types we use
mimetypes.add_type('image/svg+xml', '.svg')
mimetypes.add_type('text/javascript', '.jgz')

# Jinja2 extension for Pygments
#
# Note: To generate Pygments CSS file for style: pygmentize -S default -f html > pygments.css
#
try:
   import jinja2_highlight
except ImportError:
   print("Warning: Jinja2-Highlight not available")
   SiteFlask = Flask
   HAS_HIGHLIGHT = False
else:
   class SiteFlask(Flask):
      jinja_options = dict(Flask.jinja_options)
      jinja_options.setdefault('extensions',[]).append('jinja2_highlight.HighlightExtension')
   HAS_HIGHLIGHT = True

# Main app object
#
app = SiteFlask(__name__)
app.secret_key = str(uuid.uuid4())

# Routes
#
@app.route('/')
def page_home():
   return render_template('index.html')

@app.route('/docs')
def page_docs_home():
   return render_template('docpage.html')


if __name__ == "__main__":
    log.startLogging(sys.stdout)
    resource = WSGIResource(reactor, reactor.getThreadPool(), app)
    site = Site(resource)
    site.noisy = False
    site.log = lambda _: None
    reactor.listenTCP(8080, site)
    reactor.run()
