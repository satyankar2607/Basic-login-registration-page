from django.http import HttpResponse
from django.shortcuts import render
from quiz1.models import contestant, questionbank

x = contestant.objects.raw('SELECT id,email,pwd FROM quiz1_contestant')
emails = []
passwords = []
for i in x:
    emails.append(i.email)
    passwords.append(i.pwd)


def index(request):
    return render(request, 'index.html')


def signup(request):
    email = request.POST.get('email')
    password = request.POST.get('pwd')
    if email not in emails:
        savingdata = contestant(email=email, pwd=password)
        savingdata.save()
        return HttpResponse("Registered")
    else:
        return HttpResponse("Already Exist!!")


def login(request):
    return render(request, 'login.html')


def logch(request):
    email = request.POST.get('email')
    password = request.POST.get('pwd')

    if email not in emails:
        return HttpResponse("Wrong Credentials!!")
    else:
        if password not in passwords:
            return HttpResponse("Wrong Credentials!!")
        else:
            return render(request, 'participant_admin.html')


def adm(request):
    return render(request, 'adm.html')


def add(request):
    question = request.POST.get('question')
    opt1 = request.POST.get('opt1')
    opt2 = request.POST.get('opt2')
    opt3 = request.POST.get('opt3')
    opt4 = request.POST.get('opt4')
    corr_opt = request.POST.get('corr_opt')
    Savingdata = questionbank(questions=question, opt1=opt1, opt2=opt2, opt3=opt3, opt4=opt4, corr_opt=corr_opt)
    Savingdata.save()
    return HttpResponse("Question added!")

def showquestions(request):
    r=questionbank.objects.all()
    content={"message":r}
    return render(request,"showquestions.html",content)

def dele(request):
    question = request.POST.get('question')
    questionbank.objects.filter(questions = question).delete()
    return HttpResponse("Question deleted!")

def user(request):
    q = questionbank.objects.all()
    content = {"message": q}
    return render(request,'user.html',content)


def calc(request):
    i = questionbank.objects.all()
    for j in i:
        ans = request.POST.get(j.questions)
        print()
    return HttpResponse("helknzlk")



