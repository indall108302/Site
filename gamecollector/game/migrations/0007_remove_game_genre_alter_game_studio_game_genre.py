# Generated by Django 4.2.1 on 2024-04-26 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0006_alter_game_genre_alter_game_studio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='genre',
        ),
        migrations.AlterField(
            model_name='game',
            name='studio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='genres', to='game.studio'),
        ),
        migrations.AddField(
            model_name='game',
            name='genre',
            field=models.ManyToManyField(blank=True, related_name='studios', to='game.genre'),
        ),
    ]
