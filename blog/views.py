from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	return HttpResponse("Blog")

def blogs(request):
	return HttpResponse("Blogs")

def blogger(request, id):
	return HttpResponse(f"Blogger {id}")

def blog(request, id):
	return HttpResponse(f"Blog {id}")

def create_comment(request, id):
	return HttpResponse(f"Create Comment {id}")

def bloggers(request):
	return HttpResponse("Bloggers")
