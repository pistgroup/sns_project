from django import forms
from .models import Day

class Daycreateform(forms.ModelForm):

    class Meta:
        model = Day
        fields = '__all__'