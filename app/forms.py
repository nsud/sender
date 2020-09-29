from datetime import datetime

from django import forms


class FormAdd(forms.Form):
    title = forms.CharField(label="", max_length=100)
    body = forms.CharField(label="", max_length=100)
    time = forms.DateTimeField(default=datetime.now)
