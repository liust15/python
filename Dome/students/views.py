from django.shortcuts import render
import json
# Create your views here.
from django.http import HttpResponse
from students.models import Toutiao
from datetime import datetime
from django.core import serializers


def index(request):
    data = Toutiao.objects.all().values()
    datas = list(data)
    return HttpResponse(json.dumps(datas), content_type = "application/json")
   # return HttpResponse("Hello, world. You're at the polls index."+ {'author_list' : a})


def demo(request):
    return HttpResponse("dome")


def test(request):
    return render(request, 'test.html', {'current_time': datetime.now()})
