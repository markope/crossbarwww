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
    g, url_for, abort, render_template, flash, send_from_directory

from markdown import DocPages, get_git_latest_commit


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
app.config['DEBUG'] = True
app.config['CROSSBARDOCS'] = os.path.abspath('../../../crossbardocs')

d = os.path.join(app.config['CROSSBARDOCS'], 'pages/docs')
print("Processsing Markdown pages from {} ..".format(d))
app.pages_docs = DocPages(d)

d = os.path.join(app.config['CROSSBARDOCS'], 'pages/iotcookbook')
print("Processsing Markdown pages from {} ..".format(d))
app.pages_iotcookbook = DocPages(d)

# Routes
#
@app.route('/')
def page_home():
   session['site_area'] = 'landing'
   return render_template('index.html')

@app.route('/docs/<path:path>/')
@app.route('/docs/')
def page_docs(path=None):
   session['site_area'] = 'docs'
   if path is None or path.strip() == "":
      title = 'Documentation'
      path = 'Home'
   else:
      title = path.replace('-', ' ')

   contents = app.pages_docs.render(path)

   if contents:
      return render_template('page_docs.html', contents=contents, title=title)
   else:
      abort(404)

@app.route('/iotcookbook/<path:path>/')
@app.route('/iotcookbook/')
def page_iotcookbook(path=None):
   session['site_area'] = 'iotcookbook'
   if path is None or path.strip() == "":
      title = 'IoT Cookbook'
      path = 'Home'
   else:
      title = path.replace('-', ' ')

   contents = app.pages_iotcookbook.render(path)

   if contents:
      return render_template('page_iotcookbook.html', contents=contents, title=title)
   else:
      abort(404)

@app.route('/static/img/docs/<path:filename>')
def static_img_docs(filename):
   d = os.path.join(app.config['CROSSBARDOCS'], 'static/img/docs')
   return send_from_directory(d, filename)

@app.route('/static/img/iotcookbook/<path:filename>')
def static_img_iotcookbook(filename):
   d = os.path.join(app.config['CROSSBARDOCS'], 'static/img/iotcookbook')
   return send_from_directory(d, filename)


if __name__ == "__main__":
    log.startLogging(sys.stdout)
    resource = WSGIResource(reactor, reactor.getThreadPool(), app)
    site = Site(resource)
    site.noisy = False
    site.log = lambda _: None
    reactor.listenTCP(8080, site)
    reactor.run()
