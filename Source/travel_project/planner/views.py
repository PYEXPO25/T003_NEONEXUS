
from django.shortcuts import render,redirect
from .forms import TravelForm
from .forms import PlaceForm
from .models import Place

def generate_plan(request):
    if request.method == 'POST':
        form = TravelForm(request.POST)
        if form.is_valid():
            places = form.cleaned_data['places']
            return render(request, 'planner/display_plan.html', {'places': places})
    else:
        form = TravelForm()
    return render(request, 'planner/generate_plan.html', {'form': form})
def add_place(request):
    if request.method == 'POST':
        form = PlaceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_place')
    else:
        form = PlaceForm()
    return render(request, 'planner/add_place.html', {'form': form})