"""Deifine padrãos de URL para learning_logs"""

from django.urls import re_path, include

from . import views

app_name='learning_logs'

urlpatterns = [
    # Pagína inicial
    re_path(r'^$', views.index, name='index')
]