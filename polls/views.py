from django.shortcuts import render
from .models import Question

# Create your views here.
def index(request):
    questions = Question.objects.all()
    return render(request, "index.html", {"questions": questions})


def vote(request, pk):
    question = Question.objects.get(id=pk)
    options = question.choices.all()
    # if request.method == 'POST':
    #     input_value = request.POST['choice']
    #     selected_option = options.get(id=input_value)
    #     selected_option.vote += 5
    #     selected_option.save()
    return render(request, "vote.html", {'question': question, 'options': options})


def result(request, pk):
    question = Question.objects.get(id=pk)
    options = question.choices.all()
    if request.method == 'POST':
        input_value = request.POST['choice']
        selected_option = options.get(id=input_value)
        selected_option.vote += 5
        selected_option.save()
    return render(request, "result.html", {'question': question, 'options': options})
