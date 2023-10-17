from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth import authenticate, login
from .models import Department,Course,UserProfile
from django.http import JsonResponse



# Create your views here.

def home(request):
    return render(request,'home.html')

def loginn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('page')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username taken")
                return redirect('register')
            else:
                myuser = User.objects.create_user(username=username, password=password)
                myuser.save()
            messages.success(request, "Registration successful. You can now login.")
            return redirect('login')

        else:
            messages.info(request, "Passwords do not match")
            return redirect("register")

    return render(request, 'register.html')

def department(request):
    department=Department.objects.all()
    return render(request,'home.html',{'depart':department})


def user_dashboard(request):
    departments = Department.objects.all()
    courses = Course.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name', '')
        dob = request.POST.get('dob', '')
        age = request.POST.get('age', '')
        gender = request.POST.get('gender', '')
        phone_number = request.POST.get('phone_number', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        department_id = request.POST.get('department', '')
        course_id = request.POST.get('course', '')
        purpose = request.POST.get('purpose', '')

        if not name or not dob or not age or not gender or not phone_number or not email or not address or not department_id or not course_id or not purpose:
            # Handle missing form data, redirect, or display an error message
            return render(request, 'new.html', {'departments': departments, 'courses': courses, 'error_message': 'Please fill in all required fields'})

        try:
            department_id = int(department_id)
        except ValueError:

            return render(request, 'new.html', {'departments': departments, 'courses': courses, 'error_message': 'Invalid department selection'})

        try:
            course_id = int(course_id)
        except ValueError:

            return render(request, 'new.html', {'departments': departments, 'courses': courses, 'error_message': 'Invalid course selection'})


        department = get_object_or_404(Department, id=department_id)
        course = get_object_or_404(Course, id=course_id)

        detail = UserProfile(
            name=name,
            dob=dob,
            age=age,
            gender=gender,
            phone_number=phone_number,
            email=email,
            address=address,
            department=department,
            course=course,
            purpose=purpose
        )
        detail.save()

        return render(request, 'new.html', {'message': 'Order Confirmed'})

    return render(request, 'new.html', {'departments': departments, 'courses': courses})


 # Import JsonResponse

# Your existing views

def get_courses(request):
    department_id = request.GET.get('department_id')
    courses = Course.objects.filter(department_id=department_id)
    course_options = "<option value='' disabled selected>Select Course</option>"

    for course in courses:
        course_options += f"<option value='{course.id}'>{course.name}</option>"

    data = {'course_options': course_options}
    return JsonResponse(data)

def page(request):
    return render(request,'page.html')




