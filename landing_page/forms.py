from django import forms
from django.contrib.auth.models import User
from .models import Nav_cards



class CardUpdateForm(forms.ModelForm):

    class Meta:
        model = Nav_cards

        fields = ['heading','Summary']
