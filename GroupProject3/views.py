from django.shortcuts import render
import GroupProject3.models as mod



def index(request):
    context = {}
    assets = mod.asset.objects.all()

    context['assets'] = assets
    return render(request, 'index.html', context)



def addAsset(request):
    context = {}

    return render(request, 'addAsset.html', context)