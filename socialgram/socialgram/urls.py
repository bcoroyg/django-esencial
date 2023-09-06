""" 
Platzigram URLs module.
Configuracion de urls del Proyecto
Define los mapeos url-vistas. A pesar de que éste podría contener todo el código del mapeo url,
es más común delegar algo del mapeo a las propias aplicaciones.
"""


from django.urls import path
from socialgram import views


urlpatterns = [
    path('hello-world/', views.hello_world),
    path('hi/', views.hi)
]
