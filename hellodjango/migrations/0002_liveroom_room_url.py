# Generated by Django 2.2.2 on 2019-06-11 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hellodjango', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='liveroom',
            name='room_url',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
