from {{ project_name }}.settings.base import *  # noqa


DEBUG = False
PASSWORD_HASHERS = ('django_plainpasswordhasher.PlainPasswordHasher',)
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    },
}
