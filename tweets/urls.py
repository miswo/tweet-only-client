from django.urls import path

from . import views

app_name = 'tweets'
urlpatterns = [
    path('', views.index, name='index'),
    path('', views.tweet, name='tweet'),
]