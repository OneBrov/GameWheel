from django.urls import path, reverse_lazy
from . import views

app_name='wheel'
urlpatterns = [
    path('', views.WheelView.as_view(), name='wheel'),

    path('game/create',
        views.GameCreateView.as_view(success_url=reverse_lazy('wheel:wheel')), name='game_create'),

    path('tag/create',
        views.TagCreateView.as_view(success_url=reverse_lazy('wheel:wheel')), name='tag_create'),

    path('language/create',
        views.LanguageCreateView.as_view(success_url=reverse_lazy('wheel:wheel')), name='language_create'),

    path('publisher/create',
        views.PublisherCreateView.as_view(success_url=reverse_lazy('wheel:wheel')), name='publisher_create'),

    path('developer/create',
        views.DeveloperCreateView.as_view(success_url=reverse_lazy('wheel:wheel')), name='developer_create'),

    path('label/create',
        views.LabelCreateView.as_view(success_url=reverse_lazy('wheel:wheel')), name='label_create'),

    path('time_unit/create',
        views.Time_unitCreateView.as_view(success_url=reverse_lazy('wheel:wheel')), name='time_unit_create'),

    path('genre/create',
        views.GenreCreateView.as_view(success_url=reverse_lazy('wheel:wheel')), name='genre_create'),




]


