# -*- coding: utf-8 -*-

from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from adminphotoload.models import PhotoFrameAdmin
from common.models import Foto
from portal.forms import EmpresaAdminForm, UnidadNegocioAdminForm, \
    ResponsabilidadSocialAdminForm, ActividadAdminForm, LineaAdminForm, \
    MarcaAdminForm, NoticiaAdminForm, ProyectoAdminForm
from portal.models import Telefono, RepresentanteUnidad, RepresentanteEmpresa, \
    Empresa, UnidadNegocio, Categoria, CategoriaLinea, CategoriaMarca, \
    Proyecto, Linea, Marca, Noticia, ResponsabilidadSocial, Campania, \
    Actividad, Contacto


class EmpresaAdmin(TranslationAdmin):
    form = EmpresaAdminForm
    list_display = ("nombre",)


class ResponsabilidadSocialAdmin(TranslationAdmin):
    form = ResponsabilidadSocialAdminForm


class UnidadNegocioAdmin(TranslationAdmin):
    form = UnidadNegocioAdminForm
    list_display = ("nombre", "get_representantes",)
    filter_horizontal = ('representantes',)


class ProyectoAdmin(TranslationAdmin, PhotoFrameAdmin):
    form = ProyectoAdminForm
    list_display = ("nombre", "get_unidad_negocio", "categoria",)
    ordering = ("categoria",)


class ContactoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "email",)


class CampaniaAdmin(TranslationAdmin):
    pass


class ActividadAdmin(TranslationAdmin, PhotoFrameAdmin):
    form = ActividadAdminForm


class FotoAdmin(TranslationAdmin):
    pass


class RepresentanteEmpresaAdmin(TranslationAdmin):
    pass


class CategoriaAdmin(TranslationAdmin):
    list_display = ("nombre", "unidad_negocio",)


class CategoriaLineaAdmin(TranslationAdmin):
    list_display = ("nombre", "unidad_negocio",)


class CategoriaMarcaAdmin(TranslationAdmin):
    list_display = ("nombre", "unidad_negocio",)


class LineaAdmin(TranslationAdmin):
    form = LineaAdminForm
    list_display = ("nombre", "categoria_linea",)


class MarcaAdmin(TranslationAdmin):
    form = MarcaAdminForm
    list_display = ("nombre", "categoria_marca",)


class NoticiaAdmin(TranslationAdmin):
    form = NoticiaAdminForm


class RepresentanteEmpresaAdmin(TranslationAdmin):
    pass


admin.site.register(Telefono)
admin.site.register(RepresentanteUnidad)
admin.site.register(RepresentanteEmpresa, RepresentanteEmpresaAdmin)
admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(UnidadNegocio, UnidadNegocioAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(CategoriaLinea, CategoriaLineaAdmin)
admin.site.register(CategoriaMarca, CategoriaMarcaAdmin)
admin.site.register(Proyecto, ProyectoAdmin)
admin.site.register(Linea, LineaAdmin)
admin.site.register(Marca, MarcaAdmin)
admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(ResponsabilidadSocial, ResponsabilidadSocialAdmin)
admin.site.register(Campania, CampaniaAdmin)
admin.site.register(Actividad, ActividadAdmin)
admin.site.register(Foto, FotoAdmin)
admin.site.register(Contacto, ContactoAdmin)