# planner/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('generate/', views.generate_plan, name='generate_plan'),
    path('add_place/', views.add_place, name='add_place'),
]
