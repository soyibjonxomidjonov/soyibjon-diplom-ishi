from django.shortcuts import render, redirect
from django.http import HttpResponse
from shops_app.forms import LoginForm, ProductForm
from shops_app.forms import User
from shops_app.services.decorators import login_decorator, logout_def
from shops_app.models import Shop



def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            forma_user = form.cleaned_data.get("username")
            forma_password = form.cleaned_data.get("password")
            try:
                baza_user = User.objects.get(username=forma_user)
                if str(baza_user.password) == str(forma_password):
                    request.session["user_id"] = baza_user.id
                    next_url = request.GET.get('next', '/')
                    return redirect(next_url)
            except User.DoesNotExist:
                return redirect('login')
    else:
        form = LoginForm()

    return render(request, "forms/login.html", {'form': form})


@login_decorator
def product(request):
    owner_shops = Shop.objects.filter(owner=request.my_user)
    if not owner_shops.exists():
        return HttpResponse("Sizda do'kon mavjud emas. Iltimos, avval do'kon yarating.")
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        selected_shop_id = request.POST.get('shop_id')
        if form.is_valid() and selected_shop_id:
            information = form.save(commit=False)
            user_shop = Shop.objects.filter(id=selected_shop_id).first()
            if user_shop:
                information.shop = user_shop

                information.save()
                return HttpResponse("""Product muvaffaqiyatli qo'shildi!""")
            else:
                return HttpResponse("Xatolik: Bu do'kon sizga tegishli emas!")
    else:
        form = ProductForm()

    return render(request, "forms/product.html", {'form': form, 'owner_shops': owner_shops})


def logout_page(request):
    logout_def(request)
    return redirect("login")