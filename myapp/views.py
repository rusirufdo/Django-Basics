from django.shortcuts import render
from django.http import HttpResponse

from .models import Question

# Create your views here.
def index(req):
    q_list = Question.objects.order_by('pub_date')[:2]
    p = []
    for a in q_list:
        p.append(a.question_text)
    out = ', '.join(p)
    return HttpResponse(out)

# def index(req):
#     return HttpResponse("Hello Index Works!!!")