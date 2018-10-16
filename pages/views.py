from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Hello Laura,</h1><br><p>You look beautiful pregnant. Do you know?</p>')