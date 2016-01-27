all:
	@echo "Main targets:"
	@echo ""
	@echo "  test         : test the Web site locally"
	@echo "  test_frozen  : freeze and test the Web site locally"
	@echo "  deploy       : build images, freeze and publish the Web site"
	@echo ""
	@echo "More targets:"
	@echo ""
	@echo "  clean        : clean everything"
	@echo "  img          : build images"
	@echo "  freeze       : build static Web site"
	@echo "  upload       : upload Web site to S3"
	@echo "  requirements : install software packages required to build the Web site"
	@echo ""

requirements:
	# pip install --egg scons # Fails on Windows, so install manually
	pip install -U taschenmesser
	pip install -U scour
	pip install -U boto
	pip install -U flask
	pip install -U jinja2-highlight
	pip install -U mistune
	pip install -U frozen-flask

clean:
	rm -rf website/crossbario/build
	rm -rf website/crossbario/build_uploaded
	rm -rf website/crossbario/static/img/gen/
	rm -rf website/crossbario/static/img/docs/gen/
	scons -uc

img:
	scons img

import_docs:
	mkdir -p website/crossbario/build/static/img/
	cp -R ../crossbardocs/static/img/docs website/crossbario/static/img/
	cp -R ../crossbardocs/static/img/docs website/crossbario/build/static/img/
	cp -R ../crossbardocs/static/img/iotcookbook website/crossbario/static/img/
	cp -R ../crossbardocs/static/img/iotcookbook website/crossbario/build/static/img/

import_reports:
	mkdir -p website/crossbario/static/reports/wstest/
	mkdir -p website/crossbario/build/static/reports/wstest/
	cp -R ../crossbar-reports/wstest/20151221/ website/crossbario/static/reports/wstest/
	cp -R ../crossbar-reports/wstest/20151221/ website/crossbario/build/static/reports/wstest/

freeze:
	python website/crossbario/server.py -f

test: img import_docs import_reports
	python website/crossbario/server.py --port 8080

upload:
	scons upload

deploy: img import_docs import_reports freeze upload

# To upload to: # http://crossbarwwwtest.s3-website-eu-west-1.amazonaws.com/
#
# cd website/crossbario/build
# s3cmd sync -P --skip-existing --delete-removed . s3://crossbarwwwtest/
