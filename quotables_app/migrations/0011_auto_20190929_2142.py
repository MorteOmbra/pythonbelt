# Generated by Django 2.2.5 on 2019-09-30 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotables_app', '0010_auto_20190929_2127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quote',
            name='favorited',
        ),
        migrations.AddField(
            model_name='quote',
            name='favorited',
            field=models.ManyToManyField(related_name='favorite_quotes', to='quotables_app.User'),
        ),
    ]
