from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .controller import register_user, login_user
from django.contrib.auth import logout


class RegisterView(View):
    def get(self, request):
        return render(request, "register.html")

    def post(self, request):
        data = {
            "username": request.POST.get("username"),
            "email": request.POST.get("email"),
            "password": request.POST.get("password"),
            "confirmpassword": request.POST.get("confirmpassword"),
        }
        if not register_user(request, data):
            return redirect(reverse("register"))
        return redirect(reverse("login"))


class LoginView(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        data = {
            "username": request.POST.get("username"),
            "password": request.POST.get("password"),
        }
        if not login_user(request, data):
            return redirect(reverse("login"))
        return redirect(reverse("event_register"))


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse("login"))
