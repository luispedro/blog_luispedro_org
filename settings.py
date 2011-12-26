import os

_BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)
TEST_RUNNER = 'django_nose.run_tests'
APPEND_SLASH = True

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'                     # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = _BASE_DIR + '/blogluispedro.db'     # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Lisbon'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = _BASE_DIR + '/media/'
STATIC_URL = '/media/'
MEDIA_URL = STATIC_URL

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/admin-media/'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
    'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.cache.CacheMiddleware',
    'gitcms.redirect.middleware.RedirectMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    # Don't forget to use absolute paths, not relative paths.
    _BASE_DIR + '/templates',
)

COMPRESS_PRECOMPILERS = [
    ('text/x-sass', 'sass {infile} {outfile}'),
]
COMPRESS_ENABLED = True
COMPRESS_URL = STATIC_URL
COMPRESS_DEBUG_TOGGLE = None

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.markup',

    'compressor',

    'gitcms.tagging',
    'gitcms.pages',
    'gitcms.menus',
    'gitcms.books',
    'gitcms.blog',
    'gitcms.conferences',
    'gitcms.files',
    'gitcms.redirect',
)

GITDJANGO_DIRNAME = './content'
try:
    from local_settings import *
except ImportError:
    pass

