from django.shortcuts import render

# Create your views here.
def userfilter(request):
    d={'data':'Django is a High Level Language'}
    return render(request,'userfilter.html',d)