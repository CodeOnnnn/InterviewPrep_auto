from django.shortcuts import render,redirect, HttpResponse
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from .models import Question, Response
from .forms import Registeruserform, LoginForm, NewResponseForm
# from prep import views
# from prep.views import sc_save
def registerPage(request):
    form= Registeruserform()
    if request.method == 'POST':
        try:
            form=Registeruserform(request.POST)
            if form.is_valid():
                user= form.save()
                login(request,user)
                return redirect('index')
        except Exception as e:
            print(e)
            raise

    context={
        'form':form
    }
    return render(request,'register.html',context)

def loginPage(request):
    form = LoginForm()
    if request.method == 'POST':
        try:
            form=LoginForm(data=request.POST)
            if form.is_valid():
                user= form.get_user()
                login(request,user)
                return redirect('index')
        except Exception as e:
            print(e)
            raise
    context={
        'form':form
    }
    return render(request,'login.html',context)

@login_required(login_url='register')
def logoutPage(request):
    logout(request)
    return redirect('login')

def homePage(request):
    
    questions= Question.objects.all().order_by('-created_at')
    context={
        'questions':questions
    }
    return render(request,'index.html',context)

def questionPage(request, id):
    question= Question.objects.get(id=id)
    # question.max_score= sc_save()
    sent=question.body
    sent1=' '.join(set(sent.split()))
    questionPage.database=sent1.split()


    context = {'question':question,"page_title": "Record audio"}
    return render(request,'question.html',context)

def questionid():
    y=questionPage.database

    return y
def score(request):

    questions= Question.objects.all().order_by('-created_at')
    context={
        'questions':questions
    }
    return render(request,'scores.html',context)
