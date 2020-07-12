from django.shortcuts import render
from django.http import HttpResponse,FileResponse

# Create your views here.

def home(request):
    return render(request, 'home.html',{})

def of(request):
    return HttpResponse ('you are the best programer')

    

