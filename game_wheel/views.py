from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Game, Tag, Language, Publisher, Developer, Label, Time_unit, Genre
from django.shortcuts import redirect
from .forms import SettingsForm
from django.http import HttpResponse

import random

class WheelView(ListView):
    model = Game
    template_name = 'wheel/wheel_list.html'
    queryset = Game.objects.order_by('?')

    def set_add_info(self, your_game):
        your_game.points = your_game.sol_scored()
        your_game.langs = ', '.join([str(l) for l in your_game.languages.all()])
        your_game.gs = ', '.join([str(l) for l in your_game.genres.all()])
        your_game.ts = ', '.join([str(l) for l in your_game.tags.all()])
        your_game.price = int(your_game.ru_price)
        your_game.steam_link = 'https://store.steampowered.com/app/' + str(your_game.appid)

    def get(self, request):
        settings = request.session.get('settings', False)
        roll = request.session.get('roll', False)
        count_games = 5
        droped_game_id = False
        if settings:
            settings_form = SettingsForm(settings)
        else:
            settings_form =SettingsForm()

        if settings_form.is_valid():
            duration_less = settings_form.cleaned_data['duration_less']
            duration_more = settings_form.cleaned_data['duration_more']
            price_less = settings_form.cleaned_data['ru_price_less']
            price_more = settings_form.cleaned_data['ru_price_more']
            count_games =  settings_form.cleaned_data['count_games']
        try:
            games = Game.objects.filter(
                                    duration__lte=duration_less,
                                    duration__gte=duration_more,
                                    ru_price__lte=price_less,
                                    ru_price__gte=price_more
                                ).order_by('?')[:count_games]
        except:
            #games = False
            games = Game.objects.all().order_by('?')[:5]
        your_game = False #if we not rolled game yet
        if roll:
            del(request.session['roll'])
            del(request.session['settings'])
            try:
                for game in games:
                    self.set_add_info(game)
                droped_game_id = random.randrange(len(games))
                your_game = games[droped_game_id]
            except:
                print('0 games for your criteria')


        ctx = {'random_list': games, 'your_game' : your_game, 'settings_form': settings_form, 'count_games':count_games,
        'droped_id':droped_game_id }
        return render(request, self.template_name, ctx)

    def post(self, request):


        if 'roll' in request.POST:
            request.session['settings'] = request.POST
            request.session['roll'] = True
        return redirect(request.path)

        #return redirect(url, params)

class GameCreateView(CreateView):
    model = Game
    template_name = 'wheel/game_form.html'
    success_url = reverse_lazy('wheel:wheel')
    fields = '__all__'

class TagCreateView(CreateView):
    model = Tag
    template_name = 'wheel/game_form.html'
    fields = '__all__'

class LanguageCreateView(CreateView):
    model = Language
    template_name = 'wheel/game_form.html'
    fields = '__all__'

class PublisherCreateView(CreateView):
    model = Publisher
    template_name = 'wheel/game_form.html'
    fields = '__all__'

class DeveloperCreateView(CreateView):
    model = Developer
    template_name = 'wheel/game_form.html'
    fields = '__all__'

class LabelCreateView(CreateView):
    model = Label
    template_name = 'wheel/game_form.html'
    fields = '__all__'

class Time_unitCreateView(CreateView):
    model = Time_unit
    template_name = 'wheel/game_form.html'
    fields = '__all__'

class GenreCreateView(CreateView):
    model = Genre
    template_name = 'wheel/game_form.html'
    fields = '__all__'

