# -*- coding: utf-8 -*-

from django import forms
from django.shortcuts import get_object_or_404
from common.models import Foto


class AdminFotoForm(forms.ModelForm):
    """
    Formulario para guardar las fotos
    """
    id = forms.IntegerField(widget=forms.HiddenInput, required=False)
    imagen = forms.ImageField(required=False)

    class Meta:
        model = Foto

    def clean(self):
        """
        Verifica que la im\xc3\xa1gen principal pueda estar ausente sólo si
        existe id
        """
        cleaned_data = super(self.__class__, self).clean()
        id = cleaned_data.get('id')
        imagen = cleaned_data.get('imagen')
        if not imagen and not id:
            self._errors['imagen'] = \
                self.error_class([u'Este campo es obligatorio'])

        return cleaned_data

    def saveTo(self, obj):
        """
        Graba(o actualiza) la foto y la agrega a los objectos relacionados
        del objeto p, siempre y cuando el related name sea fotos
        """
        id = self.cleaned_data.get('id')
        new_img = self.cleaned_data.get('imagen')
        if not new_img:
            new_img = Foto.objects.get(id=id).imagen
        foto = Foto(id=id, nombre=self.cleaned_data.get('nombre'),
                    imagen=new_img)
        foto.save()
        if not id:
            obj.fotos.add(foto)

        return foto


class AdminDeleteFotoForm(forms.Form):
    """
    Formulario para borrar las fotos
    """
    id = forms.IntegerField(widget=forms.HiddenInput)

    def save(self):
        """
        borra la foto
        """
        foto = get_object_or_404(Foto, id=self.cleaned_data['id'])

        return foto.delete()