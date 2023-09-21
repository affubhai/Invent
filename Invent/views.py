from django.shortcuts import render,redirect
from .models import item,legger
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt   
from bs4 import BeautifulSoup
import requests
import html.parser
# Create your views here.

def home(request):

    return render(request, 'home.html')

def inventory(request):

    return render(request, 'inventory.html')

def log(request):
    logged_in_user = request.user
    logged_in_item = legger.objects.filter(company_name=logged_in_user.first_name)
    content = {
       'leggers': logged_in_item
    }
            
    return render(request,'log.html', content)
    
def menu(request):

    return render(request, 'menu.html')

def help(request):

    return render(request, 'help.html')

def inventory(request):
    logged_in_user = request.user
    logged_in_item = item.objects.filter(company_name=logged_in_user.first_name)
    context = {
       'items': logged_in_item
    }
            
    return render(request,'inventory.html', context)


@csrf_exempt
def add_item_form_submission(request):

    name = request.POST.get('name')
    price = request.POST.get('price')
    quantity = request.POST.get('quantity')
    code = request.POST.get('code')
    usernow = request.user

    item_info = item(name=name,price=price,quantity=quantity,item_code=code,company_name=usernow.first_name)
    item_info.save()

    log_info = legger(name=name,price=price,quantity=quantity,item_code=code,company_name=usernow.first_name)
    log_info.save()


    logged_in_user = request.user
    logged_in_item = item.objects.filter(company_name=logged_in_user.first_name)
    context = {
       'items': logged_in_item
    }
            
    return render(request,'inventory.html', context)

    


def add(request, id):
    if id:
        a = item.objects.get(id=id)
        count = a.quantity
        count += 1
        a.quantity = count
        a.save()

    return redirect('invent-inventory')

def subtract(request, id):
    if id:
        a = item.objects.get(id=id)
        count = a.quantity
        count -= 1
        a.quantity = count
        a.save()
        if count == 0:
            a.delete()
        else:
            pass

    return redirect('invent-inventory')

def delete(request, id):
    if id:
        a = item.objects.get(id=id)
        a.delete()
              

    return redirect('invent-inventory')

    