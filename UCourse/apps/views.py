from django.shortcuts import render
from django.http import HttpResponse
from .models import Account
import bcrypt
# Create your views here.

def signup(request):
    if request.method =="GET":
        return render(request,"signup.html")
    elif request.method =="POST":
        passw = request.POST.get("pass",None)
        Account.objects.create(
            name = request.POST.get("name",None),
            date = request.POST.get("date", None),
            sdt = request.POST.get("num",None),
            email = request.POST.get("email",None),
            passwd = bcrypt.hashpw(passw.encode('utf8'),bcrypt.gensalt(14))),
        all_account = Account.objects.all()
        return render(request,"base.html", context = {
            "all" : all_account
        })
        
        
