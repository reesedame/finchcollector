from django.shortcuts import render, redirect
from .models import Finch, Location
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from .forms import FeedingForm


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def finches_index(request):
    finches = Finch.objects.all()
    return render(request, "finches/index.html", {"finches": finches})


def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    feeding_form = FeedingForm()
    id_list = finch.locations.all().values_list("id")
    available_locations = Location.objects.exclude(id__in=id_list)
    return render(
        request,
        "finches/detail.html",
        {
            "finch": finch,
            "feeding_form": feeding_form,
            "locations": available_locations,
        },
    )


def add_feeding(request, finch_id):
    form = FeedingForm(request.POST)

    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.finch_id = finch_id
        new_feeding.save()

    return redirect("detail", finch_id=finch_id)


def assoc_location(request, finch_id, location_id):
    Finch.objects.get(id=finch_id).locations.add(location_id)
    return redirect("detail", finch_id=finch_id)


class FinchCreate(CreateView):
    model = Finch
    fields = ["species", "scientific_name", "conservation_status"]


class FinchUpdate(UpdateView):
    model = Finch
    fields = ["conservation_status"]


class FinchDelete(DeleteView):
    model = Finch
    success_url = "/finches"


class LocationList(ListView):
    model = Location


class LocationCreate(CreateView):
    model = Location
    fields = ["name"]
