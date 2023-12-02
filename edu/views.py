from django.shortcuts import render,HttpResponse

# Create your views here.

def education_de(request):
    return render(request,"edu/skill.html")