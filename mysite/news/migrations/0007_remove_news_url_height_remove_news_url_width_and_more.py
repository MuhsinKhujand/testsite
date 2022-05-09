# Generated by Django 4.0.4 on 2022-04-28 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_category_news_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='url_height',
        ),
        migrations.RemoveField(
            model_name='news',
            name='url_width',
        ),
        migrations.AlterField(
            model_name='news',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='news.category', verbose_name='kategoriya'),
        ),
        migrations.AlterField(
            model_name='news',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='e-pochta'),
        ),
        migrations.AlterField(
            model_name='news',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/', verbose_name='foto'),
        ),
    ]
