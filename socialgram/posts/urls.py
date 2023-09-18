""" Posts URLS """

# DJANGO
from django.urls import path

# VIEWS
from posts import views

urlpatterns = [
    path(
        route='',
        view=views.list_posts,
        name='feed',
    ),
    path(
        route='posts/new/',
        view=views.create_post,
        name='create',
    ),
]