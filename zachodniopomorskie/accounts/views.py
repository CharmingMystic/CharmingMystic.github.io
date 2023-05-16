from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as lgout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm

def login(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('home.html')
		else:
			messages.success(request, ("There Was An Error Logging In, Try Again..."))	
			return redirect('login.html')
	else:
		return render(request, 'login.html', {})

def logout(request):
	lgout(request)
	messages.success(request, ("You Were Logged Out!"))
	return redirect('home')

def profile(request):
    return render(request, 'profile.html', {})

def register(request):
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, ("Registration Successful!"))
			return redirect('home')
	else:
		form = RegisterForm()

	return render(request, 'register.html', {
		'form':form,
		})