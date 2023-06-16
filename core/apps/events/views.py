from django.shortcuts import render
from django.views import View


class EventRegisterView(View):
    def get(self, request):
        return render(request, "eventregister.html")
