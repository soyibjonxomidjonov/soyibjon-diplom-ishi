from django.shortcuts import render, redirect
from django.http import HttpResponse
from shops_app.forms import LoginForm, ProductForm, ShopForm, UserForm
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
def product_add(request):
    owner_shops = Shop.objects.filter(owner=request.my_user)
    if not owner_shops.exists():
        return HttpResponse("Sizda do'kon mavjud emas. Iltimos, avval do'kon yarating.")
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, user=request.my_user)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print(form.errors)
    else:
        form = ProductForm(user=request.my_user)

    return render(request, "forms/product.html", {'form': form, 'owner_shops': owner_shops})





@login_decorator
def shop_add(request):
    if request.method == "POST":
        form = ShopForm(request.POST, request.FILES)
        if form.is_valid():
            shop = form.save(commit=False)
            shop.owner = request.my_user
            shop.save()
            return redirect('/')
        else:
            print(form.errors)
    else:
        form = ShopForm()

    return render(request, "forms/product.html", {'form': form})



def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print(form.errors)
    else:
        form = UserForm()

    return render(request, 'forms/register.html', {'form': form})

















def logout_page(request):
    logout_def(request)
    return redirect("login")
























