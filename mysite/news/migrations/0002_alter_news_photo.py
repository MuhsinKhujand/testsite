# Generated by Django 4.0 on 2022-04-28 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='photo',
            field=models.ImageField(height_field='400', upload_to='photos/%Y/%M/', verbose_name='photo', width_field='400'),
        ),
    ]
