# Generated by Django 5.1.4 on 2025-03-08 07:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificate', '0036_alter_adress_mouja'),
        ('license', '0005_alter_license_adress_alter_license_adress_of_license'),
    ]

    operations = [
        migrations.AlterField(
            model_name='license',
            name='adress',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='certificate.adress', verbose_name='ঠিকানা'),
        ),
    ]
