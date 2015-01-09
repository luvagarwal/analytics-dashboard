# from django.db import connections
# from Analytics.models import TrackAllEF

# def dictfetchall(cursor):
#     "Returns all rows from a cursor as a dict"
#     desc = cursor.description
#     return [
#         dict(zip([col[0] for col in desc], row))
#         for row in cursor.fetchall()
#     ]

# def execute_custom_sql(query):
#     cursor = connections['analytics_db'].cursor()
#     cursor.execute(query)
#     return dictfetchall(cursor)

# def filter_browser(data, name_list):
#     """
#     Filter acc to browser
#     """
#     if()

# def generate_query(f_list):
#     """
#     Generate a raw sql query corresponding to the
#     given filter set
#     """
#     for a_list in f_list:
#         if a_list[0] == 'xaxis':
#             xaxis = a_list[1]

#     query="""
#     select a.time, a.action_id, %s from Analytics_trackallef a
#     join home_db.home_apparels b on a.apparel_id=b.apparel_id 
#     and a.merchant_id=b.merchant_id join home_db.home_personalprofile c
#     on a.user_id=c.user_id
#     """ % xaxis
#     for a_list in f_list:
#         sub_query = ""
#         if a_list[0] != 'xaxis' and a_list[0] != 'time':
#             for item in a_list[1]:
#             sub_query += 'and %s'
from datetime import datetime, timedelta


def get_time_list(current_time, num, unit):
# current_time =  
    item = current_time

    datetime_list=[]
    datetime_list.append(item)
    for i in xrange(num-1):
        if unit=='hour':
            item = item - timedelta(0,3600)
        if unit=='day':
            item = item - timedelta(1)
        if unit=='month':
            if item.month!=1:
                item = datetime(item.year,item.month-1,item.day,item.hour,item.second)
            else:
                item = datetime(item.year-1,12,item.day,item.hour,item.second)
        if unit=='year':
            item=datetime(item.year-1,item.month,item.day,item.hour,item.second)    
        datetime_list.append(item)
    return datetime_list


def dictify_params(params):
    params_dict = {}
    for param in params:
        params_dict[param[0]] = param[1]
    return params_dict


def filter_from_analytics_table(params):
    """
    Takes filters in form of dict and applies the
    filters in the analytics table
    """
    from Analytics.models import TrackAllEF
    result = TrackAllEF.objects.all().filter(merchant_id=params['merchant'])
    if 'browser' in params:
        result = result.filter(browser__in=params['browser'])
    if 'os' in params:
        result = result.filter(os__in=params['os'])
    if 'price' in params:
        result = result.filter(price__gt=params['price'][0]).filter(price__lt=params['price'][1])
    if 'time' in params:
        result = result.filter(date__gt=params['time'][0]).filter(price__lt=params['time'][1])
    if 'device' in params:
        result = result.filter(device__in=params['device'])
    if 'country' in params:
        result = result.filter(country__in=params['country'])
    return result


def filter_from_personal_table(qset, params):
    """
    NOT IMPLEMENTED (gender, age)
    apply filters in personal table
    """
    return qset


def xaxis_browser(qset):
    datatable = [['browser', 'try', 'sharefb', 'sharegp', 'follow', 'buy']]
    browsers = ['firefox', 'chrome', 'safari']
    for browser in browsers:
        temp_qset = qset.filter(browser=browser)
        try_count = temp_qset.filter(action='try').count()
        shareFB_count = temp_qset.filter(action='shareFB').count()
        shareGP_count = temp_qset.filter(action='shareGP').count()
        follow_count = temp_qset.filter(action='follow').count()
        buy_count = temp_qset.filter(action='buy').count()
        data = [browser, try_count, shareFB_count, shareGP_count,
                follow_count, buy_count]
        datatable.append(data)
    return datatable


def xaxis_os(qset):
    datatable = [['os', 'try', 'sharefb', 'sharegp', 'follow', 'buy']]
    oss = ['linux', 'windows']
    for os in oss:
        temp_qset = qset.filter(os=os)
        try_count = temp_qset.filter(action='try').count()
        shareFB_count = temp_qset.filter(action='shareFB').count()
        shareGP_count = temp_qset.filter(action='shareGP').count()
        follow_count = temp_qset.filter(action='follow').count()
        buy_count = temp_qset.filter(action='buy').count()
        data = [os, try_count, shareFB_count, shareGP_count,
                follow_count, buy_count]
        datatable.append(data)
    return datatable


def xaxis_device(qset):
    datatable = [['device', 'try', 'sharefb', 'sharegp', 'follow', 'buy']]
    devices = ['mobile', 'pc']
    for device in devices:
        temp_qset = qset.filter(device=device)
        try_count = temp_qset.filter(action='try').count()
        shareFB_count = temp_qset.filter(action='shareFB').count()
        shareGP_count = temp_qset.filter(action='shareGP').count()
        follow_count = temp_qset.filter(action='follow').count()
        buy_count = temp_qset.filter(action='buy').count()
        data = [device, try_count, shareFB_count, shareGP_count,
                follow_count, buy_count]
        datatable.append(data)
    return datatable
    

def xaxis_country(qset):
    datatable = [['country', 'try', 'sharefb', 'sharegp', 'follow', 'buy']]
    countries = []
    # change this temp to get top 5 buying countries
    temp = qset.filter(action='buy')[0:5]
    for i in temp:
        countries.append(i.country)
    for country in countries:
        temp_qset = qset.filter(country=country)
        try_count = temp_qset.filter(action='try').count()
        shareFB_count = temp_qset.filter(action='shareFB').count()
        shareGP_count = temp_qset.filter(action='shareGP').count()
        follow_count = temp_qset.filter(action='follow').count()
        buy_count = temp_qset.filter(action='buy').count()
        data = [country, try_count, shareFB_count, shareGP_count,
                follow_count, buy_count]
        datatable.append(data)
    return datatable


def xaxis_age(qset):
    
    return None


def xaxis_gender(qset):
    return None


def xaxis_time(qset, unit):
    datatable = [['time - '+unit, 'try', 'sharefb', 'sharegp', 'follow', 'buy']]
    time_list = get_time_list(datetime.today(), 10, unit)
    print time_list
    for index in xrange(1, len(time_list)):
        temp_qset = qset.filter(time__lt=time_list[index]).filter(time__gt=time_list[index-1])
        try_count = temp_qset.filter(action='try').count()
        shareFB_count = temp_qset.filter(action='shareFB').count()
        shareGP_count = temp_qset.filter(action='shareGP').count()
        follow_count = temp_qset.filter(action='follow').count()
        buy_count = temp_qset.filter(action='buy').count()
        if unit == 'hour':
            time = time_list[index].hour
        elif unit == 'day':
            time = time_list[index].day
        elif unit == 'month':
            time = time_list[index].month
        elif unit == 'year':
            time = time_list[index].year
        data = [time, try_count, shareFB_count, shareGP_count,
                follow_count, buy_count]
        datatable.append(data)
    return datatable


def xaxis_price(qset):
    datatable = [['price', 'try', 'sharefb', 'sharegp', 'follow', 'buy']]
    price_list = []
    for i in xrange(0, 11):
        price_list.append(i*1000)
    for index in xrange(len(price_list))-1:
        temp_qset = qset.filter(price__gt=price_list[index]).filter(price__lt=price_list[index+1])
        try_count = temp_qset.filter(action='try').count()
        shareFB_count = temp_qset.filter(action='shareFB').count()
        shareGP_count = temp_qset.filter(action='shareGP').count()
        follow_count = temp_qset.filter(action='follow').count()
        buy_count = temp_qset.filter(action='buy').count()
        data = [price, try_count, shareFB_count, shareGP_count,
                follow_count, buy_count]
        datatable.append(data)
    return datatable


def xaxis_top_apparels(qset):
    datatable = [['Apparel ID', 'try', 'sharefb', 'sharegp', 'follow', 'buy']]
    top_apparels_list = []
    from django.db.models import Count
    result = qset.values('apparel_id').annotate(count=Count('apparel_id')).order_by('-count')        
    for i in result:
        top_apparels_list.append(int(i['apparel_id']))
        if len(top_apparels_list) >= 5:
            break
    for apparel_id in top_apparels_list:
        temp_qset = qset.filter(apparel_id=apparel_id)
        try_count = temp_qset.filter(action='try').count()
        shareFB_count = temp_qset.filter(action='shareFB').count()
        shareGP_count = temp_qset.filter(action='shareGP').count()
        follow_count = temp_qset.filter(action='follow').count()
        buy_count = temp_qset.filter(action='buy').count()
        data = [apparel_id, try_count, shareFB_count, shareGP_count,
                follow_count, buy_count]
        datatable.append(data)
    return datatable


def browser_pie(qset):
    datatable = []
    browsers = ['firefox', 'chrome', 'safari']
    for browser in browsers:
        temp_qset = qset.filter(browser=browser)
        buy_count = temp_qset.filter(action='buy').count()
        data = [browser, buy_count]
        datatable.append(data)
    return datatable    


def os_pie(qset):
    datatable = []
    oss = ['linux', 'windows']
    for os in oss:
        temp_qset = qset.filter(os=os)
        buy_count = temp_qset.filter(action='buy').count()
        data = [os, buy_count]
        datatable.append(data)
    return datatable    


def country_geo(qset):
    datatable = [['country', 'buy']]
    countries = ['India', 'Cambodia', 'Canada', 'China', 'Denmark', 'Egypt', 'Iran']
    for country in countries:
        temp_qset = qset.filter(country=country)
        buy_count = temp_qset.filter(action='buy').count()
        data = [country, buy_count]
        datatable.append(data)
    return datatable


def call_xaxis_graphs(qset, main, value):
    if main == 'browser':
        return xaxis_browser(qset)
    if main == 'os':
        return xaxis_os(qset)
    if main == 'device':
        return xaxis_device(qset)
    if main == 'country':
        return xaxis_country(qset)
    if main == 'age':
        return xaxis_age(qset)
    if main == 'gender':
        return xaxis_gender(qset)
    if main == 'time':
        return xaxis_time(qset, value)
    if main == 'price':
        return xaxis_price(qset)
