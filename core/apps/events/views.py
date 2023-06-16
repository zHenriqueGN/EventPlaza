from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class EventRegisterView(View):
    @method_decorator(login_required(login_url="/authentication/login/"))
    def get(self, request):
        return render(request, "eventregister.html")
