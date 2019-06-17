from django.forms import ModelForm
from wars.models import Searched
from django import forms
from django.utils.safestring import mark_safe
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from crispy_forms.bootstrap import (
    PrependedText, PrependedAppendedText, FormActions)


class searchForm(forms.Form):
	search = forms.CharField(max_length = 30, label = '', widget=forms.TextInput(attrs={'placeholder': 'Realize su búsqueda'}))