""" 
Platzigram URLs module.
Configuracion de urls del Proyecto
Define los mapeos url-vistas. A pesar de que éste podría contener todo el código del mapeo url,
es más común delegar algo del mapeo a las propias aplicaciones.
"""


from django.urls import path
from django.http import HttpResponse

# Una vista en DJANGO es una función
def hello_world(request):
    'Return a greeting.'
    return HttpResponse('Hello, World!')

urlpatterns = [
    path('hello-world', hello_world)
]
