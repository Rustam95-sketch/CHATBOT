# chatbot_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.handle_message, name='handle_message'),
    path('', views.process_message, name='process_message'),
]
