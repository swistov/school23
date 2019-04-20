from django.shortcuts import render
from django.http import HttpResponse
from maths.forms import CreateNewEvaluationsForm

from random import randint, choice
import numexpr as ne


def create_eval(number=40):
    first = str(randint(1, number))
    two = str(randint(1, number))
    operators = '+', '-'
    action = choice(operators)
    expr = first + ' ' + action + ' ' + two
    answer = ne.evaluate(expr).item()

    if answer < 0:
        create_eval()
        return {'expr': expr, 'answer': answer}

    return {'expr': expr, 'answer': answer}


def index(request):
    if request.method == 'POST':
        return render(request, 'maths/index.html')
    else:
        print(create_eval())
    return render(request, 'maths/index.html', {})
