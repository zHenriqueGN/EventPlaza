from .models import User
from django.contrib.messages import add_message, constants


def register_user(request, data) -> bool:
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")
    confirmpassword = data.get("confirmpassword")

    if password != confirmpassword:
        add_message(request, constants.WARNING, "Your passwords are different!")
        return False

    if User.objects.filter(username=username).exists():
        add_message(request, constants.WARNING, "Username already exists!")
        return False

    if User.objects.filter(email=email).exists():
        add_message(request, constants.WARNING, "Email already registered!")
        return False

    User.objects.create_user(username=username, email=email, password=password)

    return True
