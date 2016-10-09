#coding=utf-8
from django.shortcuts import render,HttpResponse
from django import forms
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from dome_app.models import User
class UserForm(forms.Form):
    username=forms.CharField(label='用户名',max_length=100)
    password=forms.CharField(label='密码',widget=forms.PasswordInput())
    email=forms.EmailField()
class LoginForm(forms.Form):
    username=forms.CharField(label='用户名',max_length=100)
    password=forms.CharField(label='密码',widget=forms.PasswordInput())
def register(request):
    if request.method=='POST':
        form=UserForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            email=form.cleaned_data['email']
            username_get=User.objects.all().filter(username=username)
            email_get=User.objects.all().filter(email=email)
            if len(username_get)>0:
                return HttpResponse('该用户已经被注册，请换一个')
#            for email in user:
#                if user.email==email:
#                    result='该邮箱已经被注册'
#                    return render_to_response('faile.html', locals())
#                else:
            elif len(email_get) > 0:
                    return HttpResponse('该邮箱已经被注册，请换一个')
            else:
                user=User()
                user.username=username
                user.password=password
                user.email=email
                user.save()
                return render_to_response('success.html',locals())
    else:
        form=UserForm()
    return render_to_response('register.html', locals(),context_instance=RequestContext(request))
#登录
def login(request):
    if request.method=='POST':
        form_login=LoginForm(request.POST)
        if form_login.is_valid():
            #获取表单用户和密码
            usernme=form_login.cleaned_data['username']
            passwd=form_login.cleaned_data['password']
#            user=User.objects.filter(usernme__exact=usernme,passwd_exact=passwd)
            user_get=User.objects.all().filter(username=usernme,password=passwd)
            #获取表单数据与数据库进行比较
            if user_get:
                #比较登录成功跳转到index界面
                response=HttpResponseRedirect('index')
                #将username写入浏览器cookie失效时间为3600
                response.set_cookie('username',usernme,3600)
                return response
            else:
                #登录失败停留在login界面
                return HttpResponseRedirect('login')
    else:
        form_login=LoginForm()
    return render_to_response('login.html',locals())
#登录成功
def index(request):
    username=request.COOKIES.get('username','')
    return render_to_response('index.html',locals())
#退出登录
def logout(request):
    response=HttpResponse('logout ! !')
    #清理cookie里面保存的username
    response.delete_cookie('username')
    return response