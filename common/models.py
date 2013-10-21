# -*- coding: utf-8 -*-

from django.db import models
from common.utils import highlyRandomName
from easy_thumbnails.fields import ThumbnailerImageField


class Foto(models.Model):
    """
    Foto genérica
    """
    def get_photo_path(self, filename):
        return u'fotos/%s' % highlyRandomName(filename)

    nombre = models.CharField(max_length=250)
    imagen = ThumbnailerImageField(upload_to=get_photo_path, blank=True,
                                   null=True, verbose_name=u"imágen")

    def __unicode__(self):
        return u"%s" % self.nombre

    class Meta:
        ordering = ("nombre",)