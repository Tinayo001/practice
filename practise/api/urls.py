from django.urls import path
from . import views

urlpatterns = [
        path('add_student/', views.add_student, name="add_student"),
        path('add_subject/', views.add_subject),
        path('get_total', views.get_total),
        path('get_all/', views.get_all, name="get_all"),
        ]
