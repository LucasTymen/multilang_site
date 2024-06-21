from django.contrib import admin
from django.urls import path, include  # Import path and include for URL routing
from django.conf import settings  # Import settings to check debug mode
from django.conf.urls.static import static  # Import static to serve media files
from django.conf.urls.i18n import i18n_patterns  # Import i18n_patterns for internationalization

# Define the main URL patterns for the project
urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site URL
    path('accounts/', include('allauth.urls')),  # Include allauth URLs for authentication
    path('', include('main.urls')),  # Include URLs from the main application
]

# Add routes with internationalization support
urlpatterns += i18n_patterns(
    path('', include('main.urls')),  # Include URLs from the main application
)

# Serve static and media files in debug mode
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # Serve static files
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Serve media files
