# -*- coding: utf-8 -*-

from django import forms
from django.contrib.sites.models import Site
from django.core.validators import email_re
from django.utils.translation import ugettext_lazy as _
from common.utils import send_mass_html_mails
from common.validators import validate_name


class ShareForm(forms.Form):
    """
    Formulario para compartir un objeto por email
    """
    name = forms.CharField(validators=[validate_name])
    emails = forms.CharField(required=False,
        label="e-mails",
        widget=forms.Textarea(attrs={'rows':2}),
        help_text=_(u"e-mails should be separated by commas"))
    message = forms.CharField(required=False,
        widget=forms.Textarea(attrs={'rows':5}))
    url = forms.CharField(widget=forms.HiddenInput)

    def __init__(self, template, path, *args, **kwargs):
        """
        Recibe el path y el nombre del template
        """
        self.template = template
        self.path = path
        super(ShareForm, self).__init__(*args, **kwargs)

    def clean_emails(self):
        """
        Los emails deben tener el formato correcto y estar separados por comas
        """
        if self.cleaned_data["emails"]:
            self.emails = [email.strip() for email in
                           self.cleaned_data["emails"].split(",")]
            for email in self.emails:
                if not email_re.match(email.strip()):
                    raise forms.ValidationError(_(u"There are some invalid e-mail"))

            return self.emails
        else:
            raise forms.ValidationError(_(u"You must enter a e-mail address at "
                                          u"least."))

    def share(self):
        """
        Envía la url y el mensaje a los emails ingresados en el formularios
        """
        send_mass_html_mails(
            u"info@qlabs.com",
            u"%s quiere compartir esta página contigo" % self.cleaned_data["name"],
            self.template,
            {"name": self.cleaned_data["name"],
             "message": self.cleaned_data["message"],
             "url": self.cleaned_data["url"],
             'domain': Site.objects.get_current().name},
            self.emails,
            path=self.path
        )