from django.shortcuts import render,redirect
from . models import re_tbl
from django.contrib import messages
from django.conf import settings

# Create your views here.

def index(request):
    return render(request, "index1.html")

def signup(request):
    if request.method == 'POST':
        rn = request.POST.get('rn')
        ds = request.POST.get('ds')
        ig = request.POST.get('ig')
        ins = request.POST.get('ins')
       

        obj = re_tbl.objects.create(rn=name, ds=ds, ig=ig, ins=ins)
        obj.save()
        if obj:
            return redirect("/log")  
        else:
            return render(request, "signup1.html")
         
    return render(request,"signup1.html")
 
