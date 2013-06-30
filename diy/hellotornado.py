#!/usr/bin/env python
import os
cwd = os.path.dirname(os.path.abspath(__file__))
os.environ['PYTHON_EGG_CACHE'] = os.path.join(cwd, '..', 'misc/virtenv/lib/python2.6/site-packages')
virtualenv = os.path.join(cwd, '..', 'misc/virtenv/bin/activate_this.py')
execfile(virtualenv, dict(__file__=virtualenv))

import app
app.main(os.environ['OPENSHIFT_DIY_IP'])
