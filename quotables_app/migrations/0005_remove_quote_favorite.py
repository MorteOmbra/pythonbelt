# Generated by Django 2.2.5 on 2019-09-29 22:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotables_app', '0004_auto_20190929_1822'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quote',
            name='favorite',
        ),
    ]
