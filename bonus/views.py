from django.shortcuts import render
from .models import *
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.contrib.auth import models
import json
from django.core import serializers
from django.db.models import Avg, Count, Sum, FloatField

# Возвращает все транзакции пользователя сессии | JSON
def ReturnAllUserTransactions(request):
    print(request.user)
    if request.user.is_authenticated:
        transactions = BonusTransaction.objects.filter(user=request.user.id).order_by('-date_created') # получение всех транзакций пользователя
        return JsonResponse(serializers.serialize('json', transactions), safe=False)
    else:
        return HttpResponseBadRequest()

# Возвращает сумму всех транзакций пользователя сессии | Http
def ReturnUserTransactionSum(request):
    if request.user.is_authenticated:
        transactions_sum = (BonusTransaction.objects.filter(user=request.user.id).aggregate(value_sum=Sum('value', output_field=FloatField())))['value_sum']
        return HttpResponse(transactions_sum)
    else:
        return HttpResponseBadRequest()

def testrequest(request):
    return render(request, 'bonus/requestin.html')




# def requesting_view(request):
    #transactions = BonusTransaction.objects.filter(date_created__lte=timezone.now()).order_by('-date_created')
    # return render(request, 'onlinepayment/requesting.html', {})

#def GetUser(request):
     # user = models.User.objects.filter(pk=uid) # получение пользователя
        # user_json = serializers.serialize('json', list(user), fields=('username','date_joined','first_name','last_name')) # конвертация в JSON
        # ^---- это нужно попробовать реализовать через сессию текущего юзера

# def GetUserBonusTransactions(request):

#     if request.user.is_authenticated:

#         transactions = BonusTransaction.objects.filter(user=request.user.id).order_by('-date_created') # получение всех транзакций пользователя
#         transactions_json = serializers.serialize('json', list(transactions), fields=('value','date_created')) # конвертация в JSON

#         return HttpResponse(json.dumps(transactions_json), content_type="application/json")
#     else:
#         return HttpResponseBadRequest()

