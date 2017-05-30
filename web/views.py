# -*- coding: utf-8 -*-
from django.shortcuts import render
from json import JSONEncoder
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from web.models import Expense, Income, Token, User
from datetime import datetime
from django.utils.crypto import get_random_string
# Create your views here.
@csrf_exempt
def submit_expense(request):
    if 'date' not in request.POST:
        now = datetime.now()
    else:
        now = request.POST['date']
    #print (now)
    this_token = request.POST['token']
    this_user = User.objects.filter\
    (token__token = this_token).get()
    #print (this_user)
    Expense.objects.create(user = this_user,
        text = request.POST['text'],
            amount = request.POST['amount'], date = now)
    print("hello world")
    print(request.POST)
    return JsonResponse(
        {
            'status':'ok',
            }, encoder=JSONEncoder)
@csrf_exempt
def submit_income(request):
    if 'date' not in request.POST:
        now = datetime.now()
    else:
        now = request.POST['date']
    #print (now)
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token \
     = this_token).get()
    #print (this_user)
    Income.objects.create(user = this_user,\
     text = request.POST['text'
        ],
            amount = request.POST['amount'], date = now)
    print("hello world")
    print(request.POST)
    return JsonResponse(
        {
            'status':'ok',
            }, encoder=JSONEncoder)
def register(request):
    print("hello world!")

def index(request):
    return render(request, 'index.html', {
        'foo': 'bar',
    },)
