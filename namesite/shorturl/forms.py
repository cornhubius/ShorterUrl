from django import forms
from .models import *


class New_link(forms.Form):
    link = forms.CharField(max_length=255)
