from django.shortcuts import render,get_object_or_404 ,redirect
from django.db.models import F
from django.http import Http404,HttpResponse, HttpResponseRedirect
from .models import Question
from django.urls import reverse
from django.views import generic
import datetime 
from django.utils import timezone
from .forms import QuestionForm ,RegisterUserForm ,ChangePasswordForm
from django.contrib.auth import authenticate ,login ,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def question(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:]
    form = QuestionForm
    submitted = True
    if request.method == "POST":
        form = QuestionForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('?submitted=True')
    else:
        form=QuestionForm
        if 'submitted' in request.GET:  
            submitted = True
    context ={"latest_question_list":latest_question_list,"form":form,"submitted":submitted}
    return render(request ,"authencation/question.html",context)


def login_user(request):
    if request.method =="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('members:question')
        else:
            messages.success(request ,("There was an Error logging In,Try Again..."))
            # Return an 'invalid login' error message.
            return redirect('members:login_user')
    else:
        return render(request,"authencation/login.html")

def logout_user(request):
    logout(request)
    messages.success(request ,("You were Logout."))
    return redirect('members:login_user')

def register_user(request):
    if request.method =="POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username , password=password)
            login(request,user)
            messages.success(request,("Registration Successful!"))
            return redirect('members:login_user')
    else:
            form = RegisterUserForm()
    return render(request,'authencation/register_user.html',{'form':form})

def update_password(request):
     
    if request.user.is_authenticated:
        current_user = request.user
        if request.method == 'POST':
            form =ChangePasswordForm(current_user,request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,"Your Password Has Been Updated.")
                login(request,current_user)
                return redirect('members:question')
            else:
                messages.success(request,"Your Password cannot Changed .Because not in Condition. ")
        else:
            form = ChangePasswordForm(current_user)
    else:
        messages.success(request, "You Must Be Logged In Here.")
    return render(request,"authencation/update_password.html",{'form':form})

def search_question(request):
    if request.method =="POST":
        searched = request.POST['searched']
        questions = Question.objects.filter(question_text__contains=searched)
        return render(request,"authencation/search_question.html",{'searched':searched,'questions':questions})
    else:

        return render(request,"authencation/search_question.html",{})