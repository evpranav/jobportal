from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.http import HttpResponse
from django.contrib.auth import authenticate
from jobportal.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
import uuid
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'index.html')


def regis(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(username=username).first():
            messages.success(request, 'username already taken')
            return redirect(regis)
        if User.objects.filter(email=email).first():
            messages.success(request, 'email already taken')
            return redirect(regis)
        user_obj = User(username=username, email=email)
        user_obj.set_password(password)
        user_obj.save()
        auth_token = str(uuid.uuid4())
        profile_obj = profiles.objects.create(user=user_obj, auth_token=auth_token)
        profile_obj.save()
        send_mail_regis(email, auth_token)
        return redirect(success)
    return render(request, 'registration.html')


def send_mail_regis(email, token):
    subject = "your account has been verified"
    message = f'paste the link to verify your account http://127.0.0.1:8000/jobapp/verify/{token}'
    email_from = EMAIL_HOST_USER
    recipient = [email]
    send_mail(subject, message, email_from, recipient)


def success(request):
    return render(request, 'success.html')


def verify(request, auth_token):
    profile_obj = profiles.objects.filter(auth_token=auth_token).first()
    if profile_obj:
        if profile_obj.is_verified:
            messages.success(request, 'your account is already verified')
            return redirect(login)
        profile_obj.is_verified = True
        profile_obj.save()
        messages.success(request, 'your account has been verified')
        return redirect(login)
    else:
        return redirect(error)


def error(request):
    return render(request, 'error.html')


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username=username).first()
        if user_obj is None:
            messages.success(request, 'user not found')
            return redirect(login)
        profile_obj = profiles.objects.filter(user=user_obj).first()
        if not profile_obj.is_verified:
            messages.success(request, 'profile not verified. check your mail')
            return redirect(login)
        user = authenticate(username=username, password=password)
        if user is None:
            messages.success(request, 'wrong password or username')
            return redirect(login)
        obj = profiles.objects.filter(user=user)
        return render(request, 'profile.html', {'obj': obj})
    return render(request, 'login.html')


def postjob(request):
    return render(request, 'postjob.html')


def profile(request):
    return render(request, 'profile.html')


def profile1post(request):
    if request.method == 'POST':
        a = postjobform(request.POST)
        if a.is_valid():
            un = a.cleaned_data['username']
            em = a.cleaned_data['email']
            jt = a.cleaned_data['jobtitle']
            wt = a.cleaned_data['worktype']
            er = a.cleaned_data['experiencerequired']
            jy = a.cleaned_data['jobtype']
            b = profilepost(username=un, email=em, jobtitle=jt, worktype=wt, experiencerequired=er, jobtype=jy)
            b.save()
            return HttpResponse("job post successfully")
        else:
            return HttpResponse("error")
    return render(request, 'postjob.html')


def table(request):
    # pro=profiles.objects.all()
    us = User.objects.all()
    id = []
    li = []
    email = []
    for i in us:
        id1 = i.id
        id.append(id1)
        nm = i.username
        em = i.email
        li.append(nm)
        email.append(em)
    li1 = li[1:]
    em1 = email[1:]
    id = id[1:]
    mylist = zip(li1, em1, id)
    return render(request, 'company.html', {'mylist': mylist})


# def send(request,id):
#     a=User.objects.get(id=id)
#     li = []
#     email = []
#     id=[]
#     for i in a:
#         id1=i.id
#         id.append(id1)
#         nm = i.username
#         em = i.email
#         li.append(nm)
#         email.append(em)
#     return render(request,'send_mail.html',{'mylist':mylist})

#


def mailsend(request, id):
    a = User.objects.get(id=id)
    u = a.username
    b = a.email
    print(u)
    print(b)
    return render(request, 'send_mail.html', {'u': u, 'b': b})


def user_register(request):
    if request.method == 'POST':
        a = regform(request.POST)
        if a.is_valid():
            unm = a.cleaned_data['username']
            em = a.cleaned_data['email']
            db = a.cleaned_data['dob']
            qf = a.cleaned_data['qualification']
            ph = a.cleaned_data['phoneno']
            ps = a.cleaned_data['password']
            csps = a.cleaned_data['cspassword']
            if ps == csps:
                b = regmodel(username=unm, email=em, dob=db, qualification=qf, phoneno=ph, password=ps)
                b.save()
                return HttpResponse("registration success")
            else:
                return HttpResponse("password incorrect")
        else:
            return HttpResponse("registration failed")
    return render(request, 'user_registration.html')


def user_login(request):
    if request.method == 'POST':
        a = logform(request.POST)
        if a.is_valid():
            em = a.cleaned_data['email']
            ps = a.cleaned_data['password']
            b = regmodel.objects.all()
            for i in b:
                if em == i.email and ps == i.password:
                    un = i.username
                    em = i.email
                    ph = i.phoneno
                    qf = i.qualification
                    id = i.id
                    return render(request, 'user_profile.html', {'un': un, 'em': em, 'ph': ph, 'qf': qf, 'id': id})
                    # return HttpResponse("login success")
            else:
                return HttpResponse("login failed")
        # e = regmodel.objects.all()
        # return render(request, 'user_profile.html',{'e': e})
    return render(request, 'user_login.html')


# def user_profile(request):
#     return render(request, 'user_profile.html')


#
# def edituser(request):
#     return render(request, 'edituser.html')
#
# def show(request):
#     a = regmodel.objects.all()
#     return render(request, 'user_profile.html', {'employee': a})

def edit(request, id):
    employee = regmodel.objects.get(id=id)
    if request.method == 'POST':
        employee.username = request.POST.get('username')
        employee.email = request.POST.get('email')
        employee.phoneno = request.POST.get('phoneno')
        employee.qualification = request.POST.get('qualification')
        employee.save()
        return redirect(user_login)
    return render(request, 'edituser.html', {'employee': employee})


# def update(request, id):
#     employee = regmodel.objects.get(id=id)
#     form = regform(request.POST, instance=employee)
#     form.save()
# #
# def update(request, id):
#     employee = regmodel.objects.get(id=id)
#     form = regform(request.POST, )
#     form.save()
#     return render(request,'user_profile.html')

#


def viewjob(request, id):
    b1 = regmodel.objects.filter(id=id)
    for i in b1:
        x1 = i.username
        x2 = i.id
    a1 = profilepost.objects.all()
    l1 = []
    l2 = []
    l3 = []
    for i in a1:
        b1=i.jobtitle
        l1.append(b1)
        b2=i.username
        l2.append(b2)
        b3=i.id
        l3.append(b3)
    mylist = zip(l1,l2,l3)
    return render(request, 'viewjob.html', {'mylist': mylist, "x1": x1, "x2": x2})


def view_more(request, id, pk):
    a1 = profilepost.objects.get(id=id)
    b1 = regmodel.objects.get(id=pk)
    return render(request, 'viewmore.html', {'a1': a1, "b1": b1})


def applyjob(request, id, pk):
    a1 = profilepost.objects.get(id=id)
    b1 = regmodel.objects.get(id=pk)
    if request.method == 'POST':
        a = applyjobform1(request.POST, request.FILES)
        if a.is_valid():
            qufn = a.cleaned_data['qualification']
            phno = a.cleaned_data['phone']
            exper = a.cleaned_data['exp']
            resm = a.cleaned_data['resume']
            b = applyjobmodel1(qualification=qufn, phone=phno, exp=exper, resume=resm)
            b.save()
            return HttpResponse(" success")
        else:
            return HttpResponse("failed")
    return render(request, 'applyjob.html', {'a1': a1, 'b1': b1})
