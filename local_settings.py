"""
Django local site-specific settings for {{ project_name }} project.
"""

DEBUG = True

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)


# See https://docs.djangoproject.com/en/1.7/ref/settings/#databases for details.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',     # leave blank
        'PORT': '',     # leave blank
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
# If DEBUG is True, localhost will automatically be added to this list.
ALLOWED_HOSTS = []

# Make this unique, and don't share it with anybody.
SECRET_KEY = '{{ secret_key }}'
