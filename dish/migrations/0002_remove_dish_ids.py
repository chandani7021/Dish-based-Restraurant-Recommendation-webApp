# Generated by Django 4.2.2 on 2023-06-27 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dish', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dish',
            name='ids',
        ),
    ]
