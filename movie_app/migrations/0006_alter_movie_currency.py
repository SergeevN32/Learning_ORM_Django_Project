# Generated by Django 5.0.3 on 2024-04-05 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0005_movie_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='currency',
            field=models.CharField(choices=[('EUR', 'Euro'), ('USD', 'Dollars'), ('RUB', 'Rubles')], default='RUB', max_length=3),
        ),
    ]
