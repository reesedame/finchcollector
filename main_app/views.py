from django.shortcuts import render
from .models import Finch
from django.views.generic.edit import CreateView, UpdateView, DeleteView


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def finches_index(request):
    finches = Finch.objects.all()
    return render(request, "finches/index.html", {"finches": finches})


def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    return render(request, "finches/detail.html", {"finch": finch})


class FinchCreate(CreateView):
    model = Finch
    fields = ["species", "scientific_name", "conservation_status"]


class FinchUpdate(UpdateView):
    model = Finch
    fields = ["conservation_status"]


class FinchDelete(DeleteView):
    model = Finch
    success_url = "/finches"
