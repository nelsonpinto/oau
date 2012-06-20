from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.template import RequestContext

from proyects.models import proyect

def index(request):
    qs = proyect.objects.all().order_by('nameproyect','stateproyect','company','division','description')
    return render_to_response('proyects/index.html', locals(), context_instance=RequestContext(request))