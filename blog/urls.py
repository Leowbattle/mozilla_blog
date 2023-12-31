from django.urls import include, path
from . import views

urlpatterns = [
	path("", views.index, name="index"),
	path("blogger/", views.bloggers, name="bloggers"),
	path("blogger/<int:id>", views.blogger, name="blogger"),
	path("<int:pk>", views.BlogView.as_view(), name="blog"),
]
