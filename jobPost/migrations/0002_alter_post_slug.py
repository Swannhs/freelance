# Generated by Django 3.2.6 on 2021-08-31 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobPost', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.CharField(max_length=300, unique=True),
        ),
    ]
