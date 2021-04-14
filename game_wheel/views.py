from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Game, Tag, Language, Publisher, Developer, Label, Time_unit, Genre
from django.shortcuts import redirect
import random
class WheelView(ListView):
    model = Game
    template_name = 'wheel/wheel_list.html'

    def get(self, request):
        roll = request.session.get('roll', False)
        your_game = False
        if roll:
            del(request.session['roll'])
            games = Game.objects.order_by('?')[:5]
            your_game = random.choice(games)
            your_game.points = your_game.sol_scored()
            your_game.langs = ', '.join([str(l) for l in your_game.languages.all()])
            your_game.gs = ', '.join([str(l) for l in your_game.genres.all()])
            your_game.ts = ', '.join([str(l) for l in your_game.tags.all()])
            your_game.price = int(your_game.ru_price/100)
            your_game.steam_link = 'https://store.steampowered.com/app/' + str(your_game.appid)
        else:
            games = Game.objects.order_by('?')[:5]

        ctx = {'random_list': games, 'your_game' : your_game}
        return render(request, self.template_name, ctx)

    def post(self, request):
        if 'roll' in request.POST:
            request.session['roll'] = True
        return redirect(request.path)



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

