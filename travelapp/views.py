from django.shortcuts import render
from.models import place
from.models import country
from django.http import HttpResponse


# Create your views here.
def fun(request):
    obj = place.objects.all()
    return render(request,"index.html",{'results':obj})

def nun(request):
    countries = country.objects.all()
    return render(request,"index.html",{'details':countries})


