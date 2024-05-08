from django import template
from game.views import menu

register = template.Library()

@register.simple_tag(name='get_genre_list')
def game_genre_list(game):
    genre_list = game.genre.all()
    return genre_list

@register.simple_tag(name='get_menu')
def get_menu():
    return menu

