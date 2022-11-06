from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("/image",views.view_image, name="image")
]