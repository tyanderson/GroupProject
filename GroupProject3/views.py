from django.shortcuts import render, redirect
import GroupProject3.models as mod
from .forms import assetForm, organizationForm, locationForm, manufacturerForm
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


###### STUFF FOR MANUFACTURERS ######


def manufacturers(request):
    context = {}
    manufacturers = mod.manufacturer.objects.all()

    context['manufacturers'] = manufacturers
    return render(request, 'manufacturers.html', context)


def addManufacturer(request):
    if request.POST:
        form = manufacturerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(manufacturers)

    else:
        form = manufacturerForm()

    context = {}
    context['form'] = form

    return render(request, 'addManufacturer.html', context)


def editManufacturer(request, int):
    if request.POST:
        manufacturer = mod.manufacturer.objects.get(id=int)
        form = manufacturerForm(request.POST, instance=manufacturer)
        if form.is_valid():
            form.save()

            return redirect(manufacturers)

    else:
        context = {}

    manufacturer = mod.manufacturer.objects.get(id=int)
    context['manufacturer'] = manufacturer
    form = manufacturerForm(instance=manufacturer)
    context['form'] = form

    return render(request, 'editManufacturer.html', context)



def deleteManufacturer(request, int):
    context = {}
    if request.META['REQUEST_METHOD'] == 'POST':
        print("posting")
        manufacturer = mod.manufacturer.objects.get(id=int)
        manufacturer.delete()
        
        return redirect(manufacturers)

    else:
        print("not posting")

    manufacturer = mod.manufacturer.objects.get(id=int)
    context['manufacturer'] = manufacturer
    form = manufacturerForm(instance=manufacturer)
    context['form'] = form

    return render(request, 'deleteManufacturer.html', context)


###### STUFF FOR ORGANIZATIONS ######

def organizations(request):
    context = {}
    organizations = mod.organization.objects.all()

    context['organizations'] = organizations
    return render(request, 'organizations.html', context)


def addOrganization(request):
    if request.POST:
        form = organizationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(organizations)

    else:
        form = organizationForm()

    context = {}
    context['form'] = form

    return render(request, 'addOrganization.html', context)


def editOrganization(request, int):
    if request.POST:
        organization = mod.organization.objects.get(id=int)
        form = organizationForm(request.POST, instance=organization)
        if form.is_valid():
            form.save()

            return redirect(organizations)

    else:
        context = {}

    organization = mod.organization.objects.get(id=int)
    context['organization'] = organization
    form = organizationForm(instance=organization)
    context['form'] = form

    return render(request, 'editOrganization.html', context)



def deleteOrganization(request, int):
    context = {}
    if request.META['REQUEST_METHOD'] == 'POST':
        print("posting")
        organization = mod.organization.objects.get(id=int)
        organization.delete()
        
        return redirect(organizations)

    else:
        print("not posting")

    organization = mod.organization.objects.get(id=int)
    context['organization'] = organization
    form = organizationForm(instance=organization)
    context['form'] = form

    return render(request, 'deleteOrganization.html', context)


###### STUFF FOR LOCATIONS ######


def locations(request):
    context = {}
    locations = mod.location.objects.all()

    context['locations'] = locations
    return render(request, 'locations.html', context)


def addLocation(request):
    if request.POST:
        form = locationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(locations)

    else:
        form = locationForm()

    context = {}
    context['form'] = form

    return render(request, 'addLocation.html', context)


def editLocation(request, int):
    if request.POST:
        location = mod.location.objects.get(id=int)
        form = locationForm(request.POST, instance=location)
        if form.is_valid():
            form.save()

            return redirect(locations)

    else:
        context = {}

    location = mod.location.objects.get(id=int)
    context['location'] = location
    form = locationForm(instance=location)
    context['form'] = form

    return render(request, 'editLocation.html', context)



def deleteLocation(request, int):
    context = {}
    if request.META['REQUEST_METHOD'] == 'POST':
        print("posting")
        location = mod.location.objects.get(id=int)
        location.delete()
        
        return redirect(locations)

    else:
        print("not posting")

    location = mod.location.objects.get(id=int)
    context['location'] = location
    form = locationForm(instance=location)
    context['form'] = form

    return render(request, 'deleteLocation.html', context)