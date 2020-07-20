from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user

@unauthenticated_user
def loginPage(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('homepage')
		else:
			messages.info(request, 'Username OR password is incorrect !')

	context = {}
	return render(request, 'accounts/login.html', context)

@login_required(login_url='login')
def homepage(request):
	return render(request,'accounts/home.html')

def logoutUser(request):
	logout(request)
	return redirect('login')

def about(request):
	return render(request,'accounts/about.html')

def profile(request):
	return render(request,'accounts/profile.html')