from django.shortcuts import render

# Create your views here.
def index(request):
    """home page for the stock app"""
    return render(request, 'stockApp/index.html')