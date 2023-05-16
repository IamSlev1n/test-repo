from django.shortcuts import render
from django.http import JsonResponse
from purchase.models import Purchase
from django.core.serializers import serialize
import datetime


# Create your views here.
def purchases_view(request):
    purchases = Purchase.objects.all().values()
    data = {"purchases": list(purchases)}
    return JsonResponse(data)

