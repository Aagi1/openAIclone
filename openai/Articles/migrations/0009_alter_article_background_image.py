# Generated by Django 5.1.3 on 2024-11-12 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0008_model_remove_recherche_modeles_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='background_image',
            field=models.ImageField(upload_to=''),
        ),
    ]
