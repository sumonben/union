# Generated by Django 5.1.4 on 2025-03-05 15:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0006_secretary'),
        ('certificate', '0034_alter_certificate_description'),
        ('payment', '0006_paymentpurpose_certificate_type_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='LincenseType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.IntegerField(default=10)),
                ('name', models.CharField(max_length=250)),
                ('name_en', models.CharField(max_length=250)),
                ('amount', models.IntegerField(default=10)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': ' লাইসেন্স-এর ধরণ',
                'verbose_name_plural': ' লাইসেন্স-এর ধরণ',
                'ordering': ['serial'],
            },
        ),
        migrations.CreateModel(
            name='Lincense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lincensed_name', models.CharField(max_length=500, verbose_name='প্রতিষ্ঠানের নাম(বাংলায়)')),
                ('lincensed_name_en', models.CharField(blank=True, max_length=500, null=True, verbose_name='প্রতিষ্ঠানের নাম (ইংরেজিতে)')),
                ('lincense_owner_name', models.CharField(max_length=500, verbose_name='লাইসেন্সধারীর নাম(বাংলায়)')),
                ('lincense_owner_name_en', models.CharField(blank=True, max_length=500, null=True, verbose_name='লাইসেন্সধারীর নাম (ইংরেজিতে)')),
                ('email', models.EmailField(blank=True, max_length=100, null=True, verbose_name='ইমেইল(যদি থাকে)')),
                ('phone', models.CharField(blank=True, max_length=11, null=True, verbose_name='মোবাইল নং')),
                ('nid', models.CharField(blank=True, max_length=17, null=True, verbose_name='জাতীয় পরিচপত্র')),
                ('passport', models.CharField(blank=True, max_length=17, null=True, verbose_name='পাসপোর্ট নং (যদি থাকে)')),
                ('father_name', models.CharField(max_length=500, verbose_name='বাবার নাম(বাংলায়)')),
                ('father_name_en', models.CharField(blank=True, max_length=500, null=True, verbose_name='বাবার নাম(ইংরেজিতে)')),
                ('mother_name', models.CharField(max_length=500, verbose_name='মায়ের নাম(বাংলায়)')),
                ('mother_name_en', models.CharField(blank=True, max_length=500, null=True, verbose_name='মায়ের নাম(ইংরেজিতে)')),
                ('description', models.TextField(blank=True, max_length=1000, null=True, verbose_name='বর্ণনাঃ')),
                ('caste', models.CharField(blank=True, max_length=500, null=True, verbose_name='সম্প্রদায়')),
                ('profession', models.CharField(blank=True, max_length=500, null=True, verbose_name='পেশা')),
                ('capital', models.IntegerField(blank=True, null=True, verbose_name='পরিশোধিত মূলধন')),
                ('tax', models.IntegerField(blank=True, null=True, verbose_name='কর')),
                ('fee', models.IntegerField(blank=True, null=True, verbose_name='ফি')),
                ('vat_n_others', models.IntegerField(blank=True, null=True, verbose_name='ভ্যাট ও অন্যান্য')),
                ('total_payment', models.IntegerField(blank=True, null=True, verbose_name='মোট প্রদেয়')),
                ('total_payment_in_word', models.CharField(blank=True, max_length=500, null=True, verbose_name='মোট প্রদেয়(কথায়)')),
                ('duration_form', models.DateTimeField(blank=True, null=True)),
                ('duration_to', models.DateTimeField(blank=True, null=True)),
                ('income', models.IntegerField(blank=True, null=True, verbose_name='আয়')),
                ('file', models.FileField(blank=True, null=True, upload_to='media/', verbose_name='মেম্বারের সুপারিশ ফাইল')),
                ('nid_file', models.FileField(blank=True, null=True, upload_to='media/', verbose_name='এনআইডি-জন্ম নিবন্ধন')),
                ('tracking_no', models.CharField(blank=True, max_length=25, null=True, verbose_name='ট্র্যাকিং নং')),
                ('is_verified', models.BooleanField(default=False, verbose_name='ভেরিফাইড কিনা?')),
                ('language', models.CharField(blank=True, max_length=250, null=True, verbose_name='ভাষা')),
                ('adress', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='certificate.adress', verbose_name='ঠিকানা')),
                ('adress_of_license', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='adress_of_linsence', to='certificate.adress', verbose_name='প্রতিষ্ঠানের ঠিকানা')),
                ('chairman', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.chairman', verbose_name='চেয়ারম্যান')),
                ('member', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.member', verbose_name='সদস্য')),
                ('person', models.ManyToManyField(blank=True, to='certificate.person', verbose_name='সংশিষ্ট ব্যক্তিবর্গ')),
                ('secretary', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.secretary', verbose_name='সচিব')),
                ('transaction', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='payment.transaction', verbose_name='ট্রান্সেকশন')),
                ('lincence_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='license.lincensetype', verbose_name='লাইসেন্সের ধরণ')),
            ],
            options={
                'verbose_name': 'লাইসেন্সসমূহ',
                'verbose_name_plural': 'লাইসেন্সসমূহ',
            },
        ),
    ]
