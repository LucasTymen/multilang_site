from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

# ####### for using medias ########
from django.conf import settings
from django.conf.urls.static import static
# ####### for using medias ########

urlpatterns = [
    # Home page
    path('', views.home, name='home'),

    # List articles
    path('articles/', views.article_list, name='article_list'),

    # Article detail view
    path('article/<slug:slug>/', views.article_detail, name='article_detail'),

    # Create a new article
    path('article/new/', views.article_create, name='article_create'),

    # Update an existing article
    path('article/<slug:slug>/edit/', views.article_update, name='article_update'),

    # Delete an article
    path('article/<slug:slug>/delete/', views.article_delete, name='article_delete'),

    # User registration
    path('register/', views.register, name='register'),

    # User login
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),

    # User logout
    path('logout/', auth_views.LogoutView.as_view(template_name='main/logout.html'), name='logout'),

    # User profile
    path('profile/', views.profile, name='profile'),

    # Delete user account
    path('delete_account/', views.delete_account, name='delete_account'),
]

# ####### for using medias ########
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# ####### for using medias ########
