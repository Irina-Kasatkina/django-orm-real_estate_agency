# Generated by Django 2.2.4 on 2022-09-14 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0014_auto_20220912_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='new_building',
            field=models.BooleanField(null=True, verbose_name='Является ли новостройкой'),
        ),
    ]