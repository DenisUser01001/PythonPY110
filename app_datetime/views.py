from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

from datetime import datetime

# Create your views here.

def datetime_view(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        data = datetime.now()
        return HttpResponse(data.strftime('%H:%M %d/%m/%Y'))
