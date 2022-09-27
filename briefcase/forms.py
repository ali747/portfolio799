# forms.py
from django import forms
from .models import *
class HotelForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['id', 'image','link']