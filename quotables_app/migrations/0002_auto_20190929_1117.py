# Generated by Django 2.2.5 on 2019-09-29 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quotables_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='poster',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quotes', to='quotables_app.User'),
        ),
    ]
