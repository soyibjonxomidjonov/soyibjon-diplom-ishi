from django.shortcuts import render, redirect
from shops_app.forms import LoginForm, UserForm
from shops_app.forms import User
from shops_app.services.decorators import logout_def


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
