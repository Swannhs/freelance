# Generated by Django 3.2.6 on 2021-08-31 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=300)),
                ('slug', models.CharField(max_length=300)),
                ('description', models.TextField()),
            ],
        ),
    ]
