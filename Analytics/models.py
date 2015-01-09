from django.db import models
from django.utils.encoding import smart_unicode


class TrackAllEF(models.Model):
    # Primary Key field is automatically generated
    # id = models.AutoField(primary_key=True)
    time = models.DateTimeField(auto_now=True, auto_now_add=True)
    user_id = models.IntegerField()
    merchant_id = models.IntegerField()
    apparel_id = models.IntegerField()
    price = models.IntegerField()
    # action id = 1 for try, 2 for share on fb,
    # 3 for share on gp, 4 for follow, 5 for buy
    action = models.CharField(max_length=8)
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

# class ApparelShare(models.Model):
#     user_id = models.IntegerField()
#     time = models.DateTimeField(auto_now=True, auto_now_add=True)
#     shared_on = models.IntegerField()
#     apparel_id = models.IntegerField()
#     device_mobile = models.BooleanField(default=0)
#     location = models.IPAddressField()

#     def __unicode__(self):
#         return smart_unicode('apparel_id:%s|user_id:%s'%(self.apparel_id,self.user_id))

#     class Meta:
#         verbose_name = 'Shared Apparel'

# class MerchantProfile(User):
    
#     def __unicode__(self):
#         return smart_unicode(str(self.id) + ' | ' + self.username)

#     class Meta:
#         verbose_name = 'MerchantProfile'
