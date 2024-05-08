from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView

from .forms import RatingForm
from .forms import AddGameForm
from .models import *

menu = [
    {'title': "Добавить игру", 'url_name': 'add_game'},
]


# def index(request):
#     # page = render_to_string('game/index.html')
#     # return HttpResponse(page)
#     games = Game.verify.all()
#     genre_list = Genre.objects.all()
#
#     context = {
#         'title': 'Главная страница',
#         'menu': menu,
#         'games': games,
#         'genre_list': genre_list,
#     }
#     return render(request, 'game/index.html', context=context)


def genre(request, genre_slug):
    genre_show = get_object_or_404(Genre, slug=genre_slug)
    games = genre_show.genres.filter(is_verify=Game.Status.VERIFIED)
    genre_list = Genre.objects.all()

    context = {
        'title': f'Жанр: {genre_show.title} ',
        'games': games,
        'genre_list': genre_list,
        'genre_show': genre_show.pk,
    }

    return render(request, 'game/index.html', context=context)


def game_show(request, game_slug):
    game = get_object_or_404(Game, slug=game_slug)
    genre_list = Genre.objects.all()
    user_rating = None

    if request.user.is_authenticated:
        user_rating_obj, created = GameUser.objects.get_or_create(user=request.user, game=game)

    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating_value = form.cleaned_data['rating']
            if user_rating_obj:
                user_rating_obj.rating = rating_value
                user_rating_obj.save()
            else:
                GameUser.objects.create(user=request.user, game=game, rating=rating_value)
    else:
        initial_data = {'rating': user_rating_obj.rating} if user_rating_obj else None
        form = RatingForm(initial=initial_data)

    context = {'title': game.title,
               'game': game,
               'genre_list': genre_list,
               'form': form,
               }

    return render(request, 'game/game.html', context=context)


# def add_game(request):
#     if request.method == "POST":
#         form = AddGameForm(request.POST, request.FILES)
#         if form.is_valid():
#             # try:
#             #     Game.objects.create(**form.cleaned_data)
#             #     return redirect('home')
#             # except:
#             #     form.add_error(None, 'Ошибка добавления')
#             form.save()
#             return redirect('home')
#     else:
#         form = AddGameForm()
#
#     context = dict(title="Добавить игру", menu=menu, form=form)
#     return render(request, 'game/add_game.html', context)


class AddGame(LoginRequiredMixin, CreateView):
    form_class = AddGameForm
    template_name = 'game/add_game.html'
    success_url = reverse_lazy('home')
    extra_context = {
        'title': 'Добавление игры',
    }

    def form_valid(self, form):
        w = form.save(commit=False)
        w.editor = self.request.user
        return super().form_valid(form)


class GameHome(ListView):
    template_name = 'game/index.html'
    context_object_name = 'games'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['genre_list'] = Genre.objects.all()
        return context

    def get_queryset(self):
        return Game.verify.all()


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
