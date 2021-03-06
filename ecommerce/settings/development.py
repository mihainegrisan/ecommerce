from .base import *
import sys

DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '9c9ab6b8.ngrok.io']

INSTALLED_APPS += [
    # keep this after ...'django.contrib.staticfiles'
    'debug_toolbar'
]

MIDDLEWARE += ('debug_toolbar.middleware.DebugToolbarMiddleware',)

# DEBUG TOOLBAR SETTINGS

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]

def show_toolbar(request):
    return True

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TOOLBAR_CALLBACK': show_toolbar
}


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/' #how to access the image in the browser


# the django debug toolbar interferes with the tests.
# this is one workaround .. also check urls.py
TESTING_MODE = 'test' in sys.argv
