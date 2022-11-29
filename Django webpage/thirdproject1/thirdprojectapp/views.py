from django.http import HttpResponse
from django.shortcuts import render
from . models import place
from . models import members

def demo(request):
    obj=place.objects.all()
    obj2=members.objects.all()
    return render (request,'index.html',{'result':obj,'teams':obj2})
