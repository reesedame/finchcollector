from django.shortcuts import render

finches = [
    {"species": "American Goldfinch", "scientificName": "Spinus tristis"},
    {"species": "Northern Cardinal", "scientificName": "Cardinalis cardinalis"},
]


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def finches_index(request):
    return render(request, "finches/index.html", {"finches": finches})
