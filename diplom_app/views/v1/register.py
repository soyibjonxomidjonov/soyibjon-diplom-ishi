from django.http import HttpResponse
from django.shortcuts import render, redirect
from diplom_app.forms import UsersForm, LoginForm
from django.contrib import messages # Xabarlar uchun
from diplom_app.models import Users



def login_decorator(view_func):
    def wrapper(request, *args, **kwargs):
        if 'user_id' not in request.session:
            return redirect("login")
        return view_func(request, *args, **kwargs)

    return wrapper


def login_page(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            forma_user = form.cleaned_data.get("username")
            forma_password = form.cleaned_data.get("password")
            try:
                baza_user = Users.objects.get(username=forma_user)
                if str(baza_user.password) == str(forma_password):
                    request.session["user_id"] = baza_user.id
                    return HttpResponse("""Siz muvofaqqiyatli login qildingiz!
        <a href='/logout/'>Tizimdan chiqish</a> <br>
        <a href='/'>Asosiy sahifa</a>""")
            except Users.DoesNotExist:
                return HttpResponse("Bunday username mavjud emas!")
    else:
        form = LoginForm()

    return render(request, "forms/login.html", {'form': form})












def user_register(request):
    if request.method == "POST":
        form = UsersForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)

            post.auther = request.user

            post.save()
            messages.success(request, "Siz Muvofaqqiyatli ro'yxatdan o'tdingiz.")
            return redirect("/")
        else:
            return HttpResponse("Formani to'ldirishda xatolik bor!")
    else:
        form = UsersForm()

    return render(request, 'forms/register.html', {'form': form})




























