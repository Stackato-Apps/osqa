# encoding:utf-8
import os.path

SITE_SRC_ROOT = os.path.dirname(__file__)
LOG_FILENAME = 'django.osqa.log'

#for logging
import logging
logging.basicConfig(
    filename=os.path.join(SITE_SRC_ROOT, 'log', LOG_FILENAME),
    level=logging.ERROR,
    format='%(pathname)s TIME: %(asctime)s MSG: %(filename)s:%(funcName)s:%(lineno)d %(message)s',
)

#ADMINS and MANAGERS
ADMINS = ()
MANAGERS = ADMINS

DEBUG = False
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': True
}
TEMPLATE_DEBUG = DEBUG
INTERNAL_IPS = ('127.0.0.1',)

import json
vcap_services = json.loads(os.environ['VCAP_SERVICES'])
srv = vcap_services['mysql-5.1'][0]
cred = srv['credentials']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': cred['name'],
        'USER': cred['user'],
        'PASSWORD': cred['password'],
        'HOST': cred['hostname'],
        'PORT': cred['port'],
    }
}


CACHE_BACKEND = 'file://%s' % os.path.join(os.path.dirname(__file__),'cache').replace('\\','/')
#CACHE_BACKEND = 'dummy://'
SESSION_ENGINE = 'django.contrib.sessions.backends.db'

# This should be equal to your domain name, plus the web application context.
# This shouldn't be followed by a trailing slash.
# I.e., http://www.yoursite.com or http://www.hostedsite.com/yourhostapp
#APP_URL = 'http://'
vcap_app = json.loads(os.environ['VCAP_APPLICATION'])
APP_URL = 'http://' + vcap_app['uris'][0]

#LOCALIZATIONS
TIME_ZONE = 'America/Los_Angeles'

#OTHER SETTINGS

USE_I18N = True
LANGUAGE_CODE = 'en'

DJANGO_VERSION = 1.1
OSQA_DEFAULT_SKIN = 'default'

DISABLED_MODULES = ['books', 'recaptcha', 'project_badges']
