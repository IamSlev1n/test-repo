from django.shortcuts import render
from django.http import JsonResponse
from user.models import User


# Create your views here.
def users_view(request):
    users = User.objects.all().values()
    data = {"users": list(users)}
    return JsonResponse(data)
