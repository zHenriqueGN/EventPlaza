from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from .controller import event_register, event_edit, event_delete
from .models import Event
from core.settings import LOGIN_URL


class EventAccessView(View):
    @method_decorator(
        [
            login_required(login_url=LOGIN_URL),
            user_passes_test(
                lambda user: user.groups.filter(name="Client").exists(),
                login_url="/",
            ),
        ]
    )
    def get(self, request, id):
        event = Event.objects.get(id=id)
        context = {"event": event}
        return render(request, "eventaccess.html", context)


class EventRegisterView(View):
    @method_decorator(
        [
            login_required(login_url=LOGIN_URL),
            user_passes_test(
                lambda user: user.groups.filter(name="Manager").exists(),
                login_url="/",
            ),
        ]
    )
    def get(self, request):
        return render(request, "eventregister.html")

    @method_decorator(
        [
            login_required(login_url=LOGIN_URL),
            user_passes_test(
                lambda user: user.groups.filter(name="Manager").exists(),
                login_url="/",
            ),
        ]
    )
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
    @method_decorator(
        [
            login_required(login_url=LOGIN_URL),
            user_passes_test(
                lambda user: user.groups.filter(name="Manager").exists(),
                login_url="/",
            ),
        ]
    )
    def get(self, request):
        title_filter = request.GET.get("title")
        events = Event.objects.filter(owner=request.user)
        if title_filter:
            events = events.filter(title__contains=title_filter)
        context = {"events": events}
        return render(request, "eventedit.html", context)


class EventEditorView(View):
    @method_decorator(
        [
            login_required(login_url=LOGIN_URL),
            user_passes_test(
                lambda user: user.groups.filter(name="Manager").exists(),
                login_url="/",
            ),
        ]
    )
    def get(self, request, id):
        event = Event.objects.filter(owner=request.user, id=id).first()
        context = {"event": event}
        return render(request, "eventeditor.html", context)

    @method_decorator(
        [
            login_required(login_url=LOGIN_URL),
            user_passes_test(
                lambda user: user.groups.filter(name="Manager").exists(),
                login_url="/",
            ),
        ]
    )
    def post(self, request, id):
        data = {
            "id": id,
            "title": request.POST.get("title"),
            "logo": request.FILES.get("logo"),
            "description": request.POST.get("description"),
            "start_date": request.POST.get("start_date"),
            "end_date": request.POST.get("end_date"),
            "duration": request.POST.get("duration"),
        }
        event_edit(request, data)
        return redirect(reverse("event_editor", args=[id]))


class EventDeleteView(View):
    @method_decorator(
        [
            login_required(login_url=LOGIN_URL),
            user_passes_test(
                lambda user: user.groups.filter(name="Manager").exists(),
                login_url="/",
            ),
        ]
    )
    def post(self, request, id):
        event_delete(request, id)
        return redirect(reverse("event_edit"))
