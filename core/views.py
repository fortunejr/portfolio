from django.shortcuts import render
from django.shortcuts import render, redirect

# Home page
def index(request):
    return render(request, 'core/index.html')