from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Question, Choice
from django.template import loader

# Create your views here.
def index(request):
    question_list_latest = Question.objects.order_by("-pub_date")[:5]
    context = {
        'question_list_latest': question_list_latest
    }
    return render(request, 'index.html', context)

def details(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'detail.html', {'question':question})


def result(request, question_id):
    response = "You are looking at results of question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("your are voting question %s" % question_id)
