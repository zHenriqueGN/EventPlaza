from django.shortcuts import render
from django.http import JsonResponse
from django.views import View


class RegisterView(View):
    def get(self, request):
        return render(request, "register.html")

    def post(self, request):
        return JsonResponse(dict(request.POST))
