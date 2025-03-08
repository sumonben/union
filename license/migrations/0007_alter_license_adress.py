# Generated by Django 5.1.4 on 2025-03-08 07:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('license', '0006_alter_license_adress'),
        ('region', '0009_othersadress_division'),
    ]

    operations = [
        migrations.AlterField(
            model_name='license',
            name='adress',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='region.othersadress', verbose_name='ঠিকানা'),
        ),
    ]
