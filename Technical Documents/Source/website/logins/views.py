import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.template import loader
from django.template.loader import get_template
from django.urls import reverse
from logins.models import Player
from django import forms
from django.contrib.auth import logout
from django.template.loader import get_template
from django.shortcuts import redirect
from leaderboard.models import Leaderboard


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)

def index(request):
    return render(request, 'logins/index.html')

def user_login(request):
    # Initialize error message
    error_message = ''
    # If HTTP request method is POST
    if request.method == 'POST':
        # Initialize form object with POST data
        form = AuthenticationForm(data=request.POST)
        # If form is valid
        if form.is_valid():
            # Get cleaned data from form
            # data = form.cleaned_data
            # Authenticate user with provided credentials
            user = form.get_user()
            # If user is authenticated
            if user is not None:
                # Log in user
                login(request, user)
                # Redirect user to home page
                return HttpResponseRedirect(reverse('home'))
        # If form is not valid
        else:
            # Reinitialize form with POST data
            form = AuthenticationForm(request.POST)
            # Set error message
            error_message = 'Invalid username or password'
    # If HTTP request method is not POST
    else:
        # Initialize form object
        form = AuthenticationForm()
    # Load login template
    template = loader.get_template('logins/login.html')
    # Render template with form and error message
    return HttpResponse(template.render({'form': form.as_p(), 'error_message': error_message}, request))


def register(request):
    # Initialize error message
    error_message = ''
    # If HTTP request method is POST
    if request.method == 'POST':
        # Initialize form object with POST data
        form = CustomUserCreationForm(request.POST)
        # If form is valid
        if form.is_valid():
            # Get cleaned data from form
            data = form.cleaned_data
            # Extract username, email and password from data
            username = data.get('username')
            email = data.get('email')
            password = data.get('password1')
            # If user with given username doesn't already exist
            if not User.objects.filter(username=username).exists():
                # Create new user
                user = User.objects.create_user(username=username, email=email, password=password)
                # Create new player profile
                player = Player(user=user)
                # Save the Player object
                player.save()
                # Create new leaderboard instance for the player
                Leaderboard.objects.create(player=user)
                # Authenticate and log in user
                user = authenticate(request, username=username, password=password)
                login(request, user)
                # Redirect user to account page
                return HttpResponseRedirect(reverse('home'))
            # If user with given username already exists
            else:
                error_message = 'A user with that username already exists'
        # If form is not valid
        else:
            # If username already exists
            if form.has_error('username', code='unique'):
                error_message = 'This username is already taken. Please choose another one.'
            # If password fields do not match
            elif form.has_error('password1', code='password_mismatch'):
                error_message = 'The two password fields did not match. Please try again.'
            # If password is too short
            elif form.has_error('password1', code='min_length'):
                error_message = 'The password is too short. Please enter a password with at least 8 characters.'
            # If other validation errors occur
            else:
                try:
                    form.full_clean()
                except ValidationError as e:
                    error_message = e.message
    # If HTTP request method is not POST
    else:
        # Initialize form object
        form = CustomUserCreationForm()

    # Render register template
    return render(request, 'logins/register.html', {'form': form, 'error_message': error_message})
