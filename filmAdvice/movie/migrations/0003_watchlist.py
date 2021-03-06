# Generated by Django 2.1.2 on 2019-01-08 23:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movie', '0002_watchhistory'),
    ]

    operations = [
        migrations.CreateModel(
            name='WatchList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Kayıt Tarihi')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Güncellenme Tarihi')),
                ('movie', models.ForeignKey(blank=True, max_length=250, null=True, on_delete=django.db.models.deletion.CASCADE, to='movie.Movie')),
                ('user', models.ForeignKey(blank=True, max_length=250, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'İzlemek İstediklerim',
                'ordering': ('-created_at',),
            },
        ),
    ]
