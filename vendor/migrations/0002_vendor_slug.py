# Generated by Django 4.1 on 2022-10-30 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='slug',
            field=models.SlugField(default='timezone', max_length=200),
            preserve_default=False,
        ),
    ]
