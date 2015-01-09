from django.db import models
from django.utils.encoding import smart_unicode


class Apparels(models.Model):
    apparel_id = models.IntegerField()
    merchant_id = models.IntegerField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='home/apparels/')

    def __unicode__(self):
        return smart_unicode(self.id)

    class Meta:
        verbose_name = 'Apparel'

class PersonalProfile(models.Model):
    user_id = models.IntegerField()
    age = models.IntegerField()
    gender = models.CharField(max_length=6)
