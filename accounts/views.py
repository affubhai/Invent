
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.views.decorators.cache import cache_control
from Invent.models import item

def login(request):
    global user
    if request.method == 'POST':
        CompanyID = request.POST['CompanyId']
        Password = request.POST['Password']

        user = auth.authenticate(username=CompanyID,password=Password)

        if user is not None:
            auth.login(request, user)
            return render(request,'menu.html')
            
                      
        else:
            return HttpResponse('Invalid Details')
            return redirect('login')
    else:
        return render(request,'login.html')
    
 
def register(request):

    if request.method == 'POST':
        CompanyID = request.POST['CompanyId']
        CompanyName = request.POST['CompanyName']
        CompanyAddress = request.POST['CompanyAddress']
        CompanyContact = request.POST['CompanyContact']
        CompanyWebsite = request.POST['CompanyWebsite']
        Password = request.POST['Password']
        
        if User.objects.filter(username=CompanyID).exists():
            return HttpResponse('user id already taken')
            
        else:
            user = User.objects.create_user(username=CompanyID, password=Password, first_name=CompanyName)
            user.save();
            return redirect('login')
            
    
    else:
            return render(request,'register.html')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout(request):

    auth.logout(request)
    return redirect('/')
    return
    
