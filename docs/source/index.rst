==============
Wagtail Robots
==============

This is a basic Django application for Wagtail to manage robots.txt files
following the `robots exclusion protocol`_, complementing the Django_
`Sitemap contrib app`_.

This started as a fork of `Django Robots`_ but because of the differences
between the Django Admin and the Wagtail Admin, and other project requirements
git history has not been retained.

For installation and configuration instructions, keep reading.

.. _robots exclusion protocol: http://en.wikipedia.org/wiki/Robots_exclusion_standard
.. _Django: http://www.djangoproject.com/
.. _Sitemap contrib app: http://docs.djangoproject.com/en/dev/ref/contrib/sitemaps/
.. _Django Robots: https://github.com/jazzband/django-robots

Contents:

.. toctree::
   :maxdepth: 1

   screenshots

Installation
============

Use your favorite Python installer to install it from PyPI::

   pip install wagtail-robots

Or get the source from the application site at::

   http://github.com/adrian-turjak/wagtail-robots/

Then follow these steps:

1. Add ``'wagtail.contrib.modeladmin'`` and ``'robots'`` to your INSTALLED_APPS_ setting.
2. Run the ``migrate`` management command

You may want to additionally setup the `Wagtail sitemap generator`_.

And if you install or already happen to be using `CondensedInlinePanel`_ this
library will automatically use it in place of InlinePanel for the Rule create
and edit pages.

.. _INSTALLED_APPS: http://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
.. _TEMPLATES: https://docs.djangoproject.com/en/dev/ref/settings/#templates
.. _Wagtail sitemap generator: http://docs.wagtail.io/en/latest/reference/contrib/sitemaps.html
.. _CondensedInlinePanel: https://github.com/wagtail/wagtail-condensedinlinepanel

Initialization
==============

To activate robots.txt generation on your Wagtail site, add this line to your
URLconf_::

   url(r'^robots\.txt', include('robots.urls')),

This tells Django to build a robots.txt when a robot accesses ``/robots.txt``.
Then, please migrate your database to create the necessary tables and create
``Rule`` objects in the admin interface or via the shell.

.. _URLconf: http://docs.djangoproject.com/en/dev/topics/http/urls/

Rules
=====

``Rule`` - defines an abstract rule which is used to respond to crawling web
robots, using the `robots exclusion protocol`_, a.k.a. robots.txt.

You can link multiple URL pattern to allows or disallows the robot identified
by its user agent to access the given URLs.

The crawl delay field is supported by some search engines and defines the
delay between successive crawler accesses in seconds. If the crawler rate is a
problem for your server, you can set the delay up to 5 or 10 or a comfortable
value for your server, but it's suggested to start with small values (0.5-1),
and increase as needed to an acceptable value for your server. Larger delay
values add more delay between successive crawl accesses and decrease the
maximum crawl rate to your web server.

The Wagtail sites are used to enable multiple robots.txt per Wagtail instance.
If no rule exists it automatically allows every web robot access to every URL
except Wagtail's admin path (`/admin`).

Please have a look at the `database of web robots`_ for a full list of
existing web robots user agent strings.

.. _database of web robots: http://www.robotstxt.org/db.html

URLs
====

``Url`` - defines a case-sensitive and exact URL pattern which is used to
allow or disallow the access for web robots. Case-sensitive.

A missing trailing slash does also match files which start with the name of
the given pattern, e.g., ``'/admin'`` matches ``/admin.html`` too.

Some major search engines allow an asterisk (``*``) as a wildcard to match any
sequence of characters and a dollar sign (``$``) to match the end of the URL,
e.g., ``'/*.jpg$'`` can be used to match all jpeg files.

Caching
=======

You can optionally cache the generation of the ``robots.txt``. Add or change
the ``ROBOTS_CACHE_TIMEOUT`` setting with a value in seconds in your Django
settings file::

   ROBOTS_CACHE_TIMEOUT = 60*60*24

This tells Django to cache the ``robots.txt`` for 24 hours (86400 seconds).
The default value is ``None`` (no caching).

If you need to, you can also specify exactly which cache to use::

   ROBOTS_CACHE_ALIAS="robots"

Unless specified otherwise it will use the ``default`` cache.

Sitemaps
========

By default a ``Sitemap`` statement is automatically added to the resulting
robots.txt by reverse matching the URL of the installed `Wagtail Sitemap app`_.
This is especially useful if you allow every robot to access your whole site,
since it then gets URLs explicitly instead of searching every link.

To change the default behaviour to omit the inclusion of a sitemap link,
change the ``ROBOTS_USE_SITEMAP`` setting in your Django settings file to::

   ROBOTS_USE_SITEMAP = False

In case you want to use specific sitemap URLs instead of the one that is
automatically discovered, change the ``ROBOTS_SITEMAP_URLS`` setting to::

   ROBOTS_SITEMAP_URLS = [
       'http://www.example.com/sitemap.xml',
   ]

If the sitemap is wrapped in a decorator, dotted path reverse to discover
the sitemap URL does not work.
To overcome this, provide a name to the sitemap instance in ``urls.py``::

   urlpatterns = [
       ...
       url(r'^sitemap.xml$', cache_page(60)(sitemap_view), {'sitemaps': [...]}, name='cached-sitemap'),
       ...
   ]

and inform django-robots about the view name by adding the following setting::

   ROBOTS_SITEMAP_VIEW_NAME = 'cached-sitemap'

Use ``ROBOTS_SITEMAP_VIEW_NAME`` also if you use custom sitemap views.

.. _Wagtail Sitemap app: http://docs.wagtail.io/en/latest/reference/contrib/sitemaps.html

Host directive
==============
By default a ``Host`` statement is automatically added to the resulting
robots.txt to avoid mirrors and select the main website properly.

To change the default behaviour to omit the inclusion of host directive,
change the ``ROBOTS_USE_HOST`` setting in your Django settings file to::

   ROBOTS_USE_HOST = False

if you want to prefix the domain with the current request protocol
(**http** or **https** as in ``Host: https://www.mysite.com``) add this setting::

   ROBOTS_USE_SCHEME_IN_HOST = True


Development/Staging Override
============================
Sometimes when you have duplicate database content in both a production and
staging website, it can be useful to override any and all database entries
for the this application and explicitly disallow all.

To do that add this setting::

   ROBOTS_DISALLOW_ALL = True

The resulting `robots.txt` will look as follows::

   User-agent: *
   Disallow: /


Bugs and feature requests
=========================

As always your mileage may vary, so please don't hesitate to send feature
requests and bug reports:

    https://github.com/adrian-turjak/wagtail-robots/issues
