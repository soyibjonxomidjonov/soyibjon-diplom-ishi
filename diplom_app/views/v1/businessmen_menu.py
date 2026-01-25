from django.http import HttpResponse
from django.shortcuts import render, redirect
from diplom_app.forms import ProductForm, BusinessForm
from django.contrib import messages # Xabarlar uchun
from diplom_app.views.v1.register import login_decorator
from diplom_app.models import Businessmen


@login_decorator
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)

            post.auther = request.user

            post.save()
            messages.success(request, "Maxsulot Muvofaqqiyatli ro'yxatga qo'shildi.")
            return redirect("/")
        else:
            return render(request, 'forms/add_product.html', {'form': form})
    else:
        form = ProductForm()

    return render(request, 'forms/add_product.html', {'form': form})


@login_decorator
def add_biznes(request):
    if request.method == "POST":
        form = BusinessForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            try:
                owner_profile = Businessmen.objects.get(user_id_id=request.user_id)
                post.business_owner = owner_profile
                post.business_owner = owner_profile

                post.save()
                messages.success(request, "Yangi biznes ochildi.")
                return redirect("/")
            except Businessmen.DoesNotExist:
                # Agar bu user hali Businessmen sifatida ro'yxatdan o'tmagan bo'lsa
                return HttpResponse("Sizda biznes qo'shish huquqi yo'q (Businessmen profili topilmadi).")
        else:
            return render(request, 'forms/biznes_form.html', {'form': form})
    else:
        form = BusinessForm()

    return render(request, 'forms/biznes_form.html', {'form': form})