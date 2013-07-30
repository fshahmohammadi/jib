from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render
from groups.models import Group
from financial.models import User
from groups.models import GroupTrans
# Create your views here.

def groups(request, user_id):
    g= Group.objects.filter(users__id__exact = user_id)
    return render(request, "groups.html", {'groups' : g})
    
def group(request, group_id):
    g= Group.objects.get(id = group_id)
    t= GroupTrans.objects.filter(group__id__exact=group_id)
    return render(request, "group.html", {'group' : g, 'trans' : t})
    
    
    
