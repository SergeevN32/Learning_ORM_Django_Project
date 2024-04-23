# Generated by Django 5.0.4 on 2024-04-07 15:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0010_director_remove_movie_director_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='movie_app.director'),
        ),
    ]
