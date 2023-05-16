from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

def home(response):
	return render(response, "home.html", {})

def map(response):
	return render(response, "map.html", {})

def about(response):
	return render(response, "about.html", {})

def contact(response):
	return render(response, "contact.html", {})