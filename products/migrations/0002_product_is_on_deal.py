# Generated by Django 3.2.22 on 2023-12-23 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_on_deal',
            field=models.BooleanField(default=False),
        ),
    ]
