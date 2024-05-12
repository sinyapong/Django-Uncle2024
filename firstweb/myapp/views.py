from django.shortcuts import render
from django.http import HttpResponse
from .models import Tracking, AskQa
from django.contrib.auth.decorators import login_required

def Home(request):
    return render(request, 'myapp/home.html')

def about(request):
    return render(request, 'myapp/about.html')

def tracking(request):
    # tracks = {'Ying - TH1234', 'Pupea - TH5678', 'Pang - TH 9123'}
    tracks = Tracking.objects.all()
    return render(request, 'myapp/tracking.html',{'tracks':tracks})

def ask(request):
    if request.method == "POST":
        data = request.POST.copy()
        name = data.get('name')
        email = data.get('email')
        title = data.get('title')
        detail = data.get('detail')

        new = AskQa()
        new.name = name
        new.email = email
        new.title = title
        new.detail = detail
        new.save()

    return render(request, 'myapp/ask.html',{})

@login_required
def questions(request):
    questions = AskQa.objects.all()
    return render(request, 'myapp/question.html',{'questions':questions})


def answer(request, askid):
    record = AskQa.objects.get(id=askid)
    if request.method == "POST":
        data = request.POST.copy()
        detail_answer = data.get('detail_answer')
        record.detail_answer = detail_answer
        record.save()

    return render(request, 'myapp/answer.html',{'record':record})