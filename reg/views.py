from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

from .models import Subject, Student, Apply
# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    else:
        return render(request, "reg/index.html", {
        # "flights": Flight.objects.all()
    })
    

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'reg/login.html', {
                'message': 'Invalid credentials.'
            })
    return render(request, 'reg/login.html')

def logout_view(request):
    logout(request)
    return render(request, 'reg/login.html', {
        'message': 'Logged out'
    })

def search(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    else:
        search_id_sj = ""
        if request.method == "POST":
            search_id_sj = request.POST['search_id_sj']
        return render(request, "reg/search.html", {
            # "student": Student.objects.get(pk=request.user),
            "subjects": Subject.objects.all(),
            "search_id_sj": search_id_sj,
        })

def student(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    else:
        search_username = ""
        if request.method == "POST":
            search_username = request.POST['search_username']
        return render(request, "reg/student.html", {

            "students": Student.objects.all(),
            "search_username": search_username,
        })


def checkStu(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    else:
        if request.method == "POST":
            subject = Subject.objects.get(pk = request.POST['subject'])
            print(subject)
            list_students = subject.sjApply.all() 
        return render(request, "reg/checkStu.html", {
            "students": Student.objects.all(),
            "subject": subject,
            "list_students" : list_students,
        })

def checkSub(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    else:
        if request.method == "POST":
            student = Student.objects.get(pk = request.POST['student'])
            list_subjects = student.stuApply.all()
        return render(request, "reg/checkSub.html", {
            "subject": Subject.objects.all(),
            "student": student,
            "list_subjects": list_subjects
        })