from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth import logout
#from judge.models import * 
#from judge.forms import *
from django.template import RequestContext
from jib_site.settings import MEDIA_ROOT
from django.views.decorators.csrf import csrf_protect
from django.core.context_processors import csrf
import os.path	
import datetime

def home(request):
	return render_to_response('home.html')

@csrf_protect
def login(request):
	if request.method == 'POST':
		pass
	else:
		f = login_form()
		return render_to_response('login.html')

		
