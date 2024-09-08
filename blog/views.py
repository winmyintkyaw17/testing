from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def search_article(request):
    if request.method == 'GET':
        print(request.GET.get('article', 'all article get '))
    if request.method == 'POST':
        print(request.POST.get('article','all article post'))
    return render(request, 'search.html')

def index(request):
    return render(request, 'home.html')
    #return HttpResponse('Home Page')

def about(request):
    return render(request, 'about.html')

def article(request,id):
    return HttpResponse('The article is:'+ str(id))
def articlebyname(request,name):
    return HttpResponse('The artice name is'+ name)
def add_post(request):
    return render(request, 'add-post.html')
@require_http_methods(["POST"])
def add_post_to_database(request):
    return HttpResponse('Add post to database')
