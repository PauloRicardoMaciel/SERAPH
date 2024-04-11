#!/usr/bin/scl enable python27 -- /home/CONTA/.virtualenv/bin/python
 
import os, sys
 
from flup.server.fcgi import WSGIServer
from django.core.wsgi import get_wsgi_application
 
sys.path.insert(0, "/teste")
os.environ['DJANGO_SETTINGS_MODULE'] = "Seraph.settings"
 
WSGIServer(get_wsgi_application()).run()