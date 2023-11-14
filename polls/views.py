from django.http import HttpResponse
from django.template import loader

from polls.models import Question


def index(request):
    latest_question = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")

    context = {
        "latest_question": latest_question,
    }
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    return HttpResponse("You're looking at question %s" % question_id)


def results(request, question_id):
    return HttpResponse("The result for %s" % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s" % question_id)
