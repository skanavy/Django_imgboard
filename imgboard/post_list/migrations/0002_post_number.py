# Generated by Django 2.2.19 on 2022-08-30 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_list', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='number',
            field=models.IntegerField(default=0),
        ),
    ]
