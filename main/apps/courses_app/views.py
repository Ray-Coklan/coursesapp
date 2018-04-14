from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
from ..first_app import *
import bcrypt

def index(request):
    users = User.objects.get(id = request.session['id'])
    courses = Course.objects.all()
    context = {
        "current_user" : users,
        "show_course" : courses,
    }
    return render(request, 'courses_app/index.html', context)

def add_course(request ,id):
    user = User.objects.get(id = request.session['id'])
    Course.objects.create(
        name = request.POST['name'],
        description = request.POST['description'],
        creator = user
    )
    return redirect ('/courses')

def delete(request, id):
    current_user = User.objects.get(id = request.session['id']).id
    user_created = Course.objects.get(id=id).creator.id
    if current_user == user_created:
        x = Course.objects.get(id=id)
        x.delete()
    else:
        print 'You cannot delete this because you didnt make it'
    return redirect('/courses')
    
def join(request, id):
    current_user = User.objects.get(id = request.session['id'])
    join_course = Course.objects.get(id=id)
    join_course.students.add(current_user)
    print 'You have joined the course'
    return redirect('/courses')

def show(request, id):
    show_course = Course.objects.get(id=id)
    show_students = User.objects.filter(id=id)
    context = {
        'class' : show_course,
        'students' : show_students
    }
    return render(request, 'courses_app/show.html', context)

def edit(request,id):
    course = Course.objects.get(id=id)
    context = {
        'course': course
    }
    return render(request, 'courses_app/edit.html',context)

def process_edit(request, id):
    courses = Course.objects.get(id=id)
    courses.name = request.POST['name']
    courses.description = request.POST['description']
    courses.save()
    print "UPDATE"
    return redirect('/courses')    
