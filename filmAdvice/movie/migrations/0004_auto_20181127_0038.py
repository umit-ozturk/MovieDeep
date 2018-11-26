# Generated by Django 2.1.2 on 2018-11-26 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_auto_20181127_0037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='imdb_id',
            field=models.PositiveIntegerField(default=0, verbose_name='IMDB ID'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='movie_id',
            field=models.PositiveIntegerField(default=0, verbose_name='Film ID'),
        ),
    ]