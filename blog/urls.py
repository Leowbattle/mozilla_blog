from django.urls import include, path
from . import views

urlpatterns = [
	path("", views.index, name="index"),
	path("blogs/", views.blogs),
	path("blogger/<int:id>", views.blogger),
	path("<int:id>", views.blog),
	path("<int:id>/create", views.create_comment),
	path("bloggers/", views.bloggers),
]
