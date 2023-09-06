""" 
Platzigram URLs module.
Configuracion de urls del Proyecto
Define los mapeos url-vistas. A pesar de que éste podría contener todo el código del mapeo url,
es más común delegar algo del mapeo a las propias aplicaciones.
"""


from django.urls import path
from socialgram import views as local_views
from posts import views as posts_views


urlpatterns = [
    path('hello-world/', local_views.hello_world),
    path('sorted/', local_views.sort_num),
    path('hi/<str:name>/<int:age>/', local_views.say_hi),
    path('posts/', posts_views.list_posts)
]
