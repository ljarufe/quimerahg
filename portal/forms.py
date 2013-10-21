#-*- coding: utf-8 -*-

import re
from django import forms
from tinymce.widgets import TinyMCE
from django.conf import settings
from common.utils import send_html_mail
from portal.models import Empresa, UnidadNegocio, Contacto, Noticia, \
    ResponsabilidadSocial, Actividad, Linea, Marca, Proyecto


class EmpresaAdminForm(forms.ModelForm):
    """
    Formulario para el admin
    """
    class Meta:
        model = Empresa

    def __init__(self, *args, **kwargs):
        """
        Añade los campos con TinyMCE
        """
        super(EmpresaAdminForm, self).__init__(*args, **kwargs)
        self.fields['descripcion_en'].widget = TinyMCE()
        self.fields['descripcion_es'].widget = TinyMCE()
        self.fields['mision_en'].widget = TinyMCE()
        self.fields['mision_es'].widget = TinyMCE()
        self.fields['vision_en'].widget = TinyMCE()
        self.fields['vision_es'].widget = TinyMCE()
        self.fields['valores_en'].widget = TinyMCE()
        self.fields['valores_es'].widget = TinyMCE()
        self.fields['historia_en'].widget = TinyMCE()
        self.fields['historia_es'].widget = TinyMCE()
        self.fields['filosofia_en'].widget = TinyMCE()
        self.fields['filosofia_es'].widget = TinyMCE()


class ResponsabilidadSocialAdminForm(forms.ModelForm):
    """
    Formulario para el admin
    """
    class Meta:
        model = ResponsabilidadSocial

    def __init__(self, *args, **kwargs):
        """
        Añade los campos con TinyMCE
        """
        super(ResponsabilidadSocialAdminForm, self).__init__(*args, **kwargs)
        self.fields['introduccion_en'].widget = TinyMCE()
        self.fields['introduccion_es'].widget = TinyMCE()
        self.fields['politica_en'].widget = TinyMCE()
        self.fields['politica_es'].widget = TinyMCE()


class UnidadNegocioAdminForm(forms.ModelForm):
    """
    Formulario para el admin
    """
    if Empresa.objects.exists():
        empresa = forms.ModelChoiceField(queryset=Empresa.objects.all(),
                                         initial=Empresa.objects.latest())

    class Meta:
        model = UnidadNegocio

    def __init__(self, *args, **kwargs):
        """
        Añade los campos con TinyMCE
        """
        super(UnidadNegocioAdminForm, self).__init__(*args, **kwargs)
        self.fields['descripcion_en'].widget = TinyMCE()
        self.fields['descripcion_es'].widget = TinyMCE()
        self.fields['clientes_en'].widget = TinyMCE()
        self.fields['clientes_es'].widget = TinyMCE()


class ContactoForm(forms.ModelForm):
    """
    Formulario de contacto
    """
    comentario = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = Contacto

    def save(self, *args, **kwargs):
        """
        Envía un correo al administrador
        """
        contacto = self.cleaned_data["unidad_negocio"].email_contacto
        send_html_mail(
            settings.DEFAULT_FROM_EMAIL,
            u'Quimera hg: Nuevo mensaje de contacto',
            'email_template.html',
            self.cleaned_data,
            contacto,
            self.cleaned_data['comentario'],
        )


class ActividadAdminForm(forms.ModelForm):
    """
    Formulario para el admin
    """
    class Meta:
        model = Actividad

    def __init__(self, *args, **kwargs):
        """
        Añade los campos con TinyMCE
        """
        super(ActividadAdminForm, self).__init__(*args, **kwargs)
        self.fields['descripcion_en'].widget = TinyMCE()
        self.fields['descripcion_es'].widget = TinyMCE()


class LineaAdminForm(forms.ModelForm):
    """
    Formulario para el admin
    """
    class Meta:
        model = Linea

    def __init__(self, *args, **kwargs):
        """
        Añade los campos con TinyMCE
        """
        super(LineaAdminForm, self).__init__(*args, **kwargs)
        self.fields['descripcion_en'].widget = TinyMCE()
        self.fields['descripcion_es'].widget = TinyMCE()


class MarcaAdminForm(forms.ModelForm):
    """
    Formulario para el admin
    """
    class Meta:
        model = Marca

    def __init__(self, *args, **kwargs):
        """
        Añade los campos con TinyMCE
        """
        super(MarcaAdminForm, self).__init__(*args, **kwargs)
        self.fields['descripcion_en'].widget = TinyMCE()
        self.fields['descripcion_es'].widget = TinyMCE()


class NoticiaAdminForm(forms.ModelForm):
    """
    Formulario para el admin
    """
    class Meta:
        model = Noticia

    def __init__(self, *args, **kwargs):
        """
        Añade los campos con TinyMCE
        """
        super(NoticiaAdminForm, self).__init__(*args, **kwargs)
        self.fields['descripcion_en'].widget = TinyMCE()
        self.fields['descripcion_es'].widget = TinyMCE()


class ProyectoAdminForm(forms.ModelForm):
    """
    Formulario para el admin
    """
    class Meta:
        model = Proyecto

    def __init__(self, *args, **kwargs):
        """
        Añade los campos con TinyMCE
        """
        super(ProyectoAdminForm, self).__init__(*args, **kwargs)
        self.fields['descripcion_en'].widget = TinyMCE()
        self.fields['descripcion_es'].widget = TinyMCE()