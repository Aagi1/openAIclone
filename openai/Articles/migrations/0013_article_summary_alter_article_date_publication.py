# Generated by Django 5.1.3 on 2024-11-14 07:44

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0012_article_featured_bussiness'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='summary',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='date_publication',
            field=models.DateField(max_length=255),
        ),
    ]
