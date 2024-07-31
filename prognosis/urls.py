from django.urls import path
from . import views

urlpatterns = [
    path('get/', views.get_latest_prognosis, name='prognosis'),
    path('add/', views.new_prognosis, name='addPrognosis'),
]