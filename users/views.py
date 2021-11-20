from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.shortcuts import render, redirect, reverse
from .forms import RegistrationForm, LoginForm


# Login Functionality
def login(request):
    # if the user is currently logged in direct them to the home page
    if request.user.is_authenticated:
        messages.info(request, "You are currently logged in")
        return redirect(reverse('home'))
    else:
        form = LoginForm()
        # If the form has just been submitted
        if request.method == "POST":
            form = LoginForm(request.POST)
            try:
                if form.is_valid:
                    user = auth.authenticate(email=request.POST['email'], password=request.POST['password'])
                    # check if a user exists in the database matching the email address and password provided
                    if user:
                        auth.login(user=user, request=request)
                        messages.info(request, "You are now logged in!")
                        return redirect(reverse('home'))
                    else:
                        messages.info(request, "Login failed")
                        return render(request, 'login.html', {'form': form})
            except Exception as e:
                print(e)
                messages.info(request, "An error occurred logging in")
                return render(request, 'login.html', {'form': form})
        # If the user isn't logged in, display the login page
        try:
            form = LoginForm()
            return render(request, 'login.html', {'form': form})
        except:
            messages.info(request, "Error encountered loading the login page")
            return redirect(reverse('home'))

    
    
# Function to display the registration form    
def register(request):
    # Make sure the user is not currently logged in
    if not request.user.is_authenticated:
        # if the request is a post mapping, retrieve the submited forms details
        if request.method == "POST":
            form = RegistrationForm(request.POST)
            # make sure the form is validated before saving it
            if form.is_valid():
                form.save()
                # retrieve the submitted forms values for email and password
                email = form.cleaned_data.get('email')
                password = form.cleaned_data.get('password1')
                user_account = auth.authenticate(email=email, password=password)
                
                
                
            
            
        else:
            # If the request is a get mapping display, the registration form
            form = RegistrationForm()
            return render(request, 'register.html', {'form': form})
    else :
        # If the user is already logged in, redirect them to the home page
        messages.info(request, "Logged in users cannot access the Registration Form")
        return redirect(reverse('home'))
    
# Function that allows user to log out
@login_required
def logout(request):
    #Log the user out
    auth.logout(request)
    messages.info(request, "Logout Successful")
    return redirect(reverse('home'))