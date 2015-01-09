import os
from django.db import connections
from Analytics.models import TrackAllEF

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dressy.settings')
def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]
def my_custom_sql():
    cursor = connections['analytics_db'].cursor()

    cursor.execute("""select a.time, a.action_id,
                    b.price, c.age from Analytics_trackallef a join 
                    home_db.home_apparels b on a.apparel_id=b.apparel_id 
                    and a.merchant_id=b.merchant_id join home_db.home_personalprofile c
                    on a.user_id=c.user_id and c.age=16 """)
    print dictfetchall(cursor)

my_custom_sql()