# -*- coding: utf-8 -*-

import random
from django.utils.datastructures import MultiValueDictKeyError
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from common.utils import direct_response, json_response
from .forms import ContactoForm
from .models import Empresa, UnidadNegocio, RepresentanteEmpresa, \
    ResponsabilidadSocial, Actividad, Noticia, Proyecto, Campania


@csrf_exempt
def home(request):
    """
    Retorna la página de inicio
    """
    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ContactoForm()

    return direct_response(
        request,
        "base.html",
        {"empresa": Empresa.objects.latest(),
         "divisiones": UnidadNegocio.objects.all(),
         "representantes": RepresentanteEmpresa.objects.all(),
         "responsabilidad": ResponsabilidadSocial.objects.latest(),
         "campanias": Campania.objects.all(),
         "noticias": Noticia.objects.all(),
         "photo_random": random.randrange(1, 5),
         "form": form}
    )


def get_proyecto_json(request):
    """
    :return:devuelve un proyecto serializado en json
    """
    if request.method == 'GET':
        try:
            id_ = request.GET["id_"]
        except MultiValueDictKeyError:
            return json_response({})
        try:
            proyecto = get_object_or_404(Proyecto, id=id_)
        except ValueError:
            return json_response({})
        fotos = [{"nombre": foto.nombre,
                  "imagen": foto.imagen.url,
                  "thumbnail": foto.imagen['gallery'].url}
                 for foto in proyecto.fotos.all()]
        data = {
            "nombre": proyecto.nombre,
            "descripcion": proyecto.descripcion,
            "url": proyecto.url,
            "fotos": fotos,
        }

        return json_response(data)