import os
from os import listdir
from random import randint

from django.core.files.images import ImageFile


if __name__ == "__main__":
   os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dressy.settings')
   from home.models import Apparels

   src_dir = raw_input('Input the name of image directory that you want to dump in Apparels database: ')
   src_images = listdir(src_dir)
   count = 0
   for img in src_images:
        count += 1
        Apparels(price=randint(1000,10000), merchant_id=randint(1, 3),
        apparel_id=count, image=ImageFile(file(src_dir+'/'+img))
    ).save()
