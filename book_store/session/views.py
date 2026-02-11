from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from .models import Student

# Create your views here.


def student_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            student = Student.objects.get(username=username)
            # Check hashed password
            if check_password(password, student.password):
                request.session['student_id'] = student.id
                request.session['student_name'] = student.name
                return redirect('dashboard')
            else:
                return render(request, 'session/login.html', {
                    'error': 'Invalid username/password'
                })
        except Student.DoesNotExist:
            return render(request, 'session/login.html', {
                'error': 'Invalid username/password'
            })

    return render(request, 'session/login.html')


def dashboard(request):
    if 'student_id' not in request.session:
        return redirect('login')
    
    name= request.session.get('student_name')
    return render(request, 'session/dashboard.html',{
        "name":name
    })


def logout(request):
    request.session.flush()
    return redirect('login')
