# -*- coding: utf-8 -*-

from django.contrib.sites.models import Site
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.template import Context, loader
from django.conf import settings


class ShareableClass(models.Model):
    """
    Clase abstracta que genera el botón compartir, se necesita definir un
    objeto Site en la aplicación y sobreescribir el método get_absolute_url de
    la clase que herede de esta o en su defecto el método get_share_url siguiendo
    las especificaciones
    """
    facebook_account = models.CharField(max_length=200,
        verbose_name=_(u"Cuenta de facebook"), blank=True, null=True)
    twitter_account = models.CharField(max_length=200,
        verbose_name=_(u"Cuenta de twitter"), blank=True, null=True)
    google_account = models.CharField(max_length=200,
        verbose_name=_(u"Cuenta de google"), blank=True, null=True)

    class Meta:
        abstract = True

    def get_absolute_url(self):
        """
        Sobreescribir si el modelo tiene una url dentro del dominio
        """
        return False

    def get_share_url(self):
        """
        Sobreescribir si la clase tiene una url en un dominio externo
        """
        pass

    def get_share_button(self):
        """
        Obtiene el código para el botón de compartir
        """
        t = loader.get_template('share_button.html')
        c = Context({'object': self,
                     'domain': Site.objects.get_current().domain,
                     'STATIC_URL': settings.STATIC_URL})

        return t.render(c)


class SimpleShareableClass(models.Model):
    """
    Clase abstracta que genera el botón compartir, se necesita definir un
    objeto Site en la aplicación y sobreescribir el método get_absolute_url de
    la clase que herede de esta o en su defecto el método get_share_url siguiendo
    las especificaciones
    A diferencia de ShareableClass esta no necesita definir cuentas, se puede usar
    en un modelo existente sin necesidad de alterar la base de datos
    """
    class Meta:
        abstract = True

    def get_absolute_url(self):
        """
        Sobreescribir si el modelo tiene una url dentro del dominio
        """
        return False

    def get_share_url(self):
        """
        Sobreescribir si la clase tiene una url en un dominio externo
        """
        pass

    def get_share_button(self):
        """
        Obtiene el código para el botón de compartir
        """
        t = loader.get_template('simple_share_button.html')
        c = Context({'object': self,
                     'domain': Site.objects.get_current().domain,
                     'STATIC_URL': settings.STATIC_URL})

        return t.render(c)