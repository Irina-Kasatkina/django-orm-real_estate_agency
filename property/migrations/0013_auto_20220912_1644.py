# Generated by Django 2.2.4 on 2022-09-12 13:44

from django.db import migrations


def relate_owner_and_flat(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')

    flat_set = Flat.objects.all()
    for flat in flat_set.iterator():
        owner, _ = Owner.objects.get_or_create(
            fullname=flat.owner,
            pure_phone=flat.owner_pure_phone
        )
        owner.flats_in_property.add(flat)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_auto_20220912_1618'),
    ]

    operations = [
        migrations.RunPython(relate_owner_and_flat)
    ]
