# Generated by Django 5.2 on 2025-04-12 08:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('region', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.IntegerField(default=10)),
                ('name', models.CharField(max_length=25)),
                ('name_en', models.CharField(max_length=25)),
            ],
            options={
                'verbose_name': 'পদবী',
                'verbose_name_plural': 'পদবী',
                'ordering': ['name_en'],
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.IntegerField(default=10)),
                ('name', models.CharField(max_length=250, verbose_name=' নাম(বাংলায়)')),
                ('name_en', models.CharField(max_length=250, verbose_name=' নাম(ইংরেজিতে)')),
                ('phone', models.CharField(blank=True, max_length=11, null=True, verbose_name=' মোবাইল')),
                ('email', models.CharField(blank=True, max_length=250, null=True, verbose_name=' ই-মেইল(ইংরেজিতে)')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/', verbose_name='ছবি')),
                ('signature', models.ImageField(blank=True, null=True, upload_to='media/', verbose_name='স্বাক্ষর')),
                ('district', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='region.district', verbose_name='জেলা')),
                ('union', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='region.union', verbose_name='ইউনিয়ন')),
                ('upazilla', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='region.upazilla', verbose_name='উপজেলা')),
                ('ward', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='region.ward', verbose_name='ওয়ার্ড')),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.post', verbose_name='পদবী')),
            ],
            options={
                'verbose_name': 'মেম্বার',
                'verbose_name_plural': 'মেম্বার',
                'ordering': ['serial'],
            },
        ),
        migrations.CreateModel(
            name='Chairman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.IntegerField(default=10)),
                ('name', models.CharField(max_length=250, verbose_name=' নাম(বাংলায়)')),
                ('name_en', models.CharField(max_length=250, verbose_name=' নাম(ইংরেজিতে)')),
                ('phone', models.CharField(blank=True, max_length=11, null=True, verbose_name=' মোবাইল')),
                ('email', models.CharField(blank=True, max_length=250, null=True, verbose_name=' ই-মেইল(ইংরেজিতে)')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/', verbose_name='ছবি')),
                ('signature', models.ImageField(blank=True, null=True, upload_to='media/', verbose_name='স্বাক্ষর')),
                ('district', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='region.district', verbose_name='জেলা')),
                ('union', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='region.union', verbose_name='ইউনিয়ন')),
                ('upazilla', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='region.upazilla', verbose_name='উপজেলা')),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.post', verbose_name='পদবী')),
            ],
            options={
                'verbose_name': 'চেয়ারম্যান',
                'verbose_name_plural': 'চেয়ারম্যান',
                'ordering': ['serial'],
            },
        ),
        migrations.CreateModel(
            name='Secretary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.IntegerField(default=10)),
                ('name', models.CharField(max_length=250, verbose_name=' নাম(বাংলায়)')),
                ('name_en', models.CharField(max_length=250, verbose_name=' নাম(ইংরেজিতে)')),
                ('phone', models.CharField(blank=True, max_length=11, null=True, verbose_name=' মোবাইল')),
                ('email', models.CharField(blank=True, max_length=250, null=True, verbose_name=' ই-মেইল(ইংরেজিতে)')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/', verbose_name='ছবি')),
                ('signature', models.ImageField(blank=True, null=True, upload_to='media/', verbose_name='স্বাক্ষর')),
                ('district', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='region.district', verbose_name='জেলা')),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.post', verbose_name='পদবী')),
                ('union', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='region.union', verbose_name='ইউনিয়ন')),
                ('upazilla', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='region.upazilla', verbose_name='উপজেলা')),
            ],
            options={
                'verbose_name': 'সচিব',
                'verbose_name_plural': 'সচিব',
                'ordering': ['serial'],
            },
        ),
    ]
