#coding=utf-8
from django.shortcuts import render
from django import forms
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from dome_app.models import User
class UserForm(forms.Form):
    username=forms.CharField(label='用户名',max_length=100)
    password=forms.CharField(label='密码',widget=forms.PasswordInput())
    email=forms.EmailField()
def register(request):
    if request.method=='POST':
        form=UserForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            email=form.cleaned_data['email']
            user=User()
            user.username=username
            user.password=password
            user.email=email
            user.save()
            return render_to_response('success.html',locals())
    else:
        form=UserForm()
    return render_to_response('register.html', locals())