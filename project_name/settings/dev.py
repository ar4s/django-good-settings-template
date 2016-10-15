from {{ project_name }}.settings.base import *  # noqa


def only_true(request):
    '''For django debug toolbar.'''
    return True


DEBUG = True

ROOT_URLCONF = '{{ project_name }}.urls.dev'

INSTALLED_APPS = INSTALLED_APPS + [
    'debug_toolbar',
]

MIDDLEWARE = MIDDLEWARE + [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': "%s.only_true" % __name__,
}

AUTH_PASSWORD_VALIDATORS = []

