from django.shortcuts import render
import json
# Create your views here.
from django.http import HttpResponse
from students.models import Article
def index(request):
    b= Article.objects.all().values('title')
    print(b)
    b=list(b)
    a={"df":1,"b":b}
    return HttpResponse(json.dumps(a), content_type="application/json")
   # return HttpResponse("Hello, world. You're at the polls index."+ {'author_list' : a})
def demo(request):
    return HttpResponse("dome")