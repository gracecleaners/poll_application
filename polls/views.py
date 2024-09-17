from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("hello Oscar")

def details(request, question_id):
    return HttpResponse("Your are looking at question %s."% question_id)

def result(request, question_id):
    response = "You are looking at results of question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("your are voting question %s" % question_id)
