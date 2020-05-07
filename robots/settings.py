import sys


class Settings(object):
    defaults = {
        #: A list of one or more sitemaps to inform robots about:
        'SITEMAP_URLS': ('ROBOTS_SITEMAP_URLS', []),
        'USE_SITEMAP': ('ROBOTS_USE_SITEMAP', True),
        'USE_HOST': ('ROBOTS_USE_HOST', True),
        'CACHE_TIMEOUT': ('ROBOTS_CACHE_TIMEOUT', None),
        'CACHE_ALIAS': ('ROBOTS_CACHE_ALIAS', 'default'),
        'SITE_BY_REQUEST': ('ROBOTS_SITE_BY_REQUEST', False),
        'USE_SCHEME_IN_HOST': ('ROBOTS_USE_SCHEME_IN_HOST', False),
        'SITEMAP_VIEW_NAME': ('ROBOTS_SITEMAP_VIEW_NAME', False),
        'DISALLOW_ALL': ('ROBOTS_DISALLOW_ALL', False),
    }

    def __getattr__(self, attribute):
        from django.conf import settings
        if attribute in self.defaults:
            return getattr(settings, *self.defaults[attribute])


sys.modules[__name__] = Settings()
