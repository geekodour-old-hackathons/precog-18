# Generated by Django 2.0 on 2017-12-12 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memes', '0004_auto_20171212_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meme',
            name='mongoid',
            field=models.TextField(default='hFZgmxfBOzPojqX1', max_length=12, unique=True),
        ),
    ]
