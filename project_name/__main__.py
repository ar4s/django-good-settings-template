#!/usr/bin/env python
import os
import sys


def main(settings_module='{{ project_name }}.settings', force=False):
    if force:
        os.environ['DJANGO_SETTINGS_MODULE'] = settings_module
    else:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)


def dev():
    main('{{ project_name }}.settings.dev')


def test():
    main('{{ project_name }}.settings.test', force=True)


def prod():
    main('{{ project_name }}.settings.prod')


if __name__ == '__main__':
    prod()
