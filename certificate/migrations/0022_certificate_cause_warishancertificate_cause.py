# Generated by Django 5.1.4 on 2025-01-30 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificate', '0021_certificate_language_warishancertificate_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='cause',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='কারণঃ '),
        ),
        migrations.AddField(
            model_name='warishancertificate',
            name='cause',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='কারণঃ '),
        ),
    ]
