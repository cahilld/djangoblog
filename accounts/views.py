from django.shortcuts import render, redirect, reverse
from django.contrib import messages, auth
from .forms import UserLoginForm

# Create your views here.
def get_index(request):
    return render(request, 'index.html')

def logout(request):
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(get_index)

def login(request):
    if request.method=="POST":
        form=UserLoginForm(request.POST)
        
        if form.is_valid():
            user = auth.authenticate(username=form.cleaned_data['username'],
                                     password=form.cleaned_data['password'])
            if user is not None:
                auth.login(request, user)
            else:
                form.add_error(None, "Your details are not valid")
            return redirect(get_index)
    else:
        form = UserLoginForm()
    
    return render(request, "login.html", {'form': form})