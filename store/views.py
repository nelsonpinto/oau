from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.template import RequestContext

from store.models import store

def index(request):
    qs = store.objects.all().order_by('titleproduct','codeproduct','productdescription','priceproduct')
    return render_to_response('store/index.html', locals(), context_instance=RequestContext(request))