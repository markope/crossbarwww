update_deps:
	cp bower_components/jquery/dist/jquery.min.js static/js
	cp bower_components/materialize/dist/js/materialize.min.js static/js
	cp bower_components/materialize/dist/css/materialize.min.css static/css
	cp -R bower_components/materialize/dist/font/* static/font
	cp bower_components/autobahn/autobahn.min.* static/js

test:
	python server.py
