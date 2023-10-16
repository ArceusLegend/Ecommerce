from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic import TemplateView

from . import views
from .forms import PwdResetConfirmForm, PwdResetForm, UserLoginForm

app_name = 'users'

urlpatterns = [
    path('register/', views.account_register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/registration/login.html',
                                                form_class=UserLoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/users/login/'), name='logout'),
    path('activate/<slug:uidb64>/<slug:token>/', views.account_activate, name='activate'),
    # password reset
    path('pwd_reset/', auth_views.PasswordResetView.as_view(template_name='users/user/pwd_reset_form.html',
                                                            success_url='pwd_reset_email_conf',
                                                            email_template_name='users/user/pwd_reset_email.html',
                                                            form_class=PwdResetForm),
         name='pwd_reset'),
    path('pwd_reset_conf/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/user/pwd_reset_conf.html',
                                                     success_url='/users/pwd_reset_complete/',
                                                     form_class=PwdResetConfirmForm
                                                     ),
         name='pwd_reset_conf'),
    path('pwd_reset/pwd_reset_email_conf/',
         TemplateView.as_view(template_name="users/user/reset_status.html"), name='pwd_reset_done'),
    path('pwd_reset_complete/',
         TemplateView.as_view(template_name="users/user/reset_status.html"), name='pwd_reset_complete'),
    # dashboard
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/edit/', views.edit_details, name='edit_details'),
    path('profile/delete_user/', views.delete_user, name='delete_user'),
    path('profile/delete_conf/',
         TemplateView.as_view(template_name="users/user/delete_conf.html"), name='delete_conf'),
]
