from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse

from .models import Article
from .models import Comment

# Create your views here.
# def index(request):
#     # return HttpResponse('Hello from Python!')
#     return render(request, "index.html")

def index(request):
    return render(request, "index.html")

def board(request, type):
    articles = Article.objects.filter(board_type=type)
    paginator = Paginator(articles, 25)

    page = request.GET.get('page')
    articles = paginator.get_page(page)

    return render(request, "board.html", {"articles": articles})

def article(request, id):

    article = Article.objects.get(pk=id)
    comments = Comment.objects.filter(article_id=id)

    return render(request, "article.html", {"article": article, "comments": comments})
