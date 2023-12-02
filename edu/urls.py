from django.urls import path,include
from edu import views
urlpatterns = [
    path('educationdet/',views.education_de,name="edudet"),

]