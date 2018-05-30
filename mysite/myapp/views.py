from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'index.html')
def tools(request):
    return render(request,'tools.html')
def tricks(request):
    return render(request,'tricks.html')
