import random
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from .models import Apparels


def login(request):
    return render(request,'home/login.html')

def logout(request):
    return HttpResponseRedirect('/login')

# @login_required(login_url='/login')
def index(request):
    total = Apparels.objects.count()
    apparel_details = {}
    while len(apparel_details)<9:
        num = random.randint(1, total)
        if num not in apparel_details:
            apparel_details[num]=''
    
    for app_id in apparel_details:
        apparel_details[app_id] = Apparels.objects.get(product_id=app_id).image.url
    return render(request, 'home/index.html',
                {'apparel_details': apparel_details, 'counter': 0}
        )
