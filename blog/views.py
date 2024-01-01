from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views import generic
from .models import Profile, Blog, Comment
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

class IndexView(generic.ListView):
	template_name = "blog/index.html"
	context_object_name = "blogs"

	def get_queryset(self):
		return Blog.objects.all().order_by("-time")

class BloggersView(generic.ListView):
	template_name = "blog/bloggers.html"
	context_object_name = "bloggers"

	def get_queryset(self):
		return Profile.objects.all()

class BloggerView(generic.DetailView):
	model = Profile
	context_object_name = "blogger"
	template_name = "blog/blogger.html"

class BlogView(generic.DetailView):
	model = Blog
	context_object_name = "blog"
	template_name = "blog/blog.html"

@login_required
def submit_comment(request, blogid):
	text = request.POST.get("comment-text")
	blog = Blog.objects.get(pk=blogid)
	Comment.objects.create(author=request.user, blog=blog, time=datetime.now(), content=text)
	return redirect(request.GET["next"])
