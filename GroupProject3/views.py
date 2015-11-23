from django.shortcuts import render, redirect
import GroupProject3.models as mod
from .forms import assetForm
from django.views.generic.edit import UpdateView



def index(request):
    context = {}
    assets = mod.asset.objects.all()

    context['assets'] = assets
    return render(request, 'index.html', context)



def addAsset(request):
    if request.POST:
        form = assetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(index)

    else:
        form = assetForm()

    context = {}
    context['form'] = assetForm

    return render(request, 'addAsset.html', context)


def editAsset(request, int):
    if request.POST:
        asset = mod.asset.objects.get(id=int)
        form = assetForm(request.POST, instance=asset)
        if form.is_valid():
            form.save()
            
            return redirect(index)

    else:
        context = {}

    asset = mod.asset.objects.get(id=int)
    context['asset'] = asset
    form = assetForm(instance=asset)
    context['form'] = form

    return render(request, 'editAsset.html', context)



def deleteAsset(request, int):
    context = {}
    if request.META['REQUEST_METHOD'] == 'POST':
        print("posting")
        asset = mod.asset.objects.get(id=int)
        asset.delete()
        
        return redirect(index)

    else:
        print("not posting")

    asset = mod.asset.objects.get(id=int)
    context['asset'] = asset
    form = assetForm(instance=asset)
    context['form'] = form

    return render(request, 'deleteAsset.html', context)
