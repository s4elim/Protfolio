from .models import Profile
from django.shortcuts import render

# Create your views here.
def me(request):
    data = Profile.objects.latest('updated_at')
    return render(request,"index.html", {'data':data})

def home(request): 
    data = Profile.objects.all()
    return render(request,"home.html",{'datas': data})