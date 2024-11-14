from django.contrib import admin
from .models import Produit, Sujet, Model, TypeRecherche, Recherche, Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'titre', 'type_article', 'mot_cle_principal', 'date_publication', 'produit', 'recherche')
    list_filter = ('type_article', 'date_publication')
    search_fields = ('titre', 'mot_cle_principal', 'type_article')
    autocomplete_fields = ['produit', 'recherche']
    date_hierarchy = 'date_publication'
    list_per_page = 20
    fieldsets = (
        ('Informations générales', {
            'fields': ('titre', 'mot_cle_principal', 'type_article', 'date_publication', 'background_image')
        }),
        ('Associations', {
            'fields': ('produit', 'recherche')
        }),
    )


@admin.register(Recherche)
class RechercheAdmin(admin.ModelAdmin):
    list_display = ('id', 'titre', 'description', 'date_recherche')
    list_filter = ('date_recherche',)
    search_fields = ('titre', 'description')
    filter_horizontal = ('sujets', 'types_recherche', 'models')
    date_hierarchy = 'date_recherche'
    ordering = ('-date_recherche',)


@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'description')
    search_fields = ('nom',)


@admin.register(Sujet)
class SujetAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom')
    search_fields = ('nom',)


@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom')
    search_fields = ('nom',)


@admin.register(TypeRecherche)
class TypeRechercheAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom')
    search_fields = ('nom',)
