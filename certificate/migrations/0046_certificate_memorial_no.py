# Generated by Django 5.1.4 on 2025-03-21 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificate', '0045_alter_certificate_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='memorial_no',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='স্মারক নং'),
        ),
    ]
