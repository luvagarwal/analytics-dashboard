import os
from os import listdir
from random import randint
from datetime import datetime

if __name__ == "__main__":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dressy.settings')
    
    from Analytics.models import TrackAllEF
    from home.models import Apparels
    for i in xrange(50):
        actions = ['try', 'shareFB', 'shareGP', 'follow', 'buy']
        action = actions[randint(0, 4)]
        apparel_id = randint(1, 14)
        user_id = randint(2, 3)
        devices = ['mobile', 'pc']
        device = devices[randint(0, 1)]
        countries = ['India', 'Cambodia', 'Canada', 'China', 'Denmark', 'Egypt', 'Iran']
        country = countries[randint(0, len(countries)-1)]
        browsers = ['firefox', 'safari', 'chrome']
        browser = browsers[randint(0, 2)]
        oss = ['linux', 'windows']
        os = oss[randint(0, 1)]
        price = randint(500, 10000)
        merchant_id = Apparels.objects.get(apparel_id=apparel_id).merchant_id
        # time = datetime(2014, randint(8, 10), randint(1, 30), randint(1, 12), 44, 56, 350892)
        time = datetime.today()
        data_insert = {
            'apparel_id': apparel_id,
            'user_id': user_id,
            'device': device,
            'country': country,
            'time': time,
            'merchant_id': merchant_id,
            'action': action,
            'price': price,
            'browser': browser,
            'os': os,
        }
        TrackAllEF(**data_insert).save()
