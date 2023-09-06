'''
Sirve para el deployment a produccion
se usa para ayudar a la aplicación Django a comunicarse con el servidor web. 
'''

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'socialgram.settings')

application = get_wsgi_application()
