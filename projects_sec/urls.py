from django.urls import path
from . import views
from .views import  ProjectCreateView, Delete_Project,ProjectDetailView,ProjectPostUpdateView


urlpatterns = [
    path('project-list/',views.projects_list, name = 'My-Projects'),
    path('project-list/post/<int:pk>/', ProjectDetailView.as_view(), name = 'Projects-Detail'),
    path('project-list/createNewProject/', ProjectCreateView.as_view(), name = 'Create-Project'),

    path('project-list/updateProjectPost/<int:pk>/', ProjectPostUpdateView.as_view(), name = 'Update-Projects-Post'),
    path('project-list/edit/project-card/<int:pk>/', views.ProjectCardUpdate.as_view(), name = 'Edit-Projects-Card'),

    path('project-list/edit/project-heading/<int:pk>/', views.Project_header_info.as_view(), name = 'Edit-Projects-Heading'),

    path('project-list/post/delete/<int:pk>/', Delete_Project.as_view(), name = 'Project-Delete'),
]