import django

if django.VERSION >= (3, 0):
    from django.urls import re_path as url_path
else:
    from django.conf.urls import url as url_path

from robots.views import rules_list

urlpatterns = [
    url_path(r'^$', rules_list, name='robots_rule_list'),
]
