# Generated by Django 5.2 on 2025-04-12 08:51

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
            name='PostOffice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('name_en', models.CharField(max_length=25)),
                ('post_code', models.CharField(blank=True, max_length=15, null=True)),
                ('post_code_en', models.CharField(blank=True, max_length=15, null=True)),
                ('link', models.CharField(blank=True, max_length=15, null=True)),
            ],
            options={
                'ordering': ['name_en'],
            },
        ),
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('name_en', models.CharField(max_length=25)),
                ('ward_no', models.CharField(max_length=10)),
                ('ward_no_en', models.CharField(default='02', max_length=10)),
                ('link', models.CharField(blank=True, max_length=15, null=True)),
            ],
            options={
                'ordering': ['name_en'],
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
                ('link', models.CharField(blank=True, max_length=50, null=True)),
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
                ('link', models.CharField(blank=True, max_length=50, null=True)),
                ('upazilla', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='region.upazilla')),
            ],
            options={
                'ordering': ['name_en'],
            },
        ),
        migrations.CreateModel(
            name='OthersAdress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.IntegerField(default=10)),
                ('holding_no', models.CharField(blank=True, max_length=100, null=True, verbose_name=' হোল্ডিং নং')),
                ('village', models.CharField(blank=True, max_length=50, null=True, verbose_name=' গ্রাম/মহল্লা')),
                ('post_office', models.CharField(blank=True, max_length=50, null=True, verbose_name='ডাকঘর ')),
                ('district', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='region.district', verbose_name=' জেলা ')),
                ('division', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='region.division', verbose_name=' বিভাগ ')),
                ('union', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='region.union', verbose_name=' ইউনিয়ন ')),
                ('upazilla', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='region.upazilla', verbose_name='উপজেলা ')),
            ],
            options={
                'verbose_name': 'অন্যান্য ঠিকানা',
                'verbose_name_plural': ' অন্যান্য ঠিকানা',
                'ordering': ['serial'],
            },
        ),
        migrations.CreateModel(
            name='Village',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('name_en', models.CharField(max_length=25)),
                ('link', models.CharField(blank=True, max_length=15, null=True)),
                ('post_office', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='region.postoffice')),
                ('ward', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='region.ward')),
            ],
            options={
                'ordering': ['name_en'],
            },
        ),
        migrations.CreateModel(
            name='Mouja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('name_en', models.CharField(max_length=25)),
                ('link', models.CharField(blank=True, max_length=15, null=True)),
                ('post_office', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='region.postoffice')),
                ('village', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='region.village')),
                ('ward', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='region.ward')),
            ],
            options={
                'ordering': ['name_en'],
            },
        ),
    ]
