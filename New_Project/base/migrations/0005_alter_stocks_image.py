# Generated by Django 4.0.1 on 2022-01-30 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_stocks_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stocks',
            name='image',
            field=models.ImageField(upload_to='base/static/img/product'),
        ),
    ]