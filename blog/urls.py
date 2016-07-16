from django.conf.urls import patterns, url
from django.contrib import admin

from .views import home, contact, post_detail

urlpatterns = patterns(
    '',
    url(r'^(?P<category_slug>[\w-]+)/(?P<post_slug>[\w-]+)$', post_detail, name='detail'),
    #url(r'^/category=(?P<category_id>[0-9]+)$', home),
    url(r'^/category=(?P<post_slug>[\w-]+)', home),
    url(r'^contact', contact),
    url(r'', home),
)
