from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .controller import event_register


class EventRegisterView(View):
    @method_decorator(login_required(login_url="/authentication/login/"))
    def get(self, request):
        return render(request, "eventregister.html")

    def post(self, request):
        data = {
            "owner": request.user,
            "title": request.POST.get("title"),
            "logo": request.FILES.get("logo"),
            "description": request.POST.get("description"),
            "start_date": request.POST.get("start_date"),
            "end_date": request.POST.get("end_date"),
            "duration": request.POST.get("duration"),
        }

        event_register(request, data)
        return redirect(reverse("event_register"))
