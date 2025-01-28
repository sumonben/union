# Generated by Django 5.1.4 on 2025-01-28 15:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('region', '0003_postoffice_village_post_office'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='word',
            name='union',
        ),
        migrations.RemoveField(
            model_name='village',
            name='word',
        ),
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('name_en', models.CharField(max_length=25)),
                ('ward_no', models.CharField(max_length=25)),
                ('link', models.CharField(blank=True, max_length=15, null=True)),
                ('union', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='region.union')),
            ],
            options={
                'ordering': ['name_en'],
            },
        ),
        migrations.AddField(
            model_name='village',
            name='ward',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='region.ward'),
        ),
    ]
