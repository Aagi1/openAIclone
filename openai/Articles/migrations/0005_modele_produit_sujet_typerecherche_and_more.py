# Generated by Django 5.1.3 on 2024-11-12 05:49

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0004_company_globalaffairs_model_product_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Modele',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('version', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Sujet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TypeRecherche',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='article',
            name='company',
        ),
        migrations.RemoveField(
            model_name='article',
            name='globalAffairs',
        ),
        migrations.RemoveField(
            model_name='research',
            name='models',
        ),
        migrations.RemoveField(
            model_name='article',
            name='product',
        ),
        migrations.RemoveField(
            model_name='research',
            name='topics',
        ),
        migrations.RemoveField(
            model_name='research',
            name='types',
        ),
        migrations.RemoveField(
            model_name='article',
            name='research',
        ),
        migrations.RemoveField(
            model_name='article',
            name='safetyAndAlignements',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='description',
            new_name='contenu',
        ),
        migrations.RemoveField(
            model_name='article',
            name='background_image',
        ),
        migrations.AddField(
            model_name='article',
            name='type_article',
            field=models.CharField(choices=[('produit', 'Produit'), ('recherche', 'Recherche'), ('affaires', 'Affaires Globales'), ('info', "Information sur l'Entreprise"), ('securite', 'Sécurité')], default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='date_publication',
            field=models.DateField(),
        ),
        migrations.AddField(
            model_name='article',
            name='produit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='Articles.produit'),
        ),
        migrations.CreateModel(
            name='Recherche',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('modeles', models.ManyToManyField(blank=True, related_name='recherches', to='Articles.modele')),
                ('sujets', models.ManyToManyField(blank=True, related_name='recherches', to='Articles.sujet')),
                ('types_recherche', models.ManyToManyField(blank=True, related_name='recherches', to='Articles.typerecherche')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='recherche',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='articles', to='Articles.recherche'),
        ),
        migrations.DeleteModel(
            name='Company',
        ),
        migrations.DeleteModel(
            name='GlobalAffairs',
        ),
        migrations.DeleteModel(
            name='Model',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
        migrations.DeleteModel(
            name='Type',
        ),
        migrations.DeleteModel(
            name='Research',
        ),
        migrations.DeleteModel(
            name='SafetyAndAlignements',
        ),
    ]
