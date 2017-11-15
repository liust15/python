from django.shortcuts import render
import json
# Create your views here.
from django.http import HttpResponse
from students.models import Toutiao
def index(request):
    b= Toutiao.objects.all().values('id')
    print(b)
    b=list(b)
    return HttpResponse(json.dumps(b), content_type="application/json")
   # return HttpResponse("Hello, world. You're at the polls index."+ {'author_list' : a})
def demo(request):
    return HttpResponse("dome")