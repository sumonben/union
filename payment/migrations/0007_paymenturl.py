# Generated by Django 5.1.4 on 2025-03-20 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0006_paymentpurpose_certificate_type_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentURL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'verbose_name': 'Payment Url',
                'verbose_name_plural': 'Payment Url',
            },
        ),
    ]
