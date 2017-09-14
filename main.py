#!/usr/bin/env python
import os
import sys
import tornado.wsgi
from web.app import Application


sys.path.append(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'lib', 'python')
)

app = tornado.wsgi.WSGIAdapter(Application().make_app())
