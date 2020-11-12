from django.shortcuts import render

# Create your views here.

def index(request):
    values = {
        'title':'Index'
    }
    return render(request, 'index.html', values)