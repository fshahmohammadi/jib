from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render
from financial.models import Transaction
from financial.models import User

def trans(request, user_id):
    u= User.objects.get(name= user_id);
    t= Transaction.objects.all().filter(user= u.id )
    return render(request, "trans.html", {'trans' : t})
 