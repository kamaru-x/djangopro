from turtle import home
from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('',views.index,name='index'),
    path('home/',views.home,name='home'),
    path('addtogallery/',views.addtogallery,name='addtogallery'),
    path('details/<int:id>',views.details,name='details'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
]

#add views