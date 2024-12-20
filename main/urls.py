from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('add-tutorial/', views.add_tutorial, name='add_tutorial'),
    path('tutorial/<int:pk>/', views.tutorial_detail, name='tutorial_detail'),
    path('tutorial/<int:pk>/checkout/', views.checkout, name='checkout'),
    path('success/<int:pk>/', views.success, name='success'),
    path('cancel/', views.cancel, name='cancel'),
    path('dashboard/', views.dashboard, name='dashboard'),
]

