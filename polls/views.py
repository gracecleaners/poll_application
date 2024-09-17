from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Choice

# Create your views here.
def index(request):
    question_list_latest = Question.objects.order_by("-pub_date")[:5]
    output = ",".join([q.question_text for q in question_list_latest])
    return HttpResponse(output)

def details(request, question_id):
    return HttpResponse("Your are looking at question %s."% question_id)

def result(request, question_id):
    response = "You are looking at results of question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("your are voting question %s" % question_id)
