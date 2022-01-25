# Generated by Django 3.2.11 on 2022-01-25 14:25

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_auto_20220125_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='valid_phonenumber',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='Нормализованный номер владельца'),
        ),
    ]
