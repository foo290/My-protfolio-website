from django.urls import path, include
from . import views
from about_info import views as about_views





urlpatterns = [
    path('', views.home, name = 'Home-Landing'),
    path(r'about-me/', include('about_info.urls')),
    
    path('admin/', views.admin404, name = 'Admin404'),
    path('access-denied/', views.access_denied, name = 'AccessDenied'),

    path('edit/into-sec/', views.Edit_Intro, name = 'Intro-Edit'),

    path('edit/explore-cards/<int:pk>/', views.Edit_cards.as_view(), name = 'Card-Edit'),
    path('explore-cards/add-new/card/', views.Add_card.as_view(), name = 'Card-Add'),

    path('edit/general-status/', views.Edit_general_status, name = 'State-Edit'),
    
    path('edit/single-skill/<int:pk>/', views.Edit_skills.as_view(), name = 'Skills-Edit'),
    path('skill-set/add-new/skill/', views.Add_skills.as_view(), name = 'Skills-Add'),






]