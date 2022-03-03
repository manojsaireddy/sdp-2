from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.
from .models import User
def home(request):
    return render(request,"home.html")

def login(request):
    if request.method=='POST':
        uname=request.POST['username']
        pwd=request.POST['pass']
        flag=User.objects.filter(Q(Email=uname) & Q(password=pwd))
        if flag:
            request.session['uname']=uname
            return redirect("logouthome")
        else:
            messages.error(request, 'login invalid')
    return render(request,"login.html")
def signup(request):
    f=0
    if request.method == 'POST':
        if request.POST.get('mail') and request.POST.get('fname') and request.POST.get('lname') and request.POST.get('cpass') and request.POST.get('pass'):
            s=User()
            s.Email=request.POST.get('mail')
            s.Firstname = request.POST.get('fname')
            s.lastname = request.POST.get('lname')
            s.confirmpassword = request.POST.get('cpass')
            s.password=request.POST.get('pass')
            a=User.objects.raw('SELECT * from user_table')
            for p in a:
                if p.Email==s.Email or p.password==s.password:
                    f=1
                    break
            if (f == 1):
                messages.error(request, 'User already exists')
                return redirect('login')
            else:
                s.save()
                messages.success(request, 'Account was created successfully ')
                return redirect('login')
    return render(request,"signup.html")
def aboutus(request):
    return render(request,'aboutus.html')
def services(request):
    return render(request,'services.html')
def Residential(request):
    return render(request,'Residential.html')
def commercial(request):
    return render(request,'commercial.html')
def Lands(request):
    return render(request,'Lands.html')
def Hyderabad(request):
    return render(request,'Hyderabad.html')
def Vijayawada(request):
    return render(request,'Vijayawada.html')
def transaction(request):
    return render(request,'transaction.html')
    return redirect('home')

def logout(request):
    del request.session['uname']
    return redirect('home')
def logouthome(request):
    return render(request,'logouthome.html')
def changepwd1(request):
    uname = request.session['username']
    if (uname == None):
        return render(request, 'homepage.html')
    else:
        if request.method == 'POST':
            opwd = request.POST['opwd']
            npwd = request.POST['npwd']
            uname = request.session['username']
            flag = User.objects.filter(Q(username__iexact=uname) & Q(password__iexact=opwd))
            if flag:
                User.objects.filter(username=uname).update(password=npwd)
                return render(request, 'usershome.html')
            else:
                messages.error(request, "Give correct details")
                return HttpResponse("Give correct details")
        else:
            return render('changepwd.html')
        return render('changepwd.html')
def changepwd(request):
    uname = request.session['username']
    if (uname == None):
        return render(request, 'homepage.html')
    else:
        return render(request, 'changepwd.html', {'uname': uname})
