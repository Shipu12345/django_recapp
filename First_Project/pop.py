import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "First_Project.settings")

import django
django.setup()

import random
from First_App.models import Account,Bank,Customer
from faker import Faker

fake=Faker()

d={'Uttara Bank':101,'Janata Bank':102,'Islami Bank':103,'Sonali Bank':104,'Rupali Bank':105,'Duch Bangla Bank':106
,'Brac Bank':107,'Grameen Bank':108,'Basic Bank':109,'Bangladesh Bank':100}


t=random.randint(0,10)
print(t)
print(list(d)[t])
s=list(d)[t]
print(d[s])
