from django.shortcuts import render

# Create your views here.

def home(request):
    page_title = 'Accueil'
    return render(request, 'website/home.html', locals())