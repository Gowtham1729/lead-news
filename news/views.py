from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def news(request):
    template = loader.get_template('first.html')
    return HttpResponse(template.render())
