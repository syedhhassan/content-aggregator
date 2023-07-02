from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('science/', views.science, name='science'),
    path('health/', views.health, name='health'),
    path('technology/', views.technology, name='technology'),
    path('sports/', views.sports, name='sports'),
    path('education/', views.education, name='education'),
    path('business/', views.business, name='business')
]