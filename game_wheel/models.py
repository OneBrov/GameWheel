from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator
import random
# Create my models here.
class Tag(models.Model):
    tag = models.CharField(max_length = 100,unique=True)
    def __str__(self):
        return self.tag

class Language(models.Model):
    language = models.CharField(max_length = 100,unique=True)
    def __str__(self):
        return self.language

class Publisher(models.Model):
    publisher =  models.CharField(max_length = 100,unique=True)
    def __str__(self):
        return self.publisher

class Developer(models.Model):
    developer =  models.CharField(max_length = 100,unique=True)
    def __str__(self):
        return self.developer

class Label(models.Model): # Label - for duration. ex: main story, solo...
    label = models.CharField(max_length = 100,unique=True)
    def __str__(self):
        return self.label

class Time_unit(models.Model): # Time unit - hours , minutes
    time_unit = models.CharField(max_length = 100, unique=True)
    def __str__(self):
        return self.time_unit

class Genre(models.Model):
    genre = models.CharField(max_length = 100,unique=True)
    def __str__(self):
        return self.genre


# all data about games what we have
class Game(models.Model):
    appid = models.IntegerField() # Id on the steam
    name = models.CharField(max_length = 100)
    possitive_count = models.IntegerField(
        validators = [MinValueValidator(1, 'Count of reviews must be bigger than 1')]
    )
    negative_count = models.IntegerField(
        validators = [MinValueValidator(1, 'Count of reviews must be bigger than 1')]
    )
    owners_count = models.IntegerField()
    ru_price = models.IntegerField()
    metascore = models.IntegerField()
    price = models.IntegerField()

    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    duration  = models.FloatField()
    time_unit = models.ForeignKey(Time_unit, on_delete=models.CASCADE)
    label = models.ForeignKey(Label, on_delete=models.CASCADE)
    hltb_link = models.CharField(max_length = 100)
    #image = models.FilePathField(path=images_path)    right now without images
    languages = models.ManyToManyField(Language)
    genres =    models.ManyToManyField(Genre)
    tags =      models.ManyToManyField(Tag)
    def __str__(self):
        return self.name + ' ' +  str(self.id)

    def sol_scored(self): # thanks to @Solenium_Sol
        dur = self.duration
        raw_points = 0
        dop_k = 1
        #evaluate score by duration
        if dur <= 3 or str(self.time_unit) == 'Mins':
            raw_points = 40   #author coms  1-3 — 40   4-8 —75   9-12 — 115   12-15 — 135   16-20 — 155   20+ — 200
        elif dur <= 8:
            raw_points = 75
        elif dur <= 12:
            raw_points = 115
        elif dur <= 15:
            raw_points = 135
        elif dur <=20:
            raw_points = 155
        else:
            raw_points = 200
            dop_k = dop_k + (dur-20)//5*0.05
        #hours to minutes
        if str(self.time_unit) != 'Mins':
            dur = dur*60
        k = random.randint(90, 115)/100 #author coms Умножаем дефолтное значение на рандом число от 0.95 до 1.15

        rubles = self.ru_price / 100
        if rubles / dur >= 1.5 and rubles / dur < 2.5 :
            dop_k = dop_k  + random.randint(0, 10)/100
     #author coms   Если отношение цены ко времени меньше 1.4, то не меняем значение, если отношение цены ко времени больше-равно 1.5,
     #то увеличиваем значение в 1.0 до 1.10 раз, если соотношение больше 2.5, то увеличиваем в 1.11 до 1.20

        if rubles / dur >= 2.5:
            dop_k = dop_k  + random.randint(11, 20)/100
        #build score
        score = raw_points * k * dop_k
        return int(score)

class Settings(models.Model):
    duration_less = models.FloatField()
    duration_more = models.FloatField()

    ru_price_less = models.IntegerField()
    ru_price_more = models.IntegerField()



class Droped_games(models.Model):
    user =  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    game =  models.ForeignKey(Game, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
