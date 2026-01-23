from django.shortcuts import render, redirect
from diplom_app.forms import ProductForm, UsersForm, BusinessForm, CategoryForm
from diplom_app.models import Users, Businessmen, Business, Category, Product
from django.core.exceptions import PermissionDenied


def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            product = form.save(commit=False)

            if product.business_turi.businessman_user == request.user:
                product.save()
                return redirect("Text input")
            else:
                raise PermissionDenied
    else:
        form = ProductForm(user=request.user)

    return render(request, "add_product.html", {"form": form})






















