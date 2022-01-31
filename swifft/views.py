from django.shortcuts import redirect, render
from django.template import context
from .models import contactus
from django.core.mail import send_mail
from django.contrib.auth.models import User
import random
from django.core.mail import EmailMessage
from itmaster.settings import EMAIL_HOST_USER
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
import string
from .forms import contactus_form


def home(request):
    return render(request,'index.html')


def contact(request):
    form = contactus_form()
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        details = request.POST.get('message')
        phone = request.POST.get('phone')
        if contactus.objects.filter(Email = email).exists():
            message = messages.warning(request , email + " " + 'is already used')
            return HttpResponseRedirect('/home' , messages) 
        else:    
            # fm = form.cleaned_data
            contactus(Username=username,Email=email,Subject=subject,Details=details,Phone_no=phone).save()
            # print(fm)
            N = 7
            res = ''.join(random.choices(string.ascii_uppercase + string.digits, k = N))
            # print("The generated random string : " + str(res))
            message = "Your Query has been sucesfully send with "+ email + " and We are trying our best to connect with you as soon as possible" 
            subject = ' Query form'
            # user create 
            # User.objects.create_user(email)
            send_mail(subject, message, EMAIL_HOST_USER, [email], fail_silently = False)
            message = "New connection came with  "+ email 
            subject = 'Query form no. '+res

            send_mail(subject, message, EMAIL_HOST_USER, [EMAIL_HOST_USER], fail_silently = False)
            return HttpResponseRedirect('home')

    else:
        form = contactus_form(request.POST)        
    context = {'form' : form }
    return render(request,'contact.html',context) 
# Create your views here.
