# Generated by Django 5.1.4 on 2025-01-19 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificate', '0005_certificatetype_relation_warish_warishancertificate'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='warishancertificate',
            options={'verbose_name': 'ওয়ারিশান সনদ', 'verbose_name_plural': 'ওয়ারিশান সনদ'},
        ),
        migrations.RenameField(
            model_name='certificate',
            old_name='mother_name_bangla',
            new_name='father_name_en',
        ),
        migrations.RenameField(
            model_name='certificate',
            old_name='father_name_bangla',
            new_name='mother_name_en',
        ),
        migrations.AlterField(
            model_name='certificate',
            name='email',
            field=models.EmailField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='nid',
            field=models.CharField(blank=True, max_length=17, null=True),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='phone',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='warishancertificate',
            name='email',
            field=models.EmailField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='warishancertificate',
            name='phone',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
    ]
