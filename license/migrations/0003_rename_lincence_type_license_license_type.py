# Generated by Django 5.1.4 on 2025-03-05 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('license', '0002_rename_lincensetype_licensetype_license_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='license',
            old_name='lincence_type',
            new_name='license_type',
        ),
    ]
