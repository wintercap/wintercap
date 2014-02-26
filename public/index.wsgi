import os, sys, site

site.addsitedir('/home/desktop/py3env/lib/python3.2/site-packages')

sys.path.append('/var/www/wintercap.fr/web/wintercap')
sys.path.append('/var/www/wintercap.fr/web/wintercap/wintercap')

os.environ['DJANGO_SETTINGS_MODULE'] = 	'wintercap.settings'

## Activate virtual env here
activate_env = '/home/desktop/py3env/bin/activate_this.py'
execfile(activate_env, dict(__file__=activate_env))

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
