from django.http import HttpResponse
import datetime
from django.shortcuts import render
import datetime

def home(request):
    IsActive=True
    if request.method=='POST':
        check=request.POST.get('check')
        print(check)
        if check is None: IsActive=False
        else: IsActive=True


    

    date=datetime.datetime.now()
    name='Wasim'
    list_of_programs=[
        'WAP to check odd or even',
        'WAP to check prime no',
        'WAP to print all prime numbers',
        'WAP to print pascals triangle'
        
    ]
    student={
        'student_name':'Wasim',
        'student_college':'MBD',
        'student_city':'dbg'
    }
    data={
        'date':date,
        'IsActive':IsActive,
        'name':name,
        'student_data':student,
        'list_of_programs':list_of_programs
    }

    return render(request,"home.html",data)



def about(request):
    # return HttpResponse("<h1>This is About page</h1>")
    return render(request,"about.html",{})

def services(request):
    # return HttpResponse("<h1>This is services page</h1>")
    return render(request,"services.html",{'form':form})
    




    