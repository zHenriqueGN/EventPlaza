from django.shortcuts import render


def handler404(request, exception=None):
    return render(request, "utils/404_page.html")


def handler500(request, exception=None):
    return render(request, "utils/500_page.html")
