import json
from game_wheel.models import Tag, Language, Publisher, Developer, Label, Time_unit, Genre, Game

def add_games(file_name):
    fhand = open(file_name)
    print('File opened')
    games = json.load(fhand)
    fhand.close()
    print('For loop start')
    for game_id,game_data in games.items():

        try:
            d = Developer.objects.get_or_create(developer = game_data['dev'])[0]
            d.save()

            p = Publisher.objects.get_or_create(publisher = game_data['pub'])[0]
            p.save()

            time = Time_unit.objects.get_or_create(time_unit = game_data['time_unit'])[0]
            time.save()

            label = Label.objects.get_or_create(label = game_data['label'])[0]
            label.save()

            h_link = game_data['hltb_link']
            langs = []


            for lang in game_data['langs'].split(','):
                lang = Language.objects.get_or_create(language = lang)[0]
                langs.append(lang)
                lang.save()


            gs = []
            for g in game_data['genre']:
                g = Genre.objects.get_or_create(genre = g)[0]
                gs.append(g)
                g.save()


            ts = []
            for t in game_data['tags']:
                t = Tag.objects.get_or_create(tag = t)[0]
                ts.append(t)
                t.save()

        except Exception as e:
            print('Problems with colecting Foreign keys', e)
            continue


        try:
            g = Game(
                appid = game_data['appid'],
                name =  game_data['name'],
                possitive_count = game_data['pos_count'],
                negative_count = game_data['neg_count'],
                owners_count = int(game_data['owners']),
                ru_price = game_data['ru_price'],
                metascore = game_data['metascore'],
                price = game_data['price'],
                developer = d,
                publisher = p,
                duration = game_data['duration'],
                time_unit = time,
                label = label,
                hltb_link = h_link
            )
            print(g.name)
            g.save()

            g.languages.add(*langs)
            g.genres.add(*gs)
            g.tags.add(*ts)
            g.save()
        except Exception as e:
            print('many2many failed:',e)

def run(*args):
    try:
        f = input('Enter a file name which will be parsed (json format): ')
        print(1)
        if len(f) < 1:
            f = 'data.json'
        add_games(f)
        print(2)
    except:
        print('Oooops!! Some problem occur here')



