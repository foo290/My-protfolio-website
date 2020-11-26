from django import forms
from django.contrib.auth.models import User
from .models import PrimaryUser
# from django.contrib.auth.forms import UserCreationForm

class IntroUpdateForm(forms.ModelForm):
    
    class Meta:
        model = PrimaryUser
        fields = ['pfp','home_page_bg_img','name','fancy_name','bio','status','location','twitter','discord','linkdin','email_id']

class GeneralStatusUpdateForm(forms.ModelForm):

    class Meta:
        model = PrimaryUser
        fields = ['recent_project_title','recent_project_sub_title','recent_project_summary']