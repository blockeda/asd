# Generated by Django 5.1.4 on 2024-12-21 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
