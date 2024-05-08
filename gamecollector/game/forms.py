from django import forms
from .models import *


# class AddGameForm(forms.Form):
#     title = forms.CharField(max_length=120, label='Название: ', widget=forms.TextInput(attrs={'class':'form-input'}), error_messages={'required' : 'Необходимо ввести название'})
#     slug = forms.SlugField(max_length=120, label='Slug: ')
#     plot = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 5}), required=False, label='Описание: ')
#     genre = forms.ModelMultipleChoiceField(queryset=Genre.objects.all(), label='Жанры: ')
#     studio = forms.ModelChoiceField(queryset=Studio.objects.all(), label='Студия: ', empty_label='Студия не выбрана')
#
class AddGameForm(forms.ModelForm):
    genre = forms.ModelMultipleChoiceField(queryset=Genre.objects.all(), label='Жанры: ')
    studio = forms.ModelChoiceField(queryset=Studio.objects.all(), label='Студия: ', empty_label='Студия не выбрана')

    class Meta:
        model = Game
        fields = ['title', 'plot', 'slug', 'release_year', 'poster', 'studio', 'genre']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'plot': forms.Textarea(attrs={'cols': 50, 'rows': 5}),
        }


class RatingForm(forms.Form):
    rating = forms.FloatField(label='Rating', min_value=1, max_value=5)
