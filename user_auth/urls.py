import django.contrib.auth.views
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings #静的ファイルを表示させるために必要
from django.conf.urls.static import static #静的ファイルを表示させるために必要
app_name='user_auth'

urlpatterns=[
    path('', auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('top/', views.top, name="top"), # リダイレクト
    
    #path('logout/', auth_views.LogoutView.as_view(template_name='user_auth/logout.html'), name='logout'),
]

#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) #静的ファイルを表示させるために必要
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #画像表示