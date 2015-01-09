import os
from os import listdir
from random import randint

from django.core.files.images import ImageFile


if __name__ == "__main__":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dressy.settings')
    from home.models import PersonalProfile
    PersonalProfile(user_id=2, age=16, gender='male').save()
    PersonalProfile(user_id=3, age=20, gender='female').save()
