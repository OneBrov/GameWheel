from game_wheel.models import Game

def run():
    Game.objects.all().delete()
    print('Succesful deleting')