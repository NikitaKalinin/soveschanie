from django import forms
from .models import *

class RoomForm(forms.ModelForm):

    class Meta:
        model = Room
        exclude = [""]