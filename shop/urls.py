from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path ('',views.liste,name='liste'),
    path('about/',views.about,name='about'),
    path('commander/<int:meuble_id>/', views.commander, name='commander'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='liste'), name='logout'),
]