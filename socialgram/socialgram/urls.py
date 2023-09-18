""" 
Socialgram URLs module.
Configuracion de urls del Proyecto
Define los mapeos url-vistas. A pesar de que éste podría contener todo el código del mapeo url,
es más común delegar algo del mapeo a las propias aplicaciones.
"""

# DJANGO
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from posts import views as posts_views
from users import views as users_views


urlpatterns = [
    path('admin/', admin.site.urls),
 
    path('', include(('posts.urls', 'posts'), namespace='posts')),
    path('users/', include(('users.urls', 'users'), namespace='users')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
