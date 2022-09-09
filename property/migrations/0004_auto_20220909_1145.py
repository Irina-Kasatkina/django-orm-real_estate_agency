# Generated by Django 2.2.24 on 2022-09-09 08:45

from django.db import migrations

def update_flat_new_building(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.exclude(construction_year__isnull=True):
        flat.new_building = flat.construction_year >= 2015
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_flat_new_building'),
    ]

    operations = [
        migrations.RunPython(update_flat_new_building)
    ]
