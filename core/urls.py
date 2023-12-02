from django.urls import path,include
from core import views
urlpatterns = [
    path('',views.home,name="home"),
    path('home/',views.home,name="home"),

]