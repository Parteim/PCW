from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView

from .forms import UserCreationCustomForm


class SignIn(LoginView):
    template_name = 'user/sign_in.html'


class Logout(LogoutView):
    template_name = 'user/logout.html'


def sign_up(request):
    if request.method == 'POST':
        form = UserCreationCustomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = UserCreationCustomForm()

    return render(request, 'user/sign_up.html', {'form': form})
