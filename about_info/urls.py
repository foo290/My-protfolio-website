from django.urls import path, include
from about_info import views as about_views


urlpatterns = [
    path('', about_views.about, name = 'About-Me'),

    path('edit/about-header-info/<int:pk>/', about_views.Edit_about_header_intro.as_view(), name = 'Edit-About'),
    path('edit/about-bio-info/<int:pk>/', about_views.Edit_about_bio.as_view(), name = 'Edit-About-Bio'),
]