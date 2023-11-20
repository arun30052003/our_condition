from django.shortcuts import render

# Create your views here.

def conditions(request):
    d={'a':100,'b':50,'c':6050}
    return render(request,'app.html',d)