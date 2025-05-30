# Generated by Django 5.2 on 2025-05-23 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('region', '0003_uniondetails_post_office'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImportantLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.IntegerField(default=10)),
                ('title', models.CharField(blank=True, max_length=500, null=True)),
                ('title_en', models.CharField(blank=True, max_length=500, null=True)),
                ('link', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'লিংকসমূহ',
                'verbose_name_plural': 'লিংকসমূহ',
                'ordering': ['serial'],
            },
        ),
    ]
