from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from store.models import store

@login_required(login_url='/user/signin/')
def index(request):
    if request.user.is_anonymous():
        user = 'AnonymousUser'
    else:
        user = request.user.username
    qs = store.objects.all().order_by('titleproduct','codeproduct','productdescription','priceproduct')
    return render_to_response('store/index.html', locals(), context_instance=RequestContext(request))