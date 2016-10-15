from {{ project_name }}.settings.base import *  # noqa


DEBUG = False
ALLOWED_HOSTS = ['{{ project_name }}.local']
ROOT_URLCONF = '{{ project_name }}.urls'


CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True
X_FRAME_OPTIONS = 'DENY'
SECURE_SSL_REDIRECT = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True


SESSION_COOKIE_SECURE = True
SESSION_ENGINE = 'redis_sessions.session'
SESSION_REDIS_UNIX_DOMAIN_SOCKET_PATH = '/var/run/redis/redis.sock'
