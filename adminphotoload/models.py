# -*- coding: utf-8 -*-

from django.conf.urls import url, patterns
from django.contrib import admin
from django.db.models.loading import get_model
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from common.forms import AdminFotoForm, AdminDeleteFotoForm
from common.models import *
from common.utils import json_response, direct_response


class PhotoFrameAdmin(admin.ModelAdmin):
    """
    Modelo para subir fotos usando el widget en un iframe mediante ajax
    """
    exclude = ('fotos',)

    def get_urls(self):
        """
        URLs para subir fotos y borrarlas
        """
        urls = super(PhotoFrameAdmin, self).get_urls()
        my_urls = patterns('',
            url('^add_fotos/(?P<app>[\w]+)/(?P<model>[\w]+)/(?P<id>\d+)?$',
                self.admin_site.admin_view(self.add_fotos),
                name='admin_add_fotos'),
            url('^ajax_edit_foto/$',
                self.admin_site.admin_view(self.ajax_edit_foto),
                name='admin_ajax_edit_foto'))

        return my_urls + urls

    def add_fotos(self, request, app, model, id):
        """
        página que muestra la herramienta para subir y editar fotos
        """
        Model = get_model(app, model)
        obj = get_object_or_404(Model, id=id)
        form_add = AdminFotoForm()
        form_del = AdminDeleteFotoForm()
        if request.method == 'POST':
            if 'delete' not in request.POST:
                form_add = AdminFotoForm(request.POST, request.FILES)
                if form_add.is_valid():
                    form_add.saveTo(obj)
                    form_add = AdminFotoForm()
                    form_add.success = True
            else:
                form_del = AdminDeleteFotoForm(request.POST)
                if form_del.is_valid():
                    form_del.save()
                    form_del = AdminDeleteFotoForm()
                    form_del.success = True
        fotos = obj.fotos.all()

        return direct_response(request, 'add_photos.html', {'form_add': form_add,
                                                            'form_del': form_del,
                                                            'fotos': fotos})

    @csrf_exempt
    def ajax_edit_foto(self, request):
        """
        si el id recibido es correcto devuelve el nombre y descripcion de la
        foto
        """
        if request.method == 'POST':
            try:
                foto = Foto.objects.get(id=request.POST['id'])
                data = foto.__dict__
                data.pop('imagen')
                data.pop('_state')
            except Foto.DoesNotExist:
                data = {'response': 'el id no pertenece a ninguna foto'}

            return json_response(data)