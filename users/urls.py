from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'users'

urlpatterns = [
    # Página de login
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    
    # Página de logout
    path('logout/', views.logout_view, name='logout'),

    # Página de cadastro
    path('register', views.register, name='register')
]
