# Generated by Django 3.0.8 on 2020-10-11 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.TextField(default='', max_length=130),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(max_length=1000),
        ),
    ]
