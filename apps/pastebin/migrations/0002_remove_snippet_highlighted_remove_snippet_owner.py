# Generated by Django 4.2 on 2023-06-10 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pastebin', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='snippet',
            name='highlighted',
        ),
        migrations.RemoveField(
            model_name='snippet',
            name='owner',
        ),
    ]