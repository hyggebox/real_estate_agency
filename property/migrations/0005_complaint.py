# Generated by Django 3.2.11 on 2022-01-17 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_auto_20220117_1524'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('flat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.flat')),
            ],
        ),
    ]
