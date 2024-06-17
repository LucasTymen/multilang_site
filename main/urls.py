from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('article/<slug:slug>/', views.article_detail, name='article_detail'),
    path('article/new/', views.article_create, name='article_create'),
    path('article/<slug:slug>/edit/', views.article_update, name='article_update'),
    path('article/<slug:slug>/delete/', views.article_delete, name='article_delete'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='main/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('delete_account/', views.delete_account, name='delete_account'),
]
