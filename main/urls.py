from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.views.i18n import set_language

# Define URLs for the 'main' application
urlpatterns = [
    # Route for changing language
    path('set_language/', set_language, name='set_language'),

    # Route for home page
    path('', views.home, name='home'),

    # Route for listing articles
    path('articles/', views.article_list, name='article_list'),

    # Route for creating a new article
    path('article/new/', views.article_create, name='article_create'),

    # Route for updating an existing article
    path('article/<slug:slug>/edit/', views.article_update, name='article_update'),

    # Route for deleting an article
    path('article/<slug:slug>/delete/', views.article_delete, name='article_delete'),

    # Route for article detail
    path('article/<slug:slug>/', views.article_detail, name='article_detail'),

    # Route for user registration
    path('register/', views.register, name='register'),

    # Route for user login
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),

    # Route for user logout
    path('logout/', auth_views.LogoutView.as_view(template_name='main/logout.html'), name='logout'),

    # Route for user profile
    path('profile/', views.profile, name='profile'),

    # Route for deleting user account
    path('delete_account/', views.delete_account, name='delete_account'),

    # Route for the chatbot
    path('chatbot/', views.chatbot, name='chatbot'),

    # Route for the search AI function (fake search is replaced with actual)
    path('search/', views.search, name='search'),
]
