from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', include('social_django.urls', namespace = 'social')),
    path('login/', auth_views.LoginView.as_view(template_name='login/index.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout/index.html'), name='logout'),

]
