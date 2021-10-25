from django.urls import path
from . import views

app_name = 'web' 

urlpatterns = [
    path('', views.index,name="index"), 
    path('login/', views.login,name="login"),
    path('signup/', views.signup,name="signup"),
    path('profiler/', views.profiler,name="profiler"), 
    path('profilerB/', views.profilerB,name="profilerB"),
    path('imageupload/', views.imageupload,name="imageupload"),
    path('home/', views.home,name="home"),
]