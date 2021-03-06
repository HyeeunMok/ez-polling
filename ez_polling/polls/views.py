from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import JsonResponse

from .models import Question, Select

# Get questions and display them
def index(request):
    latest_question_list = Question.objects.order_by('-published_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

# Show specific question and selects
def detail(request, question_id):
  try:
    question = Question.objects.get(pk=question_id)
  except Question.DoesNotExist:
    raise ("Question does not exist")
  return render(request, 'polls/detail.html', { 'question': question })

# Get question and display results
def results(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  return render(request, 'polls/results.html', { 'question': question })

# Vote for a question select
def vote(request, question_id):
    # print(request.POST['select'])
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_select = question.select_set.get(pk=request.POST['select'])
    except (KeyError, Select.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a select.",
        })
    else:
        selected_select.votes += 1
        selected_select.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def resultsData(request, obj):
    votedata = []

    question = Question.objects.get(id=obj)
    votes = question.select_set.all()

    for i in votes:
        votedata.append({i.select_text:i.votes})

    print(votedata)
    return JsonResponse(votedata, safe=False)


