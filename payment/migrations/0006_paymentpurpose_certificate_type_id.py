# Generated by Django 5.1.4 on 2025-01-28 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0005_paymentpurpose_payment_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentpurpose',
            name='certificate_type_id',
            field=models.IntegerField(default=0),
        ),
    ]
