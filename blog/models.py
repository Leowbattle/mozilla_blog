from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	bio = models.TextField()

	def __str__(self):
		return self.user.username

class Blog(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	time = models.DateTimeField()
	title = models.CharField(max_length=200)
	content = models.TextField()

class Comment(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
	time = models.DateTimeField()
	content = models.TextField()
