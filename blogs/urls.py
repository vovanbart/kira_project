from django.urls import path
from . import views

app_name = "blogs"
urlpatterns = [
    path("", views.index, name="index"),
    path("new/", views.post_create, name="post_create"),
    path("edit/<int:pk>/", views.post_edit, name="post_edit"),
    path("register/", views.register, name="register"),
]