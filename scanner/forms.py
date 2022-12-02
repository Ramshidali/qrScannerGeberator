from django.forms.widgets import TextInput,Textarea,Select,DateInput,CheckboxInput,FileInput
from django import forms
from . models import *


class HouseForm(forms.ModelForm):

    class Meta:
        model = HouseDetails
        fields = ['house_name','area']