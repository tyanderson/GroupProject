from django.shortcuts import render
from forms import assetForm


def index(request):
    context = {}
    context['form'] = assetForm()
    return render(request, 'index.html', context)