# Generated by Django 2.2.5 on 2019-09-29 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotables_app', '0007_auto_20190929_1924'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quote',
            name='is_favorite',
        ),
        migrations.AddField(
            model_name='quote',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
    ]
