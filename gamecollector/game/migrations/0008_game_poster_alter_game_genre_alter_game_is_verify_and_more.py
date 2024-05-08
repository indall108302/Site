# Generated by Django 4.2.1 on 2024-04-27 07:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0007_remove_game_genre_alter_game_studio_game_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='poster',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='photos/%Y/%m/%d/', verbose_name='Обложка'),
        ),
        migrations.AlterField(
            model_name='game',
            name='genre',
            field=models.ManyToManyField(blank=True, related_name='genres', to='game.genre', verbose_name='Жанр'),
        ),
        migrations.AlterField(
            model_name='game',
            name='is_verify',
            field=models.BooleanField(choices=[(False, 'На проверке'), (True, 'Одобрено')], default=1, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='game',
            name='studio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='studios', to='game.studio', verbose_name='Студия'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='title',
            field=models.CharField(max_length=120, verbose_name='Жанр'),
        ),
        migrations.AlterField(
            model_name='studio',
            name='title',
            field=models.CharField(max_length=120, verbose_name='Студия'),
        ),
    ]
