from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate
from django.contrib.auth import logout as auth_logout
from django.views.decorators.csrf import csrf_exempt
from .models import User

@csrf_exempt
def login(request):
    if request.method == "GET":
        return render(request, "accounts/login.html")

    elif request.method == "POST":
        email = request.POST.get("inputEmail", None)
        password = request.POST.get("inputPassword", None)

        res = {}

        if not email:
            res['error'] = '이메일을 입력해주세요.'
        elif not password:
            res['error'] = '비밀번호를 입력해주세요.'
        else:
            try:
                user = User.objects.get(email=email)
                if check_password(password, user.password):
                    request.session['user'] = user.id
                    return redirect('/')
                else:
                    res['error'] = '비밀번호가 틀렸습니다.'
            except:
                res['error'] = '이메일이 존재하지 않습니다.'
        return render(request, "accounts/login.html", res)

@csrf_exempt
def register(request):
    if request.method == "GET":
        return render(request, "accounts/register.html")

    elif request.method == "POST":
        email = request.POST.get("inputEmail", None)
        password = request.POST.get("inputPassword", None)
        check_password = request.POST.get("checkPassword", None)

        res = {}

        if not (email and password and check_password):
            res['error'] = '모든 값을 입력해야 합니다.'
        elif password != check_password:
            res['error'] = '비밀번호가 다릅니다.'
        elif User.objects.get(email=email):
            res['error'] = '이미 가입돼있는 이메일입니다.'
        else:
            user = User(email=email, password=make_password(password))
            user.save()
        return render(request, "accounts/register.html", res)
    
def logout(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    auth_logout(request) # 세션 제거 & requset.user 값 초기화
    return redirect('/')