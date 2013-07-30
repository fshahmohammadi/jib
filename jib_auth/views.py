from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.contrib.auth import *
from django.template import RequestContext
from jib_site.settings import MEDIA_ROOT
from django.views.decorators.csrf import csrf_protect
from django.core.context_processors import csrf
from jib_auth.forms import *
import os.path	
import datetime


@csrf_protect
def login(request):
	if request.method == 'POST':
		f = login_form(request.POST)
		if f.is_valid():
			print "f is valid"
			print f.cleaned_data['username']
			print f.cleaned_data['password']
			u = authenticate(username = f.cleaned_data['username'], password = f.cleaned_data['password'])
			if u is not None:
				return HttpResponseRedirect('/')
			else:
				error = 'Invalid Username/Password'

	f = login_form()
	return render_to_response('login.html', RequestContext(request,locals()))


