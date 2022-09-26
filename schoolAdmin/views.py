from django.shortcuts import render

# Create your views here.

def schoolAdmin_home(request):
    return render(request,'schoolAdmin/home.html')

def schoolAdmin_viewstaff(request):
    return render(request,'schoolAdmin/viewstaff.html')

    
def schoolAdmin_addstaff(request):
    return render(request,'schoolAdmin/addstaff.html')

def schoolAdmin_viewstudent(request):
    return render(request,'schoolAdmin/viewstudent.html')
