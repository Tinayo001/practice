from django.urls import path
from . import views

urlpatterns = [
        path('add_student', views.add_student),
        path('add_subject', views.add_subject),
        ]
