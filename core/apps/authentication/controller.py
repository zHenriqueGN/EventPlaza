from .models import User
from django.contrib.messages import add_message, constants
from django.contrib.auth import authenticate, login


def register_user(request, data) -> bool:
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")
    confirmpassword = data.get("confirmpassword")

    if password != confirmpassword:
        add_message(request, constants.ERROR, "Your passwords are different!")
        return False

    if User.objects.filter(username=username).exists():
        add_message(request, constants.ERROR, "Username already exists!")
        return False

    if User.objects.filter(email=email).exists():
        add_message(request, constants.ERROR, "Email already registered!")
        return False

    User.objects.create_user(username=username, email=email, password=password)

    return True


def login_user(request, data) -> bool:
    username = data.get("username")
    password = data.get("password")

    user = authenticate(username=username, password=password)

    if not user:
        add_message(request, constants.ERROR, "Username or password are incorrect!")
        return False

    login(request, user)

    return True
