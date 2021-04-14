from django.contrib import admin
from .models import Game, Tag, Developer, Publisher, Language, Label, Time_unit, Genre
# Register your models here.
admin.site.register(Game)
admin.site.register(Tag)
admin.site.register(Developer)
admin.site.register(Publisher)
admin.site.register(Language)
admin.site.register(Label)
admin.site.register(Time_unit)
admin.site.register(Genre)
