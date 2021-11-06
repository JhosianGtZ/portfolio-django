from django.urls import path
from . import views


app_name = "blog"
urlpatterns = [
    path("", views.renderposts, name="posts"),
    path("<int:post_id>", views.post_detail, name="post_detail"),
]
