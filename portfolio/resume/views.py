from django.shortcuts import render
from django.http import HttpResponse
from .models import Skill

# Create your views here.
def portfolio(request):
    return render(request, "portfolio.html")

def portfolio2(request):
    return render(request, "portfolio2.html")

def home(request):
    skills=Skill.objects.all()
    data = {
        "first_name": "Ani",
        "last_name": "Asryan",
        "skills": skills  
    }
    return render(request, "index.html", context= data)
