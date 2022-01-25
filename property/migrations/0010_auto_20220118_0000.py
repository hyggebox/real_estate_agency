# Generated by Django 3.2.11 on 2022-01-17 21:00
import phonenumbers

from django.db import migrations


def convert_phone_number(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        parsed_phonenumber = phonenumbers.parse(flat.owners_phonenumber, "RU")
        if phonenumbers.is_valid_number(parsed_phonenumber):
            formatted_phonenumber = phonenumbers.format_number(
                parsed_phonenumber,
                phonenumbers.PhoneNumberFormat.E164
            )
            flat.valid_owners_phonenumber = formatted_phonenumber
            flat.save()


def move_backward(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        flat.valid_owners_phonenumber = None
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_flat_valid_owners_phonenumber'),
    ]

    operations = [
        migrations.RunPython(convert_phone_number, move_backward),
    ]
