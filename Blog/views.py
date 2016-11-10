# coding:utf-8
import json
import os

from django.http import HttpResponse
from django.shortcuts import render
from django.utils.translation import ugettext

from Blog.Model.models import Question


def index(request):
    context = {}
    context['str'] = os.path.join(os.path.dirname(__file__), "..")
    context['question'] = Question.objects.all()
    context['hello'] = ugettext('hello')
    context['world'] = ugettext('world!')
    return render(request, "blog/index2.html", context)
    return render(request, "blog/index.html", context)


def add(request):
    response_data = {}
    response_data['result'] = 'failed'
    response_data['message'] = 'You messed up'
    # json_adta = serializers.serialize('json',response_data)
    return HttpResponse(json.dumps(response_data), content_type="application/json")


def delete(request):
    response_data = {}
    response_data['result'] = 'failed'
    response_data['message'] = 'You messed up'
    # json_adta = serializers.serialize('json',response_data)
    return HttpResponse(json.dumps(response_data), content_type="application/json")


def update(request):
    response_data = {}
    response_data['result'] = 'failed'
    response_data['message'] = 'You messed up'
    # json_adta = serializers.serialize('json',response_data)
    return HttpResponse(json.dumps(response_data), content_type="application/json")


def get(request):
    return render(request, "test.html")

