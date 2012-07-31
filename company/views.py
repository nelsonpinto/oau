from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect

from django.views.defaults import page_not_found as default_page_not_found 
from django.views.defaults import server_error as default_server_error

from company.models import client

import os

def page_not_found(request, template='404.html'):
    return default_page_not_found(request, template=template)

def server_error(request, template='500.html'):
    return default_server_error(request, template=template)

def home(request):    
    if request.user.is_anonymous():
        user = 'AnonymousUser'
    else:
        user = request.user.username
    return render_to_response('home.html', locals(), context_instance=RequestContext(request))

def index(request):
    qs = client.objects.all().order_by('company','nameproyect','division','description')
    return render_to_response('company/index.html', locals(), context_instance=RequestContext(request))

def user_createaccount(request):
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            return HttpResponseRedirect('/')
    else:
        formulario = UserCreationForm()
    return render_to_response('company/user_createaccount.html',{'formulario':formulario}, context_instance=RequestContext(request))

def user_signin(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/user/private/')
    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            user = request.POST['username']
            password = request.POST['password']
            access = authenticate(username=user, password=password)
            if access is not None:
                if access.is_active:
                    login(request, access)
                    return HttpResponseRedirect('/user/private/')
                else:
                    return render_to_response('company/user_noactive.html', context_instance=RequestContext(request))
            else:
                return render_to_response('company/user_nouser.html', context_instance=RequestContext(request))
    else:
        formulario = AuthenticationForm()
    return render_to_response('company/user_signin.html',{'formulario':formulario}, context_instance=RequestContext(request))

@login_required(login_url='/user/signin/')
def user_private(request):
    user = request.user
    return render_to_response('company/user_private.html',{'user':user}, context_instance=RequestContext(request))

@login_required(login_url='/user/signin/')
def user_signout(request):
    logout(request)
    return HttpResponseRedirect('/')



