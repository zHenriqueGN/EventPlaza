from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .controller import event_register
from .models import Event


class EventRegisterView(View):
    @method_decorator(login_required(login_url="/authentication/login/"))
    def get(self, request):
        return render(request, "eventregister.html")

    @method_decorator(login_required(login_url="/authentication/login/"))
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


class EventEditView(View):
    @method_decorator(login_required(login_url="/authentication/login/"))
    def get(self, request):
        title_filter = request.GET.get("title")
        events = Event.objects.filter(owner=request.user)
        if title_filter:
            events = events.filter(title__contains=title_filter)
        context = {"events": events}
        return render(request, "eventedit.html", context)
