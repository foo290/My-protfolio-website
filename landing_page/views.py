from django.shortcuts import render
from django.http import HttpResponse
from general_info.models import PrimaryUser
from projects_sec.models import Projects,Projects_cover_info
from skill_set.models import Skills
from about_info.models import AboutMe
from .models import HomePage
# Create your views here.



navbar_name = ''


def home(request):
    global navbar_name
    context_dic = {
        'context': PrimaryUser.objects.first()  

    }

    navbar_name = context_dic['context'].fancy_name
    
    skill_dic=[]
    skill_var = [i[1:] for i in Skills.objects.all().values_list()]
    for j in skill_var:
        temp={}
        temp['title']=j[0]
        temp['items'] = j[1].split('\r\n')
        skill_dic.append(temp)
        
    context_dic['skill_set'] = skill_dic
    context_dic['cards'] = HomePage.objects.all()
    context_dic['fancy_name']=navbar_name


    return render(request, 'landing_page/home.html',context=context_dic)


def about(request):


    tempobj = AboutMe.objects.first()
    selfIntro=tempobj.self_intro.split('\r\n')

    return render(request, 'landing_page/about.html',context={'fancy_name':navbar_name,'about':tempobj,'selfIntro':selfIntro})


def projects(request):
    context_dic = {
        'cover':Projects_cover_info.objects.first(),
        'projects' : Projects.objects.all(),
        'fancy_name':navbar_name
    }
    return render(request, 'landing_page/projects.html',context=context_dic)

def error404(request,exception):
    return render(request, 'error404page.html')





