# Generated by Django 2.2.4 on 2022-09-12 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_auto_20220912_1644'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owner_pure_phone',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owners_phonenumber',
        ),
    ]
