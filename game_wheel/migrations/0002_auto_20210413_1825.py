# Generated by Django 3.1.7 on 2021-04-13 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game_wheel', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='ry_price',
            new_name='ru_price',
        ),
    ]
