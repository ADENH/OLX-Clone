from django.urls import path
from django.contrib.auth import login
from django.contrib.auth import views as auth_views
#from . import  views
app_name='accounts'

urlpatterns = [
    path('login/' , auth_views.LoginView.as_view() , name='login'),
    path('logout/' , auth_views.LoginView.as_view() , name='logout'),
    path('password_change/' , auth_views.PasswordChangeView.as_view() , name='password_change_form'),
    path('password_change/done/' , auth_views.PasswordResetDoneView.as_view() , name='password_change_done'),
    path('password_reset/' , auth_views.PasswordResetView.as_view() , name='password_reset'),
    path('password_reset/done/' , auth_views.PasswordResetDoneView.as_view() , name='password_reset_done'),
    path('reset/<uidb64>/<token>/' , auth_views.LoginView.as_view() , name='password_reset_confirm'),
    path('reset/done/' , auth_views.LoginView.as_view() , name='password_reset_complete'),
]