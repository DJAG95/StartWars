# Generated by Django 2.2.2 on 2019-06-17 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wars', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='searched',
            old_name='id_Film',
            new_name='id_Film_Visited',
        ),
    ]
