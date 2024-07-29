from django.urls import path
from . import views

urlpatterns = [
    path('get/', views.get_members, name='members'),
    path('add/', views.new_member, name='addMembers'),
]