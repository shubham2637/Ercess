from django.shortcuts import render
from django.urls import reverse
from .forms import userForm
from .models import user
# Create your views here.
from django.core.mail import send_mail
def index(request):
    use = userForm()
    context ={'form' : use}
    return render(request, "accounts/index.html",context)


def signup(request):
    if form.is_valid():
        Name = form.cleaned_data['name']
        Email = form.cleaned_data['email']
        Password = form.cleaned_data['password1']
        context={'form' : 'form'}
        #cc_myself = form.cleaned_data['cc_myself']
        U = user(name=Name,email=Email,password=Password)
        #recipients = ['vishaljaiswal.info@gmail.com']
        recipients=['shubham37@outlook.com']
        if cc_myself:
            recipients.append(sender)

        send_mail(subject, context, sender, recipients)
        return render(request, "accounts/signupsuccess.html",context)
    #return render(request, "accounts/")
def signupsuccess(request):
    users = {}
    return render(request, "accounts/signupsuccess.html",context)
