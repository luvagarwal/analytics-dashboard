from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import ipdb
from datetime import datetime
from home.models import Apparels
import json
from .forms import GenerateReportForm, RegisterForm, LoginForm
import utils

def addrequest(request):
    action_id = request.GET.get('action_id', '')
    apparel_id = request.GET.get('apparel_id', '')
    user_id = request.user.id
    device_mobile = 0
    location = request.get_host()
    # if user_id is None:
    #     user_id=0
    from .models import ApparelTryShare
    data_insert = {
        'action_id': action_id,
        'apparel_id': apparel_id,
        'user_id': user_id,
        'device_mobile': device_mobile,
        'location': location,
    }
    ApparelTryShare(**data_insert).save()
    return HttpResponse(user_id)


def giveUserID(request):
    return HttpResponse(request.user.id)


def follow(request):
    apparel_id = request.GET.get('apparel_id', '')
    user_shared_id = request.GET.get('user_id', '')
    user_follow_id = request.user.id
    if user_follow_id is None:
        user_follow_id = -1
    device_mobile = 0
    location = request.get_host()
    data_insert = {
        'apparel_id': apparel_id,
        'user_shared_id': user_share_id,
        'user_follow_id': user_follow_id,
        'device_mobile': device_mobile,
        'location': location,
    }
    from .models import ApparelFollow
    ApparelFollow(**data_insert).save()
    return HttpResponseRedirect('/home')


def MerchantLogin(request):
    if request.POST:
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/Analytics/dashboard')

    return HttpResponseRedirect('/Analytics/register')


def MerchantLogout(request):
    logout(request)
    return HttpResponseRedirect('/Analytics/register')


def register(request):
    if request.POST:
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=request.POST['username'], password=request.POST['password1'])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/Analytics/dashboard')
        else:
            return HttpResponseRedirect('/Analytics/register')
    else:
        form = RegisterForm()
        lform = LoginForm()
        return render(request, 'Analytics/register.html',
                      {'RegisterForm': form, 'LoginForm': lform})


def initial_dashboard(request):
    """
    Initial dashboard
    """
    f_applied = request.GET.lists()
    params = utils.dictify_params(f_applied)
    params['merchant'] = request.user.id
    qset = utils.filter_from_analytics_table(params)
    qset = utils.filter_from_personal_table(qset, params)
    datatable_browser = utils.browser_pie(qset)
    datatable_os = utils.os_pie(qset)
    datatable_country = utils.country_geo(qset)
    datatable_top_apparels = utils.xaxis_top_apparels(qset)
    datatable_time = utils.xaxis_time(qset, 'month')
    print datatable_time
    # datatable_time = [['time - month', 'try', 'sharefb', 'sharegp', 'follow', 'buy'], [datetime.datetime(2014, 10, 15, 20, 36), 0, 0, 0, 0, 0], [datetime.datetime(2014, 9, 15, 20, 0), 0, 0, 0, 0, 0], [datetime.datetime(2014, 8, 15, 20, 0), 0, 0, 0, 0, 0], [datetime.datetime(2014, 7, 15, 20, 0), 0, 0, 0, 0, 0], [datetime.datetime(2014, 6, 15, 20, 0), 0, 0, 0, 0, 0], [datetime.datetime(2014, 5, 15, 20, 0), 0, 0, 0, 0, 0], [datetime.datetime(2014, 4, 15, 20, 0), 0, 0, 0, 0, 0], [datetime.datetime(2014, 3, 15, 20, 0), 0, 0, 0, 0, 0], [datetime.datetime(2014, 2, 15, 20, 0), 0, 0, 0, 0, 0]]
    context = {'b_datatable': datatable_browser, 'o_datatable': datatable_os,
               'country_datatable': datatable_country,
               'top_apparels': datatable_top_apparels,
               'time_datatable': datatable_time,
    }
    return render(request, 'Analytics/dashboard.html', context)


def filters_dashboard(request):
    """
    """
    f_applied = request.GET.lists()
    params = utils.dictify_params(f_applied)
    params['merchant'] = request.user.id
    qset = utils.filter_from_analytics_table(params)
    qset = utils.filter_from_personal_table(qset, params)
    datatable = utils.call_xaxis_graphs(qset, params['main'][0], 'fdfdfd')
    return HttpResponse(json.dumps(datatable))
