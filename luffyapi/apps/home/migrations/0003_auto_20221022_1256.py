# Generated by Django 2.2.2 on 2022-10-22 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20221022_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='img',
            field=models.ImageField(help_text='图片尺寸必须是:3840x800', null=True, upload_to='banner', verbose_name='轮播图'),
        ),
    ]
