from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
#from django.http import HttpResponse

# Create your views here.
def sign_up(request):
    if request.method=="POST":
        fm=UserCreationForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:        
     fm=UserCreationForm()
    return render(request,'enroll/signup.html', {'form':fm})
    #return HttpResponse("Sign-up page")