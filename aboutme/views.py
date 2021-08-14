from django.shortcuts import render
from aboutme import models
# Create your views here.
def home(request):
    aboutmes=models.Aboutme.objects.all()
    return render(request,'home.html',{'aboutmes':aboutmes})
