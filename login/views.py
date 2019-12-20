from django.shortcuts import render, redirect
from . import models
from .forms import UserForm, RegisterForm
import hashlib
from django.http import JsonResponse
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url


def hash_code(s, salt='Macintosh1984'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())    # update方法只接受bytes类型
    return h.hexdigest()


# Create your views here.
def index(request):
    pass
    return render(request, 'login/index.html')


def login(request):
    # 不允许重复登陆
    if request.session.get('is_login', None):
        return redirect('/index')

    # 图片验证码
    hashkey = CaptchaStore.generate_key()
    image_url = captcha_image_url(hashkey)

    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "请检查填写的内容!"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.User.objects.get(name=username)
                if user.password == hash_code(password): # 哈希值和数据库内的值进行比对
                    # 往session字段内写入用户状态和数据
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    return redirect('/index/')
                else:
                    message = "密码不正确!"
            except Exception as e:
                print(e)
                message = "用户名不存在!"
        # locals -- 返回当前所有本地变量字典
        return render(request, 'login/login.html', locals())
    login_form = UserForm()
    return render(request, 'login/login.html', locals())


def register(request):
    if request.session.get('is_login', None):
        # 登陆状态不允许注册
        return redirect('/index/')
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        message = "请检查填写的内容!"
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            if password1 != password2:
                message = "两次输入密码不一致"
                return render(request, 'login/register.html', locals())
            else:
                same_name_user = models.User.objects.filter(name= username)
                if same_name_user:
                    message = '用户已经存在，请重新选择用户名'
                    return render(request, 'login/register.html', locals())
                same_email_user = models.User.objects.filter(email=email)
                if same_email_user: # 邮箱地址唯一
                    message = '该邮箱地址已被注册，请使用别的邮箱'
                    return render(request, 'login/register.html', locals())
                new_user = models.User.objects.create()
                new_user.name = username
                new_user.password = hash_code(password1)    # 使用加密密码
                new_user.email = email
                new_user.sex = sex
                new_user.save()
                return redirect('/login/')
    register_form = RegisterForm()
    return render(request, 'login/register.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        return redirect('/index/')
    # 删除当前的会话数据和会话cookie
    request.session.flush()
    return redirect('/index/')