from django.db import models

# Table des Produits
class Produit(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.nom


# Table des Sujets
class Sujet(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom


# Table des Modèles (ex: GPT-4)
class Model(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom


# Table des Types de Recherche
class TypeRecherche(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom


# Table des Recherches
class Recherche(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField()
    date_recherche = models.DateField()
    sujets = models.ManyToManyField(Sujet, related_name='recherches_sujet', blank=True)
    types_recherche = models.ManyToManyField(TypeRecherche, related_name='recherches_type', blank=True)
    models = models.ManyToManyField(Model, related_name='recherches_model', blank=True)

    def __str__(self):
        return self.titre


# Table des Articles
class Article(models.Model):
    TYPE_ARTICLE_CHOICES = [
        ('produit', 'Produit'),
        ('recherche', 'Recherche'),
        ('stories', 'Stories'),
        ('affaires', 'Affaires Globales'),
        ('info', 'Information sur l\'Entreprise'),
        ('securite', 'Sécurité'),
    ]

    titre = models.CharField(max_length=255)
    #titre_article = models.CharField(max_length=255)
    mot_cle_principal = models.CharField(max_length=255)
    date_publication = models.DateField(max_length=255)
    summary = models.CharField(max_length=255)
    background_image = models.ImageField()
    type_article = models.CharField(max_length=50, choices=TYPE_ARTICLE_CHOICES)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE, null=True, blank=True, related_name='articles')
    recherche = models.ForeignKey(Recherche, on_delete=models.SET_NULL, null=True, blank=True, related_name='articles')
    featured_bussiness = models.BooleanField(default=False)  # Nouveau champ pour indiquer les articles en page d'accueil

    def __str__(self):
        return self.titre
