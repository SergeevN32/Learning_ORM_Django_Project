# Generated by Django 5.0.3 on 2024-04-08 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0013_actor_photo_actor_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='photo',
            field=models.ImageField(blank=True, default='movie_app/static/movie_app/img/actors/def.jpg', null=True, upload_to='movie_app/static/movie_app/img/actors'),
        ),
    ]