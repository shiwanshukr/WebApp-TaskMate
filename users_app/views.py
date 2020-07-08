from django.shortcuts import render, redirect
from .forms import CustomRegisterForm
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method == "POST":
        register_form = CustomRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save() # in db so lets not check it now.
            messages.success(request,('New User account created, LOGIN TO GET STARTED!'))
            return redirect('register')


    else:

        register_form = CustomRegisterForm()

    return render(request, 'register.html', {'register_form': register_form})


    