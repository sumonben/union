# Generated by Django 5.1.4 on 2025-01-30 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificate', '0020_alter_certificatetype_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='language',
            field=models.CharField(blank=True, choices=[('1', 'বাংলা'), ('2', 'English')], max_length=25, null=True, verbose_name='ভাষা'),
        ),
        migrations.AddField(
            model_name='warishancertificate',
            name='language',
            field=models.CharField(blank=True, choices=[('1', 'বাংলা'), ('2', 'English')], max_length=25, null=True, verbose_name='ভাষা'),
        ),
    ]
