# -*- coding: utf-8 -*-

from django.views.decorators.csrf import csrf_exempt
from common.utils import direct_response
from share.forms import ShareForm


@csrf_exempt
def send_share(request, template, path):
    """
    Maneja el formulario de envío de correos
    """
    if request.method == "POST":
        form = ShareForm(template, path, request.POST)
        if form.is_valid():
            form.share()
    else:
        form = ShareForm(template, path)

    return direct_response(request, "send_form.html",
                           {"form": form})