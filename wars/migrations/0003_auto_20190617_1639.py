# Generated by Django 2.2.2 on 2019-06-17 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wars', '0002_auto_20190617_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searched',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]