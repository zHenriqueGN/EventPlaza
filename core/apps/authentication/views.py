from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .controller import register_user, login_user
from django.contrib.auth import logout
from django.contrib.messages import add_message, constants


class RegisterView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("/events/")
        return render(request, "register.html")

    def post(self, request):
        if request.user.is_authenticated:
            return redirect("/events/")
        data = {
            "username": request.POST.get("username"),
            "email": request.POST.get("email"),
            "password": request.POST.get("password"),
            "confirmpassword": request.POST.get("confirmpassword"),
            "user_group": request.POST.get("user_group"),
        }
        if not register_user(request, data):
            return redirect(reverse("register"))
        return redirect(reverse("login"))


class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("/events/")
        return render(request, "login.html")

    def post(self, request):
        if request.user.is_authenticated:
            return redirect("/events/")        
        data = {
            "username": request.POST.get("username"),
            "password": request.POST.get("password"),
        }
        if not login_user(request, data):
            return redirect(reverse("login"))
        return redirect("/events/")


class LogoutView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect(reverse("login"))
        logout(request)
        add_message(request, constants.SUCCESS, "User successfully logged out!")
        return redirect(reverse("login"))
