from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path('login/', views.LoginView, name='login'),
    path('register', views.RegisterView, name='register'),
    path('logout', views.LogoutView, name='logout'),
    path('', views.ProfileView, name='profile'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
