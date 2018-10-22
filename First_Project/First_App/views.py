from django.shortcuts import render
from django.http import HttpResponse
from First_App.models import Account,Bank,Customer
from First_App.forms import Form_Name
from First_App.forms1 import NewForm

# Create your views here.

def index(request):
    context_dict={'insert_me':'','text':'Hello World','number':100}
    return render(request,'First_App/index.html',context_dict)
def index1(request):
    return HttpResponse('Hello worldddddddddd')

def customer_list(request):
    cus_name_list=Customer.objects.order_by('Cus_Name')
    name_dict={'cus_list':cus_name_list}
    return render(request,'First_App/Banks_state.html',context=name_dict)

def form_name_view(request):
    form=Form_Name()
    if request.method == 'POST':
        form=Form_Name(request.POST)
        if form.is_valid():
            print('Name: '+form.cleaned_data['name'])
            print('Mail: '+form.cleaned_data['email'])
            print('Date: ',form.cleaned_data['date'])
            print('Text: '+form.cleaned_data['text'])


    return render(request,'First_App/form_output.html',{'form':form})

# def form_of_newForm(request):
#     form=NewForm()
#     if request.method == 'POST':
#         form=NewForm(request.POST)
#         if form.is_valid():
#             form.save(commit=True)
#             return index(request)
#         else:
#             print("ERROR! FORM INVALID.")
#     return render(request,'First_App/signup.html',{'form':form})
