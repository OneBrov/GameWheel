from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from django.forms.widgets import NumberInput


class SettingsForm(forms.Form):
    count_games = forms.IntegerField(initial = 5, validators = [MinValueValidator(3), MaxValueValidator(20)])
    duration_less = forms.FloatField(required=False,
                                    initial=9999,
                                    validators = [ MinValueValidator(1.0)],
                                    widget=forms.TextInput(attrs={'class' : 'myfieldclass'})
                                )

    duration_more = forms.FloatField(required=False,  initial=0,validators = [MinValueValidator(0)])

    ru_price_less = forms.IntegerField(required=False,initial =999999,validators = [MinValueValidator(1)])
    ru_price_more = forms.IntegerField(required=False,initial =0,validators = [MinValueValidator(0)])


