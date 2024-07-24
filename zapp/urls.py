from django.urls import path
from . import views

urlpatterns = [
    path('',views.zetflix,name="home"),
    path('addToList/',views.addToList,name="addToList"),
    path('removeFromList/',views.removeFromList,name="removeFromList"),
    path('myList/',views.myList,name="myList"),

    path('getMovie/',views.getMovie,name="getMovie"),
    path('getTvshow/',views.getTvshow,name="getTvshow"),
    path('getUser/',views.getUser,name="getUser"),

    path('addMovie/',views.addMovie,name="addMovie"),
    path('addTvshow/',views.addTvshow,name="addTvshow"),
    path('addUser/',views.addUser,name="addUser"),

    path('removeMovie/',views.removeMovie,name="removeMovie"),
    path('removeTvshow/',views.removeTvshow,name="removeTvshow"),
    path('removeUser/',views.removeUser,name="removeUser"),

    path('updateMovie/',views.updateMovie,name="updateMovie"),
    path('updateTvshow/',views.updateTvshow,name="updateTvshow"),
    path('updateUser/',views.updateUser,name="updateUser"),
]
