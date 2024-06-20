from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
]


# Définition des URLs pour le projet principal
urlpatterns = [
    # Route pour l'admin
    path('admin/', admin.site.urls),
]

# Ajout des routes avec prise en charge de l'internationalisation
urlpatterns += i18n_patterns(
    path('', include('main.urls')),
)

# Ajout des routes pour servir les fichiers statiques en mode DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
