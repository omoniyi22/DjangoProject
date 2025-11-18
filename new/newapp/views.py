from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import View
from .models import MenuItem


def list_menu(request):
    menus = MenuItem.objects.all()
    return render(request, "menu_list.html", {"menus": menus})


def delete_item(request, pk):
    menu = get_object_or_404(MenuItem, pk=pk)
    menu.delete()
    return redirect("list_menu")  # redirect to your list page


def create_menu(request):
    if(request.method == "POST"):
        name = request.POST.get("name")
        price = request.POST.get("price")

        MenuItem.objects.create(name=name, price=price)
        return redirect("list_menu")

    return render(request, "create_menu.html")


def menu_details(request, pk):
    menu = get_object_or_404(MenuItem, pk=pk)
    return render(request, "menu_details.html", {"menu": menu})
