from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, CreateView, UpdateView
from .models import AboutMe

# Create your views here.

def about(request):
    tempobj = AboutMe.objects.first()
    return render(request, 'about_info/about.html',context={'about':tempobj})


class Edit_about_header_intro(LoginRequiredMixin,UpdateView): 

    login_url = "/access-denied/"
    redirect_field_name = ""
    raise_exception = False

    """ This view is to edit the hader part of about page """

    model = AboutMe

    additional_context = {'legend':'About Info'}
    def get_context_data(self, *args, **kwargs):
        context = super(Edit_about_header_intro, self).get_context_data(*args, **kwargs)
        context.update(self.additional_context)
        return context

    template_name = 'editUpdate.html'
    fields = ['cover_name','micro_greeting_1','micro_greeting_2','short_intro','cover_image']


class Edit_about_bio(LoginRequiredMixin,UpdateView): 

    login_url = "/access-denied/"
    redirect_field_name = ""
    raise_exception = False

    """ This view is to edit content of the About page """

    model = AboutMe

    additional_context = {'legend':'About Info'}
    def get_context_data(self, *args, **kwargs):
        context = super(Edit_about_bio, self).get_context_data(*args, **kwargs)
        context.update(self.additional_context)
        return context

    template_name = 'editUpdate.html'
    fields = ['greeting_heading','greeting_subheading','self_intro','fairwell_words']

