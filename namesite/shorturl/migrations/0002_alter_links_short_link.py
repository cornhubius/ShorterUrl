# Generated by Django 3.2.9 on 2021-11-06 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shorturl', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='links',
            name='short_link',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
