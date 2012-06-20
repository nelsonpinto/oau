from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.template import RequestContext

def index(request):
    qs = User.objects.all().order_by('username','first_name','last_name')
    return render_to_response('store/index.html', locals(), context_instance=RequestContext(request))