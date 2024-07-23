from django.urls import path
from . import views

urlpatterns = [
    path('',views.zetflix,name="home"),
    path('add/',views.add,name="add"),
    path('remove/',views.remove,name="remove"),
    path('list/',views.list,name="list")
]
