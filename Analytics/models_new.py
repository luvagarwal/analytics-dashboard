from django.db import models
from django.utils.encoding import smart_unicode

class TrackAllEF(models.Model):
    visit_id = models.CharField(max_length=128)
    action = models.CharField(max_length=8)
    apparel_id = models.IntegerField()
    merchant_id = models.IntegerField()
    price = models.IntegerField()
    time = models.DateTimeField(auto_now=True, auto_now_add=True)


class Visit(models.Model):
    visit_id = models.CharField(primary_key=True, max_length=128)
    time_enter = models.DateTimeField(auto_now=True, auto_now_add=True)
    time_exit = models.DateTimeField()
    user_id = models.IntegerField()
    # action id = 1 for try, 2 for share on fb,
    # 3 for share on gp, 4 for follow, 5 for buy
    device = models.CharField(max_length=6)
    country = models.CharField(max_length=25)
    browser = models.CharField(max_length=10)
    os = models.CharField(max_length=10)

    def __unicode__(self):
        return smart_unicode('apparel_id:%s|user_id:%s'%(self.apparel_id,self.user_id))

    class Meta:
        verbose_name = 'Actions'


class TrackFollow(models.Model):
    # user that follow the shared apparel
    user_follow_id = models.IntegerField()
    activity_id = models.ForeignKey(TrackAllEF)

    def __unicode__(self):
        return smart_unicode('user_shared:%s' % self.user_follow_id)

    class Meta:
        verbose_name = 'Followed Apparel'

