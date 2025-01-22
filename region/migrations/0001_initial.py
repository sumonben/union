# Generated by Django 5.1.4 on 2025-01-22 04:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True)),
                ('name_en', models.CharField(max_length=15, unique=True)),
                ('link', models.CharField(blank=True, max_length=15, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True)),
                ('name_en', models.CharField(max_length=25, unique=True)),
                ('lattitude', models.CharField(blank=True, max_length=15, null=True)),
                ('longitude', models.CharField(blank=True, max_length=15, null=True)),
                ('link', models.CharField(blank=True, max_length=15, null=True)),
                ('division', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='region.division')),
            ],
            options={
                'ordering': ['name_en'],
            },
        ),
        migrations.CreateModel(
            name='Upazilla',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('name_en', models.CharField(max_length=25)),
                ('link', models.CharField(blank=True, max_length=15, null=True)),
                ('district', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='region.district')),
            ],
            options={
                'ordering': ['name_en'],
            },
        ),
        migrations.CreateModel(
            name='Union',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('name_en', models.CharField(max_length=25)),
                ('link', models.CharField(blank=True, max_length=15, null=True)),
                ('upazilla', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='region.upazilla')),
            ],
            options={
                'ordering': ['name_en'],
            },
        ),
    ]
