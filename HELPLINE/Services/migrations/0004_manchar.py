# Generated by Django 3.1.7 on 2021-03-28 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0003_auto_20210328_1533'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manchar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('fname', models.CharField(max_length=200)),
                ('lname', models.CharField(max_length=200)),
                ('mobileno', models.CharField(max_length=200)),
                ('mail', models.CharField(max_length=200)),
            ],
        ),
    ]