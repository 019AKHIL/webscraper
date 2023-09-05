from django.http import HttpResponse
from django.shortcuts import render
from .models import Place, team


# Create your views here.
def demo(request):
    place = Place.objects.all()
    team_obj = team.objects.all()
    return render(request, "index.html", {'result': place,'team': team_obj})
