from django.http import HttpResponse
from django.shortcuts import render, redirect
from diplom_app.forms import LoginForm
from diplom_app.models import Users




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
                    return render(request, "biznesmen.html", {"user": baza_user})
            except Users.DoesNotExist:
                return HttpResponse("Bunday username mavjud emas!")
    else:
        form = LoginForm()

    return render(request, "login.html", {'form': form})




























