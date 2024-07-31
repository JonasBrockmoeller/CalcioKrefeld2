from django.urls import path
from . import views

urlpatterns = [
    path('get/homeranking/', views.get_latest_homeranking_result, name='getHomeRanking'),
    path('getAll/', views.get_results, name='getResults'),
    path('add/', views.new_result, name='newResult'),
]