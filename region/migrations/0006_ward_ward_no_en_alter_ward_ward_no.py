# Generated by Django 5.1.4 on 2025-01-30 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('region', '0005_delete_word'),
    ]

    operations = [
        migrations.AddField(
            model_name='ward',
            name='ward_no_en',
            field=models.CharField(default='02', max_length=10),
        ),
        migrations.AlterField(
            model_name='ward',
            name='ward_no',
            field=models.CharField(max_length=10),
        ),
    ]
