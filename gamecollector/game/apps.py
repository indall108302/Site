from django.apps import AppConfig


class GameConfig(AppConfig):
    verbose_name = "Игры"
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'game'
