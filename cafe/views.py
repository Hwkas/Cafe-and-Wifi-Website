from django.shortcuts import render


# Create your views here.
from .models import *
from .forms import *


def home(request):
    all_cafes = CafeModel.objects.all()
    form = CafeFrom()
    context = {"form": form}
    if request.method == "POST":
        form = CafeFrom(request.POST)
        if form.is_valid():
            form.save()
    return render(request, "cafe/index.html", context)


def add_cafe(request):
    form = CafeFrom()
    context = {"form": form}
    if request.method == "POST":
        form = CafeFrom(request.POST)
        if form.is_valid():
            form.save()
    return render(request, "cafe/add.html", context)
