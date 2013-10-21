# -*- coding: utf-8 -*-

from modeltranslation.translator import translator, TranslationOptions
from portal.models import *


class FotoTranslation(TranslationOptions):
    fields = ("nombre",)


class RepresentanteEmpresaTranslation(TranslationOptions):
    fields = ("cargo",)


class EmpresaTranslation(TranslationOptions):
    fields = ("descripcion", "mision", "vision", "valores", "historia",
              "filosofia")


class UnidadNegocioTranslation(TranslationOptions):
    fields = ("nombre", "descripcion", "clientes",)


class CategoriaTranslation(TranslationOptions):
    fields = ("nombre",)


class CategoriaLineaTranslation(TranslationOptions):
    fields = ("nombre",)


class CategoriaMarcaTranslation(TranslationOptions):
    fields = ("nombre",)


class ProyectoTranslation(TranslationOptions):
    fields = ("nombre", "descripcion",)


class LineaTranslation(TranslationOptions):
    fields = ("nombre", "descripcion",)


class MarcaTranslation(TranslationOptions):
    fields = ("nombre",)


class NoticiaTranslation(TranslationOptions):
    fields = ("nombre", "descripcion",)


class ResponsabilidadSocialTranslation(TranslationOptions):
    fields = ("introduccion", "politica",)


class CampaniaTranslation(TranslationOptions):
    fields = ("nombre",)


class ActividadTranslation(TranslationOptions):
    fields = ("nombre", "descripcion",)


translator.register(Foto, FotoTranslation)
translator.register(RepresentanteEmpresa, RepresentanteEmpresaTranslation)
translator.register(Empresa, EmpresaTranslation)
translator.register(UnidadNegocio, UnidadNegocioTranslation)
translator.register(Categoria, CategoriaTranslation)
translator.register(CategoriaLinea, CategoriaLineaTranslation)
translator.register(CategoriaMarca, CategoriaMarcaTranslation)
translator.register(Proyecto, ProyectoTranslation)
translator.register(Linea, LineaTranslation)
translator.register(Marca, MarcaTranslation)
translator.register(Noticia, NoticiaTranslation)
translator.register(ResponsabilidadSocial, ResponsabilidadSocialTranslation)
translator.register(Campania, CampaniaTranslation)
translator.register(Actividad, ActividadTranslation)