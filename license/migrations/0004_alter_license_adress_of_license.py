# Generated by Django 5.1.4 on 2025-03-08 07:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('license', '0003_rename_lincence_type_license_license_type'),
        ('region', '0009_othersadress_division'),
    ]

    operations = [
        migrations.AlterField(
            model_name='license',
            name='adress_of_license',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='adress_of_linsence', to='region.othersadress', verbose_name='প্রতিষ্ঠানের ঠিকানা'),
        ),
    ]
