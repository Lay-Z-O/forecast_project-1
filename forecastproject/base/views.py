from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def base(request):
    return render(request, 'base.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def home(request):
    return render(request, 'homepage.html')

def overview(request):
    return render(request, 'overview.html')

def forecast(request):
    return render(request, 'forecast.html')

def information(request):
    return render(request, 'information.html')

def profile(request):
    return render(request, 'profile.html')