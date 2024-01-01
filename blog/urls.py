from django.urls import include, path
from . import views

urlpatterns = [
	path("", views.IndexView.as_view(), name="index"),
	path("blogger/", views.BloggersView.as_view(), name="bloggers"),
	path("blogger/<int:pk>", views.BloggerView.as_view(), name="blogger"),
	path("<int:pk>", views.BlogView.as_view(), name="blog")
]
