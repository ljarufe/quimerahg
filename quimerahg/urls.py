# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    # Apps
    url(r'^', include('portal.urls')),
    (r'^i18n/', include('django.conf.urls.i18n')),
    (r'^tinymce/', include('tinymce.urls')),
    # Media y static
    (r'^media/(?P<path>.*)$','django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT,'show_indexes': True}),
    (r'^static/(?P<path>.*)$','django.views.static.serve',
         {'document_root': settings.STATIC_ROOT,'show_indexes': True}),
)