from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.detail import DetailView

from .models import Profile, Blog, Comment

def index(request):
	blogs = Blog.objects.all().order_by("-time")#[:5]
	context = { "blogs": blogs }
	return render(request, "blog/index.html", context)

def bloggers(request):
	bloggers = Profile.objects.all()
	context = { "bloggers": bloggers }
	return render(request, "blog/bloggers.html", context)

def blogger(request, id):
	context = { "id": id }
	return render(request, "blog/blogger.html", context)

class BlogView(DetailView):
	model = Blog

# def blog(request, id):
# 	blog = Blog.objects.get(pk=id)
# 	context = { "blog": blog }
# 	return render(request, "blog/blog.html", context)
