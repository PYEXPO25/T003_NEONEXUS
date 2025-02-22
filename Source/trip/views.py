from django.shortcuts import render, redirect  # type: ignore
from .forms import *
from .models import *  # Ensure correct model import
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# ✅ Home Page View
 # Redirects to login if not authenticated
def home(request):
    return render(request, 'home.html')

# ✅ Login View
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home after login
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})

    return render(request, 'login.html')

# ✅ Logout View
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout

# ✅ Route Page (Map Page)
def Routepage(request):
    return render(request, 'map.html')

# ✅ Hidden Spots Page
def AllHiddenSpots(request):
    context = {
        "all_hidden": HiddenSpot.objects.all()  # Ensure correct model name
    }
    return render(request, 'district.html', context)

# ✅ Delete a Spot
def DeleteProducts(request, id):
    selected_spot = HiddenSpot.objects.get(id=id)
    selected_spot.delete()  # Ensure the delete action is per
