# Generated by Django 5.1.3 on 2024-11-11 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0002_rename_illustration_article_contenu_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='contenu',
            new_name='description',
        ),
        migrations.AddField(
            model_name='article',
            name='background_image',
            field=models.ImageField(blank=True, null=True, upload_to='articles/'),
        ),
    ]
