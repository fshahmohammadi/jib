from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.contrib.auth import *
from django.template import RequestContext
from jib_site.settings import MEDIA_ROOT
from django.views.decorators.csrf import csrf_protect
from django.core.context_processors import csrf
from jib_auth.forms import *
from financial.models import Golden
import os.path	
import datetime


@csrf_protect
def login(request):
	if request.method == 'POST':
		f = login_form(request.POST)
		if f.is_valid():
			u = authenticate(username = f.cleaned_data['username'], password = f.cleaned_data['password'])
			if u is not None:
				return HttpResponseRedirect('/')
			else:
				error = 'Invalid Username/Password'

	f = login_form()
	return render_to_response('login.html', RequestContext(request,locals()))

@csrf_protect
def register(request):
	if request.method == 'POST':
		f = register_form(request.POST)
		if f.is_valid():
			if User.objects.filter(username = f.cleaned_data['username']).count() > 0 :
				error = 'Invalid Username'
			elif f.cleaned_data['password'] != f.cleaned_data['confirm']:
				error = 'password mismatch'
			else:
				User.objects.create_user(username = f.cleaned_data['username'], password=f.cleaned_data['password'], email = f.cleaned_data['email'], first_name=f.cleaned_data['name'], last_name=f.cleaned_data['lname'])
				error = 'registered successfully'

	f = register_form()
	return render_to_response('register.html', RequestContext(request,locals()))

@csrf_protect
def upgrade(request):
	if request.method == 'POST':
		f = upgrade_form(request.POST)
		if f.is_valid():
			g = Golden()
			g.user = request.user
			g.account = 0
			g.save()
			return render_to_response('text.html', {text : 'done'} )
	f = upgrade_form()
	return render_to_response('upgrade.html', RequestContext(request,locals()))
