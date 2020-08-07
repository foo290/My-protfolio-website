from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name = 'Home-Landing'),
    path('about-me/', views.about, name = 'About-Me'),
    path('projects/', views.projects, name = 'My-Projects'),

]