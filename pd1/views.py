from django.shortcuts import render, HttpResponse, redirect
from .models import Jobs,User,Apply,Userjob,Account
from django.core.files.storage import default_storage
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
import smtplib
import requests
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password, check_password


def first(request):
    return HttpResponse('hello world')

def index(request):
    context = {
        "variable": "3456"
    }
    return render(request, 'index.html', context)

def jobseeker(request):
    if request.method=='POST':
        company_name = request.session.get("company_name", 'Guest')
        email=request.POST.get("email")
        name=request.POST.get("name")
        city=request.POST.get("city")
        role=request.POST.get("role")
        resume = request.FILES.get("resume")
        
        Apply.objects.create(company_name=company_name,name=name,email=email,city=city,role=role,resume=resume)
        send_confirmation_email(email, role)
        return redirect('jobpage')

    return render(request, 'jobseeker.html')

def create_account(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if Account.objects.filter(email=email).exists():
            messages.error(request, "Account already exists")
            return redirect('create_account')

        if len(password) < 6:
            messages.error(request, "Password should have more than 6 characters")
            return redirect('create_account')

        # Create user with hashed password
        Account.objects.create(username=username, email=email, password=make_password(password))
        messages.success(request, "Account created! Please log in.")
        return redirect('login')   # Redirect to login page after signup

    return render(request, 'create_account.html')



def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')


        account = Account.objects.filter(email=email).first()

        if account :
            if check_password(password, account.password): # Ensure password verification
                User.objects.create(email=email, password=password)
                request.session['email'] = email
                print('i am here')  # Debugging line
                return redirect('jobpage')  # Redirect after successful login
            else:
                messages.error(request, "Invalid email or password")
                return redirect('login')
        else:
            messages.error(request, "Account does not exist. Please create an account.")
            return redirect('create_account')


    return render(request, 'login.html')


def applyed(request):
    if request.method == 'GET':
        email = request.session.get('email')
        if not email:
            print('No email_id')
            return render(request, 'applyed.html', {'jobs': []})

        apps = Apply.objects.filter(email=email)

        if not apps.exists():
            print('Not applied to any job yet')
            return render(request, 'applyed.html', {'jobs': []})  
        
        jobs = []
        for app in apps:
            print(f"Searching jobs for: {app.company_name}, {app.role}")  
            job = Jobs.objects.filter(company_name__icontains=app.company_name, job_role__icontains=app.role)
            print(f"Found Jobs: {list(job)}")  
            jobs.extend(job)  

        return render(request, 'applyed.html', {'jobs': jobs})
    
    return render(request, 'applyed.html', {'jobs': []})


def joblogin(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        Userjob.objects.create(email=email,password=password)
        
        request.session['email'] = email
        return redirect('jobprovider')
    return render(request,'joblogin.html')


from .models import Jobs

def jobprovider(request):
    if request.method == 'POST':
        company_name = request.POST.get('company_name')
        job_role = request.POST.get('job_role')
        salary = request.POST.get('salary')
        description = request.POST.get('description')
        email = request.POST.get('email')
        Jobs.objects.create(company_name=company_name,email=email,job_role=job_role, salary=salary, description=description)
        
    return render(request, 'jobprovider.html')

def notification(request):
    if request.method == 'GET':
        email = request.session.get("email")  
        print("Session Email:", email)  

        apps = []  

        if email:
            jobs = Jobs.objects.filter(email=email)  
            
            if jobs.exists(): 
                company_names = jobs.values_list('company_name', flat=True) 
                print("Company Names Found:", list(company_names)) 

                apps = Apply.objects.filter(company_name__in=company_names)  
               

                if not apps:
                    print("No applications found for these companies.")

            else:
                print("No job found for this email.")

        return render(request, 'notification.html', {'apps': apps})


def send_confirmation_email(jobseeker_email, job_title):
    subject = "Job Application Submitted Successfully"
    message = f"Dear Job Seeker,\n\nYou have successfully applied for the position '{job_title}'. We will notify you about updates.\n\nBest Regards,\nJob Portal Team"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [jobseeker_email]

    send_mail(subject, message, email_from, recipient_list)

def manage(request):
    if request.method=='GET':
        email = request.session.get("email")
        print(email)
        apps=Jobs.objects.filter(email=email)
        
        if apps:
            print(apps)
            return render(request, 'manage.html', {'apps': apps})  # Pass apps to the template
        else:
            return render(request, 'manage.html', {'message': "No jobs posted yet"})
    if request.method == 'POST':
        job_role = request.POST.get('job_role')  # Corrected from GET to POST

        if job_role:
            deleted_count, _ = Jobs.objects.filter(email=request.session.get("email"), job_role=job_role).delete()  
            if deleted_count > 0:
                print(f"Deleted {deleted_count} job(s) with role: {job_role}")
            else:
                print("No matching jobs found to delete.")

    return redirect('manage') 
    

def jobpage(request):
    query=request.GET.get('search','')
    if query:
        all_jobs=Jobs.objects.filter(job_role__icontains=query)
    else:
        all_jobs = Jobs.objects.all()

    if request.method=='POST':
        company_name=request.POST.get('company_name')
        request.session['company_name'] = company_name
        return redirect('jobseeker')


    return render(request, 'job_page.html', {'jobs': all_jobs ,'query':query})
def succesful(request):
    return render(request,'succesful.html')

import smtplib





