# Generated by Django 3.1.7 on 2021-03-28 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0004_manchar'),
    ]

    operations = [
        migrations.AddField(
            model_name='emergency',
            name='desc',
            field=models.CharField(default='...', max_length=200),
        ),
        migrations.AddField(
            model_name='manchar',
            name='desc',
            field=models.CharField(default='...', max_length=200),
        ),
        migrations.AddField(
            model_name='numbers',
            name='desc',
            field=models.CharField(default='...', max_length=200),
        ),
    ]
