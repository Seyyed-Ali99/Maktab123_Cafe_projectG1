from django.shortcuts import render, redirect,reverse
from .models import Customers
from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Message
from django.views.generic import View
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def home_view(request):
    return render(request, 'home.html',context=None)

def about_view(request):
    return render(request,'aboutus.html')

def register_user_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_repeat = request.POST.get('password_repeat')
        phone = request.POST.get('phone_number')

        # Check if a user with the provided username already exists
        if not password == password_repeat:
            return HttpResponse("Your password and Repeated One is not equal")

        user = Customers.objects.filter(username=username)

        if user.exists():
            # Display an information message if the username is taken
            return HttpResponse("Username already taken!")

        # Create a new User object with the provided information
        Customers.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            phone_number=phone,
        )

        # Redirect to login page
        return redirect('login')

        # Render the registration page template (GET request)
    return render(request, 'register.html')


# Define a view function for the login page
def login_user_view(request):
    # Check if the HTTP request method is POST (form submission)
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if a user with the provided username exists
        if not Customers.objects.filter(username=username).exists():
            # Display an error message if the username does not exist
            messages.error(request, 'Invalid Credentials')
            return redirect('/login/')

        # Authenticate the user with the provided username and password
        user = authenticate(username=username, password=password)

        if user is None:
            # Display an error message if authentication fails (invalid password)
            messages.error(request, "Invalid Credentials")
            return redirect('/login/')
            # Log in the user and redirect to the home page upon successful login

        login(request, user)

        # Redirect based on role
        if user.role == 'admin':
            return redirect("admin-dashboard")  # Change to actual admin dashboard URL name
        else:
            return redirect("home")  # Change to actual customer page URL name

    return render(request, 'login.html')

class LogOutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')
def dashboard_view(request):
    return render(request,'dashboard/dashboard.html')









# user profile
@login_required
def profile(request):
    user = request.user

    if request.method == 'POST':
        user.first_name = request.POST.get('first_name', user.first_name)
        user.last_name = request.POST.get('last_name', user.last_name)
        user.phone_number = request.POST.get('phone_number', user.phone_number)
        user.birth_date = request.POST.get('birth_date', user.birth_date)
        user.save()
        messages.success(request, 'Profile updated successfully!')

    return render(request, 'profile.html', {'user': user})


# send message


@login_required
def send_message(request):
    if request.method == 'POST':
        description = request.POST.get('description')

        # Create a new message instance
        message = Message(description=description, user=request.user)
        message.save()
        messages.success(request, 'Message sent successfully!')
        return redirect('profile')  # Redirect to profile or wherever desired

    return render(request, 'send_message.html')


# view message
@login_required
def view_messages(request):
    messages = Message.objects.filter(user=request.user)  # Get messages for the logged-in user
    return render(request, 'view_messages.html', {'messages': messages})


# logout


