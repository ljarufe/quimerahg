# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('portal.views',
    url(
        regex=r'^$',
        view="home",
        name="home"
    ),
    url(
        regex='^get_proyecto_json/$',
        view='get_proyecto_json',
        name='get_proyecto_json'
    )
)