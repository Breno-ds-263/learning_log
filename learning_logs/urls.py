"""Define padrões de URL para learning_logs"""

from django.urls import path
from . import views

app_name = 'learning_logs'

urlpatterns = [
    # Página inicial
    path('', views.index, name='index'),

    # Mostra todos os tópicos
    path('topics/', views.topics, name='topics'),

    # Página de detalhes para um único tópico
    path('topics/<topic_id>/', views.topic, name='topic'),

    # Página para novo tópio
    path('new_topic/', views.new_topic, name='new_topic'),

    # Pagina para adicionar uma nova entrada
    path('new_entry/<topic_id>/', views.new_entry, name='new_entry'),

    # Pagina para editar uma entrada
    path('edit_entry/<entry_id>/', views.edit_entry, name='edit_entry')
    
     
]
