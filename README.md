# DJANGO ESENCIAL

## Entorno Virtual - Python 3
* Crear
```
python3 -m venv venv
```

* Iniciar
```
source venv/bin/activate
```

* Desactivar
```
deactivate
```

* Lista de dependencias del entorno
```
pip freeze
```

## DJANGO v2.2
* Intalación
```
pip install django==2.2 -U
```

* Iniciar proyecto
```
django-admin startproject name .
```

* Creacion de app
```
python manage.py startapp posts
```

## PATRONES DE DISEÑO
* Es una solución reutilizable a un problema común

### MTV
* **MODEL** → Define la estructura de los datos.
* **TEMPLATE** → Es la lógica de presentación de datos
* **VIEW** → Es el encargado de traer los datos y pasarlos al template

## MIGRACIONES
* Ejecutar migraciones
```
python manage.py migrate
```

* Migracion de modelos
```
python manage.py makemigrations
```

## SHELL DJANGO
* Shell
```
python manage.py shell
```