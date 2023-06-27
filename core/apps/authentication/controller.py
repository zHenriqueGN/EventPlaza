from .models import User
from django.contrib.messages import add_message, constants
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group


def register_user(request, data) -> bool:
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")
    confirmpassword = data.get("confirmpassword")
    user_group = data.get("user_group")

    if password != confirmpassword:
        add_message(request, constants.ERROR, "Your passwords are different!")
        return False

    if User.objects.filter(username=username).exists():
        add_message(request, constants.ERROR, "Username already exists!")
        return False

    if User.objects.filter(email=email).exists():
        add_message(request, constants.ERROR, "Email already registered!")
        return False

    user = User.objects.create_user(username=username, email=email, password=password)

    if not add_group(user, user_group):
        User.objects.get(username=username).delete()
        add_message(request, constants.ERROR, "The selected group does not exists!")
        return False

    add_message(request, constants.SUCCESS, "User successfully registered!")

    return True


def add_group(user: User, group: str) -> Group:
    if not Group.objects.filter(name=group).exists():
        return False
    group = Group.objects.get(name=group)
    user.groups.add(group)
    return True


def login_user(request, data) -> bool:
    username = data.get("username")
    password = data.get("password")

    user = authenticate(username=username, password=password)

    if not user:
        add_message(request, constants.ERROR, "Username or password are incorrect!")
        return False

    login(request, user)
    add_message(request, constants.SUCCESS, "User successfully logged in!")

    return True
