# Generated by Django 4.2.1 on 2024-04-18 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('plot', models.TextField(blank=True, verbose_name='Описание')),
                ('release_year', models.DateField(verbose_name='Год выпуска')),
                ('is_verify', models.BooleanField(default=False)),
            ],
        ),
    ]
