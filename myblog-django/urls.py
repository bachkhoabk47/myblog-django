from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles import views

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^markdown/', include("django_markdown.urls")),
    #url(r'^search/', include('haystack.urls')),
    url(r'^static/(?P<path>.*)$', views.serve),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
	}),
    url(r'^', include("blog.urls", namespace='posts')),

    #rl(r'^(?P<category_id>[0-9]+)/(?P<post_id>[0-9]+)$', post_detail, namespace='posts'),
    #url(r'', home),
    
    #url(r'^post/(?P<slug>\S+)$', views.post),
)
