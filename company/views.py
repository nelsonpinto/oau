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

def page_not_found(request, template='404.html'):
    return default_page_not_found(request, template=template)

def server_error(request, template='500.html'):
    return default_server_error(request, template=template)

def home(request):
    return render_to_response('home.html', locals(), context_instance=RequestContext(request))

def index(request):
    qs = client.objects.all().order_by('company','nameproyect','division','description')
    return render_to_response('company/index.html', locals(), context_instance=RequestContext(request))

def user_new(request):
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            return HttpResponseRedirect('/')
    else:
        formulario = UserCreationForm()
    return render_to_response('company/user_new.html',{'formulario':formulario}, context_instance=RequestContext(request))

def user_sign_in(request):
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            return HttpResponseRedirect('/')
    else:
        formulario = UserCreationForm()
    return render_to_response('company/user_new.html',{'formulario':formulario}, context_instance=RequestContext(request))



