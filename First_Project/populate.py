import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "First_Project.settings")

import django
django.setup()

import random
from First_App.models import Account,Bank,Customer
from faker import Faker

fake=Faker()

Bank_names={'Uttara Bank':101,'Janata Bank':102,'Islami Bank':103,'Sonali Bank':104,'Rupali Bank':105,'Duch Bangla Bank':106
,'Brac Bank':107,'Grameen Bank':108,'Basic Bank':109,'Bangladesh Bank':100}

def add_bank():
    num=random.randint(0,9)
    random_bank_name=list(Bank_names)[num]
    random_bank_id=Bank_names[random_bank_name]
    t=Bank.objects.get_or_create(Bank_ID=random_bank_id,Bank_Name=random_bank_name)[0]
    t.save()
    return t

def populate(N=5):
    for every in range(N):
        bank_ready=add_bank()
        fake_customer=fake.name()
        fake_customer_id=fake.msisdn()
        fake_amount=fake.zipcode()

        custo=Customer.objects.get_or_create(Cus_ID=fake_customer_id,Cus_Name=fake_customer)[0]

        acc=Account.objects.get_or_create(C_ID=custo,B_ID=bank_ready,Ammount=fake_amount)[0]

if __name__=='__main__':
    print('Populating Script...')
    populate(20)
    print("Populating Completed!")
