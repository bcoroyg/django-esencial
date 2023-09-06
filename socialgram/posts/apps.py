'''POST aplication module.'''
'''Declara toda la configuracion de la APP al publico, puede ser reutilizable'''


from django.apps import AppConfig


class PostsConfig(AppConfig):
    '''Post aplication settings.'''
    name = 'posts'
    verbose_name = 'Posts'
