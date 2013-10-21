# -*- coding: utf-8 -*-

from datetime import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _
from share.models import ShareableClass
from common.utils import highlyRandomName
from easy_thumbnails.fields import ThumbnailerImageField
from common.models import Foto


class Telefono(models.Model):
    """
    Teléfono genérico
    """
    numero = models.CharField(max_length=20, )
    PHONE_TYPE = (
        (u"Cl", u"Claro"),
        (u"Mo", u"Movistar"),
        (u"RC", u"RPC"),
        (u"RM", u"RPM"),
        (u"Ne", u"Nextel"),
        (u"Fi", u"Fijo")
    )
    tipo = models.CharField(max_length=2, choices=PHONE_TYPE)

    def __unicode__(self):
        return u"%s: %s" % (self.get_tipo_display(), self.numero)


class RepresentanteEmpresa(models.Model):
    """
    Representantes de la empresa
    """
    nombre = models.CharField(max_length=200)
    cargo = models.CharField(max_length=250)
    email = models.EmailField()

    def __unicode__(self):
        return u"%s" % self.nombre

    class Meta:
        verbose_name = u"Representante de empresa"
        verbose_name_plural = u"Representantes de empresa"


class Empresa(ShareableClass):
    """
    Clase que representa la empresa
    """
    def get_photo_path(self, filename):
        return u'fotos/%s' % highlyRandomName(filename)

    nombre = models.CharField(max_length=50, verbose_name=u"nombre")
    descripcion = models.TextField(verbose_name=u"descripción", blank=True,
                                   null=True)
    mision = models.TextField(verbose_name=u"misión", blank=True, null=True)
    vision = models.TextField(verbose_name=u"vision", blank=True, null=True)
    valores = models.TextField(blank=True, null=True)
    historia = models.TextField(blank=True, null=True)
    filosofia = models.TextField(verbose_name=u"filosofía", blank=True,
                                 null=True)
    direccion = models.CharField(max_length=250, verbose_name=u"dirección",
                                 blank=True, null=True)
    telefono = models.ForeignKey(Telefono, verbose_name=u"teléfono", blank=True,
                                 null=True)
    logo = ThumbnailerImageField(upload_to=get_photo_path, blank=True,
                                 null=True)
    email = models.EmailField(blank=True, null=True)

    def __unicode__(self):
        return u"%s" % self.nombre

    class Meta:
        get_latest_by = "id"


class RepresentanteUnidad(models.Model):
    """
    Representantes de las unidades de negocio
    """
    nombre = models.CharField(max_length=200)
    email = models.EmailField()

    def __unicode__(self):
        return u"%s" % self.nombre

    class Meta:
        verbose_name = u"Representante de unidad"
        verbose_name_plural = u"Representantes de unidad"


class UnidadNegocio(models.Model):
    """
    Unidades de negocio dentro de la empresa
    """
    def get_photo_path(self, filename):
        return u'fotos/%s' % highlyRandomName(filename)

    nombre = models.CharField(max_length=250)
    descripcion = models.TextField(verbose_name=u"descripción", blank=True,
                                   null=True)
    representantes = models.ManyToManyField(RepresentanteUnidad, blank=True,
                                            null=True)
    empresa = models.ForeignKey(Empresa)
    logo = ThumbnailerImageField(upload_to=get_photo_path, blank=True,
                                 null=True)
    bg_image = models.ImageField(upload_to=get_photo_path, blank=True,
                                 null=True, verbose_name=u"imágen de fondo")
    clientes = models.TextField(null=True, blank=True)
    email_contacto = models.EmailField(null=True, blank=True,
                                       verbose_name=u"e-mail de contacto")

    def __unicode__(self):
        return u"%s" % self.nombre

    def get_representantes(self):
        return ", ".join([item.nombre for item in self.representantes.all()])
    get_representantes.short_description = u"Representantes"

    class Meta:
        verbose_name = u"Unidad de negocio"
        verbose_name_plural = u"Unidades de negocio"
        ordering = ("id",)


class Categoria(models.Model):
    """
    Categorías de los proyectos de una unidad de negocio
    """
    nombre = models.CharField(max_length=150)
    unidad_negocio = models.ForeignKey(UnidadNegocio,
                                       verbose_name=u"unidad de negocio")

    def __unicode__(self):
        return u"%s" % self.nombre

    class Meta:
        verbose_name = u"Categoría de proyecto"
        verbose_name_plural = u"Categorías de proyectos"


class CategoriaLinea(models.Model):
    """
    Categorías de las lineas de una unidad de negocio
    """
    nombre = models.CharField(max_length=150)
    unidad_negocio = models.ForeignKey(UnidadNegocio,
                                       verbose_name=u"unidad de negocio")

    def __unicode__(self):
        return u"%s" % self.nombre

    class Meta:
        verbose_name = u"Categoría de linea"
        verbose_name_plural = u"Categorías de lineas"


class CategoriaMarca(models.Model):
    """
    Categorías de las marcas de una unidad de negocio
    """
    nombre = models.CharField(max_length=150)
    unidad_negocio = models.ForeignKey(UnidadNegocio,
                                       verbose_name=u"unidad de negocio")

    def __unicode__(self):
        return u"%s" % self.nombre

    class Meta:
        verbose_name = u"Categoría de marca"
        verbose_name_plural = u"Categorías de marcas"


class Proyecto(models.Model):
    """
    Proyectos de una unidad de negocio
    """
    nombre = models.CharField(max_length=300)
    descripcion = models.TextField(verbose_name=u"descripción", blank=True,
                                   null=True)
    categoria = models.ForeignKey(Categoria, verbose_name=u"categoría")
    url = models.URLField(blank=True, null=True)
    fotos = models.ManyToManyField(Foto)

    def __unicode__(self):
        return u"%s" % self.nombre

    def get_unidad_negocio(self):
        return u"%s" % self.categoria.unidad_negocio
    get_unidad_negocio.short_description = u'Unidad de Negocio'


class Linea(models.Model):
    """
    Linea de una unidad de negocio
    """
    nombre = models.CharField(max_length=300)
    descripcion = models.TextField(verbose_name=u"descripción", blank=True,
                                   null=True)
    categoria_linea = models.ForeignKey(CategoriaLinea,
                                        verbose_name=u"categoría")

    def __unicode__(self):
        return u"%s" % self.nombre


class Marca(models.Model):
    """
    Marca dentro de una unidad de negocio
    """
    def get_photo_path(self, filename):
        return u'fotos/%s' % highlyRandomName(filename)

    nombre = models.CharField(max_length=300)
    imagen = ThumbnailerImageField(upload_to=get_photo_path)
    url = models.URLField(blank=True, null=True)
    categoria_marca = models.ForeignKey(CategoriaMarca,
                                        verbose_name=u"categoría")

    def __unicode__(self):
        return u"%s" % self.nombre


class Noticia(models.Model):
    """
    Noticia en forma de blog
    """
    def get_photo_path(self, filename):
        return u'fotos/%s' % highlyRandomName(filename)

    nombre = models.CharField(max_length=350)
    descripcion = models.TextField(verbose_name=u"descripción", blank=True,
                                   null=True)
    imagen = ThumbnailerImageField(upload_to=get_photo_path, blank=True,
                                   null=True)
    fecha = models.DateField(default=datetime.now)

    def __unicode__(self):
        return u"%s" % self.nombre

    @classmethod
    def get_intervalos_fecha(cls):
        """
        Devuelve la primera y última fecha
        """
        cls.objects.all().order_by("fecha")


class ResponsabilidadSocial(models.Model):
    """
    Política de responsabiliad social
    """
    introduccion = models.TextField(verbose_name=u"introducción", blank=True,
                                    null=True)
    politica = models.TextField(verbose_name=u"política", blank=True,
                                null=True)

    def __unicode__(self):
        return u"Responsabilidad Social"

    class Meta:
        get_latest_by = "id"
        verbose_name_plural = u"Responsabilidades sociales"


class Campania(models.Model):
    """
    Campañas de responsabilidad social
    """
    nombre = models.CharField(max_length=150)

    def __unicode__(self):
        return u"{obj.nombre}".format(obj=self)

    class Meta:
        verbose_name = u"Campaña"
        verbose_name_plural = u"Campañas"


class Actividad(models.Model):
    """
    Actividad de responsabilidad social
    """
    nombre = models.CharField(max_length=350)
    campania = models.ForeignKey(Campania, verbose_name=u"Campaña")
    descripcion = models.TextField(verbose_name=u"descripción", blank=True,
                                   null=True)
    fotos = models.ManyToManyField(Foto)

    def __unicode__(self):
        return u"%s" % self.nombre

    class Meta:
        verbose_name_plural = u"Actividades"


class Contacto(models.Model):
    """
    Cliente que entra en contacto con el formulario
    """
    nombre = models.CharField(max_length=250,
                              verbose_name=_(u"nombres y apellidos"))
    email = models.EmailField(verbose_name=_(u"correo"))
    unidad_negocio = models.ForeignKey(UnidadNegocio,
                                       verbose_name=u"Área")

    def __unicode__(self):
        return u"%s" % self.nombre