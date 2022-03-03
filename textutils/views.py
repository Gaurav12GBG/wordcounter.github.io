## I have created this file ##
from django.http import HttpResponse
from django.http.request import validate_host
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def index(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        feedback = request.POST['feedback']
        if len(name) < 2 or len(email) < 3 or len(phone) < 10 or len(feedback) < 4:
            messages.error(request, "Please fill the form correctly")
        else:
            userfeedback = UserFeedback(name=name, email=email,
                                        phone=phone, feedback=feedback)
            userfeedback.save()
            messages.success(
                request, "Your feedback has been successfully sent")

    # Show the user feedback
    userfeedback = UserFeedback.objects.all().order_by('-sno')
    context = {'userfeedbacks': userfeedback}

    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')

@login_required
def analyze(request):
    if request.method == "POST":
        text = request.POST['text']
        login_user = User.objects.get(id=request.user.id)
        user = login_user
        
        texthistory = TextContentHistory(text=text, user=user)
        texthistory.save()
        messages.success(request, "TextContent Saved Successfully!")
            
    return render(request, 'index.html')


@login_required
def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        Issue = request.POST['content']
        if len(name) < 2 or len(email) < 3 or len(phone) < 10 or len(Issue) < 4:
            messages.warning(request, "Please fill the form correctly")
        else:
            contact = Contact(name=name, email=email,
                              phone=phone, Issue=Issue)
            contact.save()
            messages.success(
                request, "Your message has been successfully sent")

    return render(request, 'contact.html')


def profile(request):
    if request.user.is_authenticated:
        return render(request, "profile.html")

    return HttpResponse("404 - Not Found")


def edit_profile(request):
    if request.method == "POST":
        un = request.POST['username']
        fn = request.POST['fname']
        ln = request.POST['lname']
        em = request.POST['email']

        user = User.objects.get(id=request.user.id)
        user.username = un
        user.first_name = fn
        user.last_name = ln
        user.email = em

        user.save()
        messages.success(
            request, f"{request.user} is updated his Profile successfully!!!")
        return redirect("profile")

    return render(request, "profile.html")


def signup1(request):
    if request.method == 'POST':
        username = request.POST['uname']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # checks for errorneous
        # username should be under 10 characters
        if len(username) > 10:
            messages.error(
                request, 'Username must be under 10 characters')
            return redirect("signup1")

        # user should be alphanumeric
        if not username.isalnum():
            messages.error(
                request, 'Username should only contain letters and numbers')
            return redirect("signup1")

        if User.objects.filter(username=username).exists():
            messages.error(
                request, 'Username is already taken, Please try with different !')
            return redirect("signup1")

        if User.objects.filter(email=email).exists():
            messages.error(
                request, 'Email is already taken, Please try with different !')
            return redirect("signup1")

        # passwortds should match
        if pass1 != pass2:
            messages.error(request, 'Password do not match')
            return redirect("signup1")

        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()
        messages.success(
            request, "Youe onlineWORDcounter account has been created successfully! kindly please login..")
        return redirect("login1")

    else:
        return render(request, "signup1.html")


def login1(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, "successfully logged in !")
            return redirect("index")
        else:
            messages.error(request, "Invalid Credentials, Please try again!")
            return redirect("login1")

    return render(request, "login1.html")


def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out !")
    return redirect("index")


@login_required
def viewHistory(request):
    texthistory = TextContentHistory.objects.filter(user=request.user.id)
    context = {"texthistories" : texthistory}

    return render(request, "viewHistory.html", context)

def update_content(request, id):
    edittext = TextContentHistory.objects.get(id=id)
    delEdittext = edittext
    delEdittext.delete()
    return render(request, "update_content.html", {'edittext': edittext})
    

def delete_content(request, id):
    deletetext = TextContentHistory.objects.get(id=id)
    deletetext.delete()
    texthistory = TextContentHistory.objects.filter(user=request.user.id)
    
    return render(request, "viewHistory.html", {'texthistories': texthistory})
    
def change_password(request):
    if request.method=="POST":
        current = request.POST["cpwd"]
        new_pas = request.POST["npwd"]
        
        user = User.objects.get(id=request.user.id)
        un = user.username
        check = user.check_password(current)
        
        if check==True:
            user.set_password(new_pas)
            user.save()
            messages.success(request, "Password Changed Successfully!!!")

            user = User.objects.get(username=un)
            login(request,user)
            return redirect("login1")
        else:
            messages.error(request, "Incorrect Current password")

    return render(request, "change_password.html")
