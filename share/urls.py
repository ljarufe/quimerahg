# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

# Reescribir esta url con los parámetros adecuados para el template y la ruta
# si se desea cambiar el formato del correo en html enviado.
urlpatterns = patterns('share.views',
    url(r'^send/$',
        'send_share',
        {"template": "default_share_email.html",
         "path": ""},
        name='send_share'),
)