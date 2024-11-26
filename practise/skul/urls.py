from django.urls import path
from .import views

urlpatterns = [
        path('', views.add_student, name="name"),
        path('add_subject/', views.add_subject, name="subject"),
        ]
