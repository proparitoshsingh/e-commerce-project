import re
from django.shortcuts import redirect, render
from django.http import HttpResponse
from pages.views import navbar_context, home_view, get_session

# Create your views here.
from .models import User


def auth_view(request):
    return render(request, 'registration.html', navbar_context)


def signup(request):
    if request.method == "POST":
        email = request.POST.get('email')
        pwd = request.POST.get('pass')

        if User.objects.filter(email=email).count() > 0:
            return HttpResponse('Username already exists.')
        else:
            print(email, pwd)
            obj = User.objects.create(email=email, password=pwd)
            obj.save()
            return redirect(auth_view)
    else:
        return render(request, 'registration.html', navbar_context)


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        pwd = request.POST.get('pass')

        check_user = User.objects.filter(email=email, password=pwd)
        print(request, check_user, email, pwd)
        if check_user:
            request.session['user'] = email
            if request.POST.get('name'):
                name = request.POST.get('name')
                navbar_context["uname"] = name.split()[0]
            else:
                navbar_context["uname"] = email
            return redirect(home_view)
        else:
            return HttpResponse('Please enter valid Username or Password.')

    return render(request, 'registration.html')

def logout(request):
    try:
        del request.session['user']
    except:
        return redirect(auth_view)
    
    navbar_context["uname"] = ""
    
    return redirect(auth_view)

def account_view(request):
    return render(request, 'account.html', navbar_context)

def cart_view(request):
    context = {}
    return render(request, 'cart.html', navbar_context)