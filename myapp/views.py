
from django.http.response import HttpResponse
from django.shortcuts import render,HttpResponse
from myapp.models import Bookcab

# Create your views here.


def index(request):

    if request.method == "POST":
        name = request.POST.get('name')
        telephone = request.POST.get('telephone')
        cartype = request.POST.get('cars')
        pickadd = request.POST.get('name')
        dropadd = request.POST.get('dropadd')
        pickdateandtime = request.POST.get('pickdatetime')
        
        bookcab = Bookcab(name=name,telephone=telephone,cartype=cartype,pickadd=pickadd,dropadd=dropadd,pickdateandtime=pickdateandtime)
        bookcab.save()
        return render(request,"thanks.html")
  
    return render(request,'index.html')


def thanks(request):
    return render(request,"thanks.html")