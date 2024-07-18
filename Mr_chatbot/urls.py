from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from chatbot import views

urlpatterns = [
    path('', include("chatbot.urls")),    
    path('admin/', admin.site.urls),
    path('profile/', views.profile, name='profile'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]

    