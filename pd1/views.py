from django.shortcuts import render, HttpResponse, redirect
from .models import Jobs,User,Apply,Userjob
from django.core.files.storage import default_storage
from django.core.mail import send_mail
from django.conf import settings

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


def login(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        User.objects.create(email=email,password=password)
        return redirect('jobpage')

    return render(request,'login.html')
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




def apply_for_job(request, company_name):
    job = Jobs.objects.get(id=company_name)  
    jobseeker_email = request.user.email  
    send_confirmation_email(jobseeker_email, job.title)

    return redirect('jobs_page')  


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

