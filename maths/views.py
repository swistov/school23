from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    if request.method == 'GET':
        return render(request, '')
    else:
        HttpResponse(status=500)