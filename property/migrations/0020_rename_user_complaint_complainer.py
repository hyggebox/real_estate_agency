# Generated by Django 3.2.11 on 2022-01-26 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0019_auto_20220126_1531'),
    ]

    operations = [
        migrations.RenameField(
            model_name='complaint',
            old_name='user',
            new_name='complainer',
        ),
    ]