from django.shortcuts import render,HttpResponse
from .models import Projects,Projects_cover_info
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from project_posts.models import P_Post

# Create your views here.

def projects_list(request):
    context_dic = {
        'cover':Projects_cover_info.objects.first(),
        'projects' : Projects.objects.all(),
    }
    return render(request, 'projects_sec/projects.html',context=context_dic)


class ProjectDetailView(DetailView):
    model = P_Post

    template_name = 'projects_sec/project_details.html'
#
#

class ProjectCreateView(LoginRequiredMixin,CreateView): 

    login_url = "/access-denied/"
    redirect_field_name = ""
    raise_exception = False

    """ This view is to create projects list """

    model = Projects

    additional_context = {'legend':"Add New Project"}
    def get_context_data(self, *args, **kwargs):
        context = super(ProjectCreateView, self).get_context_data(*args, **kwargs)
        context.update(self.additional_context)
        return context

    template_name = 'editUpdate.html'
    fields = ['thumbnail','project_title','project_summary','github_link']


class ProjectPostUpdateView(LoginRequiredMixin, UpdateView):

    login_url = "/access-denied/"
    redirect_field_name = ""
    raise_exception = False

    """ This view is to Update projects Posts """

    model = P_Post

    additional_context = {'legend':"Update Project's Post"}
    def get_context_data(self, *args, **kwargs):
        context = super(ProjectPostUpdateView, self).get_context_data(*args, **kwargs)
        context.update(self.additional_context)
        return context

    template_name = 'editUpdate.html'
    fields = ['project_summary']

class ProjectCardUpdate(LoginRequiredMixin, UpdateView):
    
    login_url = "/access-denied/"
    redirect_field_name = ""
    raise_exception = False


    """ This view is to Update Projects Cards """
        
    model = Projects


    additional_context = {'legend':"Update Project's Card"}
    def get_context_data(self, *args, **kwargs):
        context = super(ProjectCardUpdate, self).get_context_data(*args, **kwargs)
        context.update(self.additional_context)
        return context

    template_name = 'editUpdate.html'
    fields = ['thumbnail','project_title','project_summary','github_link','post_link']


class Project_header_info(LoginRequiredMixin, UpdateView):
    
    login_url = "/access-denied/"
    redirect_field_name = ""
    raise_exception = False


    """ This view is to Update Projects Page info """
        
    model = Projects_cover_info


    additional_context = {'legend':"Project Page"}
    def get_context_data(self, *args, **kwargs):
        context = super(Project_header_info, self).get_context_data(*args, **kwargs)
        context.update(self.additional_context)
        return context

    template_name = 'editUpdate.html'
    fields = ['cover_name','cover_subname','page_heading','page_subheading','cover_image']

class Delete_Project(LoginRequiredMixin, DeleteView):
    login_url = "/access-denied/"
    redirect_field_name = ""
    raise_exception = False

    success_url = '/projects/project-list/'


    """ This view is to Delete Projects """
        
    model = Projects


    additional_context = {'legend':"Delete Project"}
    def get_context_data(self, *args, **kwargs):
        context = super(Delete_Project, self).get_context_data(*args, **kwargs)
        context.update(self.additional_context)
        return context






