from django.shortcuts import render,redirect
from .models import Userdata,Doctorinfo,Appointmentinfo
from django.contrib import messages

def index(request):
    return render(request,'index.html')


def signup(request,method=['GET','POST']):
    if request.method=="POST":
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')

        user=Userdata.objects.filter(email=email)
        if user.exists():
            messages.info(request,"user already exist")
        elif password1 != password2:
            messages.info(request,"password not matched")
        else:
            messages.info(request,"user already exist")
            Userdata.objects.create(email=email,password=password1)
        return render(request,'login.html')
    return render(request,'signup.html')

 
def login(request,method=['GET','POST']):
    if request.method=="POST":
        email=request.POST.get('email')
        password1=request.POST.get('password1')

        user=Userdata.objects.filter(email=email,password=password1)
        if user.exists():
            request.session['email']=email
            return redirect('/main/')
        else:
            messages.info(request,'email and password is incorrect')
            return render(request,'login.html')
    return render(request,'login.html')


def main(request):
    email = request.session['email']
    print(email)
    doctors = Doctorinfo.objects.all()
    return render(request,'main.html',{'doctors':doctors,'email':email})

def appointment(request):
    if request.method=="POST":
        email = request.session['email']
        user=Userdata.objects.get(email=email)
        doctor = request.POST.get('doctor')
        doctorobj=Doctorinfo.objects.get(doc_name=doctor)
        patient = request.POST.get('patient')
        email_address= request.POST.get('email')
        contact = request.POST.get('contact')
        date_time = request.POST.get('date_time')
        symptoms = request.POST.get('symptoms')
        Appointmentinfo.objects.create(
            user=user,
            doctor=doctorobj,
            patient_name=patient,
            email=email_address,
            contact=contact,
            date_time=date_time,
            symptoms=symptoms
        )
        return render(request,'success.html')
    return render(request,'appointment.html')

def book(request,id):
    email = request.session['email']
    doctor = Doctorinfo.objects.get(id=id)
    return render(request,'appointment.html',{'email':email,'doctor':doctor})