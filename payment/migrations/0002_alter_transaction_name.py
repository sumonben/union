# Generated by Django 5.2 on 2025-05-20 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='name',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
