#!/usr/bin/env python
import os
import sys

from django.conf import settings

TEST_ROOT = os.path.dirname(os.path.abspath(__file__))

if not settings.configured:
    settings.configure(
        TEST_ROOT = TEST_ROOT,
        DATABASE_ENGINE = 'sqlite3',
        MEDIA_URL = '/media/',
        MEDIA_ROOT = os.path.join(TEST_ROOT, 'project', 'site_media', 'media'),
        STATIC_URL = '/static/',
        ADMIN_MEDIA_PREFIX = '/static/admin/',
        STATIC_ROOT = os.path.join(TEST_ROOT, 'project', 'site_media', 'static'),
        STATICFILES_STORAGE = 'staticfiles.storage.StaticFilesStorage',
        STATICFILES_DIRS = (
            os.path.join(TEST_ROOT, 'project', 'documents'),
        ),
        STATICFILES_FINDERS = (
            'staticfiles.finders.FileSystemFinder',
            'staticfiles.finders.AppDirectoriesFinder',
            'staticfiles.finders.DefaultStorageFinder'
        ),
        ROOT_URLCONF = 'tests.urls',
        TEMPLATE_DIRS = (
            os.path.join(TEST_ROOT, 'project', 'templates'),
        ),
        INSTALLED_APPS = [
            'django.contrib.admin',
            'staticfiles',
            'tests',
            'tests.apps.test',
            'tests.apps.no_label',
            'tests.apps.skip',
        ],
    )

from django.test.simple import run_tests


def runtests(*test_args):
    if not test_args:
        test_args = ['tests']
    sys.path.insert(0, os.path.dirname(TEST_ROOT))
    failures = run_tests(test_args, verbosity=1, interactive=True)
    sys.exit(failures)


if __name__ == '__main__':
    runtests(*sys.argv[1:])
