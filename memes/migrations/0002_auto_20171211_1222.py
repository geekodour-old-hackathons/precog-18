# Generated by Django 2.0 on 2017-12-11 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meme',
            name='url',
            field=models.URLField(db_index=True, editable=False, unique=True),
        ),
    ]
