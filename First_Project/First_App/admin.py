from django.contrib import admin
from First_App.models import Account,Bank,Customer,SignUP
# Register your models here.
admin.site.register(Account)
admin.site.register(Customer)
admin.site.register(Bank)
admin.site.register(SignUP)
