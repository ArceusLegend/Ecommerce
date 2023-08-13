from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.account_register, name = "register"),
    path('activate/<uidb64>/<token>/', views.account_activate, name = "activate"),
    path('dashboard/', views.dashboard, name='dashboard'),
]
