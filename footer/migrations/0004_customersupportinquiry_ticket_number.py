# Generated by Django 3.2.22 on 2024-07-21 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('footer', '0003_customersupportinquiry'),
    ]

    operations = [
        migrations.AddField(
            model_name='customersupportinquiry',
            name='ticket_number',
            field=models.CharField(default='TEMP', editable=False, max_length=32),
            preserve_default=False,
        ),
    ]