from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.views.i18n import set_language

# Définition des URLs pour l'application 'main'
urlpatterns = [
    # Route pour le changement de langue
    path('set_language/', set_language, name='set_language'),

    # Route pour la page d'accueil
    path('', views.home, name='home'),

    # Route pour la liste des articles
    path('articles/', views.article_list, name='article_list'),

    # Route pour le détail d'un article
    path('article/<slug:slug>/', views.article_detail, name='article_detail'),

    # Route pour la création d'un nouvel article
    path('article/new/', views.article_create, name='article_create'),

    # Route pour la mise à jour d'un article existant
    path('article/<slug:slug>/edit/', views.article_update, name='article_update'),

    # Route pour la suppression d'un article
    path('article/<slug:slug>/delete/', views.article_delete, name='article_delete'),

    # Route pour l'inscription de l'utilisateur
    path('register/', views.register, name='register'),

    # Route pour la connexion de l'utilisateur
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),

    # Route pour la déconnexion de l'utilisateur
    path('logout/', auth_views.LogoutView.as_view(template_name='main/logout.html'), name='logout'),

    # Route pour le profil de l'utilisateur
    path('profile/', views.profile, name='profile'),

    # Route pour la suppression du compte utilisateur
    path('delete_account/', views.delete_account, name='delete_account'),
]
