Management Commands
===================

.. highlight:: console

.. _collectstatic:

collectstatic
-------------

Collects the static files from all installed apps and copies them to the
:ref:`staticfiles-storage`.

You can limit the apps parsed by providing a list of app names::

   $ python manage.py collectstatic --exclude-dirs admin polls

Duplicate file names are resolved in a similar way to how template resolution
works. Files are initially searched for in :ref:`staticfiles-dirs` locations,
followed by apps in the order specified by the INSTALLED_APPS setting.

Some commonly used options are:

``--noinput``
    Do NOT prompt the user for input of any kind.

``-i PATTERN`` or ``--ignore=PATTERN``
    Ignore files or directories matching this glob-style pattern. Use multiple
    times to ignore more.

``-n`` or ``--dry-run``
    Do everything except modify the filesystem.

``-l`` or ``--link``
    Create a symbolic link to each file instead of copying.

``--no-default-ignore``
    Don't ignore the common private glob-style patterns ``'CVS'``, ``'.*'``
    and ``'*~'``.

For a full list of options, refer to the collectstatic management command help
by running::

   $ python manage.py collectstatic --help

.. _findstatic:

findstatic
----------

Searches for one or more relative paths with the enabled finders.

   $ python manage.py findstatic css/base.css admin/js/core.css
   /home/special.polls.com/core/media/css/base.css
   /home/polls.com/core/media/css/base.css
   /home/polls.com/src/django/contrib/admin/media/js/core.js

By default, all matching locations are found. To only return the first match
for each relative path, use the ``--first`` option::

   $ python manage.py findstatic css/base.css --first
   /home/special.polls.com/core/media/css/base.css

This is a debugging aid; it'll show you exactly which static file will be
collected for a given path.

runserver
---------

Overrides the core ``runserver`` command if the ``staticfiles`` app
is installed (in ``INSTALLED_APPS``) and adds automatic serving of static
files and the following new options.

``--nostatic``

Use the ``--nostatic`` option to disable serving of static files with the
``staticfiles`` app entirely. This option is only available if the
``staticfiles`` app is in your project's ``INSTALLED_APPS`` setting.

Example usage::

    django-admin.py runserver --nostatic

``--insecure``

Use the ``--insecure`` option to force serving of static files with the
``staticfiles`` app even if the ``DEBUG`` setting is ``False``.

.. warning:: By using this you acknowledge the fact that it's
   **grossly inefficient** and probably **insecure**. This is only intended for
   local development, should **never be used in production** and is only
   available if the ``staticfiles`` app is in your project's ``INSTALLED_APPS``
   setting.

Example usage::

    django-admin.py runserver --insecure
