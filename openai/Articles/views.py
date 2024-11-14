from django.shortcuts import render
from .models import Article


def accueil(request):
    articles_chatgpt = Article.objects.filter(produit__nom='chatGPT')
    articles_recherche = Article.objects.filter(type_article='recherche')
    articles_storie = Article.objects.filter(type_article='stories')
    articles_business = Article.objects.filter(featured_bussiness='True')
    articles_api = Article.objects.filter(produit__nom='api')
    return render(request, 'Articles/pageAcceuil.html', {'articles_chatgpt': articles_chatgpt, 'articles_recherche': articles_recherche, 'articles_storie': articles_storie})

def test(request):
    articles_chatgpt = Article.objects.filter(produit__nom='chatGPT')
    return render(request, 'Articles/test.html', {'slides': articles_chatgpt})

def news_products(request):
    articles_produit = Article.objects.filter(type_article='produit')
    # Sélection des trois premiers articles
    top_three_articles = articles_produit[:3]
    # Sélection des autres articles restants
    remaining_articles = articles_produit[3:]
    # Nombre d'article produit
    nombre_articles = articles_produit.count()
    return render(request, 'Articles/news_base.html', {
        'section_title': 'Product',
        'top_three': top_three_articles,
        'others': remaining_articles,
        'nombre_articles': nombre_articles
    })

def news_research(request):
    articles_research = Article.objects.filter(type_article='recherche')
    top_three_articles = articles_research[:3]
    remaining_articles = articles_research[3:]
    nombre_articles = articles_research.count()

    return render(request, 'Articles/news_base.html', {
        'section_title': 'Research',
        'top_three': top_three_articles,
        'others': remaining_articles,
        'nombre_articles': nombre_articles
    })

def news_stories(request):
    articles_stories = Article.objects.filter(type_article='stories')
    top_three_stories = articles_stories[:3]
    remaining_stories = articles_stories[3:]
    nombre_stories = articles_stories.count()

    return render(request, 'Articles/news_base.html', {
        'section_title': 'Stories',
        'top_three': top_three_stories,
        'others': remaining_stories,
        'nombre_articles': nombre_stories
    })