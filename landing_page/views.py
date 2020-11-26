from django.shortcuts import render, redirect
from django.http import HttpResponse
from general_info.models import PrimaryUser
from django.contrib.auth.mixins import LoginRequiredMixin
from skill_set.models import Skills
from .models import Nav_cards
from django.views.generic import DetailView, CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

from general_info.forms import IntroUpdateForm, GeneralStatusUpdateForm
from .forms import CardUpdateForm



# Create your views here.

navbar_name = ''


def home(request):
    global navbar_name
    context_dic = {
        'context': PrimaryUser.objects.first()
    }
    try:
        navbar_name = context_dic['context'].fancy_name
    except:
        pass
    
    skill_dic=[]
    skill_var = [i for i in Skills.objects.all().values_list()]
    for j in skill_var:
        temp={}
        temp['id_']=j[0]
        temp['title']=j[1]
        temp['items'] = j[2].split('\r\n')
        skill_dic.append(temp)
        
    context_dic['skill_set'] = skill_dic
    context_dic['cards'] = Nav_cards.objects.all()
    context_dic['fancy_name']=navbar_name

    return render(request, 'landing_page/home.html',context=context_dic)


@login_required(login_url='/access-denied/',redirect_field_name='')
def Edit_Intro(request):
    if request.method == 'POST':
        form = IntroUpdateForm(request.POST, request.FILES ,instance=request.user.primaryuser)
        
        if form.is_valid():
            form.save()
            messages.success(request,'saved')
            return redirect('Home-Landing')
    else:
        form = IntroUpdateForm(instance=request.user.primaryuser)

    context = {
        'profile_form':form
    }
    return render(request,'landing_page/intro_edit.html',context)


@login_required(login_url='/access-denied/',redirect_field_name='')
def Edit_general_status(request):
    if request.method == 'POST':
        form = GeneralStatusUpdateForm(request.POST ,instance=request.user.primaryuser)
        
        if form.is_valid():
            form.save()
            messages.success(request,'saved')
            return redirect('Home-Landing')
    else:
        form = GeneralStatusUpdateForm(instance=request.user.primaryuser)

    context = {
        'legend':'Edit General Status',
        'form': form
    }
    return render(request,'editUpdate.html',context)


class Edit_cards(LoginRequiredMixin,UpdateView):
    login_url = "/access-denied/"
    redirect_field_name = ""
    raise_exception = False

    model = Nav_cards

    additional_context = {'legend':'Edit Cards'}
    def get_context_data(self, *args, **kwargs):
        context = super(Edit_cards, self).get_context_data(*args, **kwargs)
        context.update(self.additional_context)
        return context

    template_name = 'editUpdate.html'
    fields = ['heading','Summary','link']


class Add_card(LoginRequiredMixin,CreateView): 

    login_url = "/access-denied/"
    redirect_field_name = ""
    raise_exception = False

    """ This view is to create new Cards """

    model = Nav_cards

    additional_context = {'legend':'Add New Cards'}
    def get_context_data(self, *args, **kwargs):
        context = super(Add_card, self).get_context_data(*args, **kwargs)
        context.update(self.additional_context)
        return context

    template_name = 'editUpdate.html'
    fields = ['heading','Summary','link']


class Edit_skills(LoginRequiredMixin,UpdateView):
    login_url = "/access-denied/"
    redirect_field_name = ""
    raise_exception = False

    model = Skills

    additional_context = {'legend':'Edit Skills'}
    def get_context_data(self, *args, **kwargs):
        context = super(Edit_skills, self).get_context_data(*args, **kwargs)
        context.update(self.additional_context)
        return context

    template_name = 'editUpdate.html'
    fields = ['heading','items']


class Add_skills(LoginRequiredMixin,CreateView): 

    login_url = "/access-denied/"
    redirect_field_name = ""
    raise_exception = False

    """ This view is to add new skill """

    model = Skills

    additional_context = {'legend':'Add New Skills'}
    def get_context_data(self, *args, **kwargs):
        context = super(Add_skills, self).get_context_data(*args, **kwargs)
        context.update(self.additional_context)
        return context

    template_name = 'editUpdate.html'
    fields = ['heading','items']


# ----------------------------------------------------------------------------------------------------------------------------------------

def error404(request,exception):
    return render(request, 'error_pages/error404page.html')

def admin404(request):
    return render(request, 'error_pages/admin404.html')

def error500(request):
    return render(request, 'error_pages/error500.html')

def access_denied(request):
    return render(request,'error_pages/unauthorized_access.html')

