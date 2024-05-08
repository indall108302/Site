from django.contrib import admin
from .models import Game, Genre, Studio


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    fields = ["title", "slug", "plot", "release_year", "is_verify", "studio", "genre"]
    prepopulated_fields = {'slug': ("title",)}
    filter_horizontal = ['genre']
    list_display = ("title", "release_year", "is_verify", "studio")
    list_display_links = ("title",)
    ordering = ['release_year', "title"]
    list_editable = ("is_verify", )
    list_per_page = 5
    actions = ['approve']
    search_fields = ['title', 'genre__title']
    list_filter = ['studio__title', 'genre__title', 'is_verify']

    @admin.action(description='Одобрить')
    def approve(self, request, queryset):
        count = queryset.update(is_verify=Game.Status.VERIFIED)
        self.message_user(request, f"Одобрено {count} записей")

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    list_display_links = ("id", "title")
    ordering = ["title"]


@admin.register(Studio)
class StudioAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    list_display_links = ("id", "title")
    ordering = ["title"]
