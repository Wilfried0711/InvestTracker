# Generated by Django 5.1.1 on 2024-09-21 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='first_nanme',
            new_name='first_name',
        ),
    ]
