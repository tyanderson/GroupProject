from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render


def index(request):
    template = loader.get_template('templates/index.html')
    return render(request, 'polls/index.html')
    # return HttpResponse(template.render())
