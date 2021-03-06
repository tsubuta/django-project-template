# Sam's Django Project Template

**Note:** The master branch contains a template for Django 2.0. If you wish to use a previous version, please
check out the appropriate branch:

* [django-1.10 branch](https://github.com/sjkingo/django-project-template/tree/django-1.10)
* [django-1.9 branch](https://github.com/sjkingo/django-project-template/tree/django-1.9)
* [django-1.8 branch](https://github.com/sjkingo/django-project-template/tree/django-1.8)
* [django-1.7 branch](https://github.com/sjkingo/django-project-template/tree/django-1.7)
* [django-1.6 branch](https://github.com/sjkingo/django-project-template/tree/django-1.6)

## Features

This Django project template sets up a new project with the following features:

* PostgreSQL for database connections.
* Sensible time zone and defaults for Brisbane, Australia.
  * Note that internationalization is disabled!
* `settings` app to store site-specific settings by providing `settings/dev.py` and `settings/prod.py`
  files.
* Enables the [django-debug-toolbar](https://github.com/jazzband/django-debug-toolbar) app for development
* Flat project structure (no sub-directory called `project_name`).
* Serves static and media files when using the development server.
* Password validation is enabled for Django's auth system.

## Installation

Note: This will install the latest stable version of Django (at the time of writing, 2.0). If this is undesirable,
manually download [requirements.txt](https://raw.github.com/sjkingo/django-project-template/master/requirements.txt)
and edit accordingly.

1. Create a new virtualenv and activate it.
2. Install the requirements:

        $ pip install -r https://raw.github.com/sjkingo/django-project-template/master/requirements.txt

3. Create a new project using the template:

        $ export PROJECT_NAME=foo
        $ django-admin.py startproject --template https://github.com/sjkingo/django-project-template/archive/master.zip $PROJECT_NAME

4. Run the following to clean up the template directory and update `requirements.txt`:

        $ cd $PROJECT_NAME
        $ pip freeze > requirements.txt
        $ rm -f README.md
        $ chmod +x manage.py

5. By default, `settings.dev` is used in `manage.py`. To switch to the production settings, set the environment variable `DJANGO_SETTINGS_MODULE`:

        $ DJANGO_SETTINGS_MODULE=settings.prod ./manage.py ...

It is based on the `project_template` shipped with [`stable/2.0`](https://github.com/django/django/tree/stable/2.0.x/django/conf/project_template).
