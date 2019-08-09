from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Youtubejobs,Pick
from django.utils import timezone
from django.core.files.storage import FileSystemStorage
# Create your views here.

def home(request):
    return render(request, 'home.html')

def register(request):
    return render(request, 'register.html')

def signup(request):
    if request.method == 'POST':

        if request.POST['username'] == '' or request.POST['password'] == '':
            return render(request, 'signup.html', {'error':'아이디 비밀번호를 입력하세요'})
        
        if request.POST['password'] != request.POST['con_password']:
            return render(request, 'signup.html', {'error':'비밀번호 불일치'})

        try :
            user = User.objects.get(username = request.POST['username'])
            return render(request, 'signup.html', {'error':'이미 존재하는 이름'})
        except User.DoesNotExist:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
            auth.login(request, user)

            return redirect('/')


    else:
        return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        pw = request.POST['password']

        user = auth.authenticate(request, username = username, password = pw)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'error':'아이디, 비밀번호 확인'})

    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


def search(request):          
    title =  request.GET.get('search')
    if title != "":
        status = Youtubejobs.objects.filter(title__icontains=title)
    else: 
        status = False
    return render(request,'search.html',{'status':status})

def pick(request):
    pick = Pick.objects
    return render(request, 'pick.html', {'picks':pick})

def detail(request):
    return render(request, 'detail.html') 