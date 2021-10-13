from django.shortcuts import render
from django.http  import HttpResponse
from .models import Location,Category,photos

def welcome(request):
    ('welcome')
    # return HttpResponse('Welcome to gallaryx')
    return render(request, 'welcome.html')
