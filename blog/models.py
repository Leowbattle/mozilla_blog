from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	bio = models.TextField()

	def __str__(self):
		return self.user.username
	
	def get_all_blogs(self):
		return Blog.objects.filter(author=self.user.pk)

class Blog(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	time = models.DateTimeField()
	title = models.CharField(max_length=200)
	content = models.TextField()

	def __str__(self):
		return self.title

	def get_all_comments(self):
		return Comment.objects.filter(blog=self.pk)

class Comment(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
	time = models.DateTimeField()
	content = models.TextField()
