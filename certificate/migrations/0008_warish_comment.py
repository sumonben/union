# Generated by Django 5.1.4 on 2025-01-19 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificate', '0007_alter_adress_options_alter_relation_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='warish',
            name='comment',
            field=models.CharField(blank=True, choices=[('0', '------'), ('1', 'বর্তমানে মৃত')], max_length=25, null=True, verbose_name='মন্তব্য'),
        ),
    ]
