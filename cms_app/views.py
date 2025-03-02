from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    context = {
        "title": "About",
        "isShow": True
    }
    return render(request, 'about.html', context)