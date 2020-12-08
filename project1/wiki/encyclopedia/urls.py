from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:wiki_title>", views.show_wiki, name="show_wiki")
]
