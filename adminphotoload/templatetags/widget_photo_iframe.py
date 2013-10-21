# -*- coding: utf-8 -*-

from django import template
from django.conf import settings

register = template.Library()

@register.inclusion_tag('templatetags/iframe.html')
def widget_photo_iframe(app, model, id, change):
    """
    Inserta el código para la herramienta para subir fotos en un iframe
    """

    return {'app': app,
            'model': model,
            'id': id,
            'change': change,
            'STATIC_URL': settings.STATIC_URL}