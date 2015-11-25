from django.shortcuts import render, redirect
import GroupProject3.models as mod
from .forms import assetForm, organizationForm, locationForm, manufacturerForm
from django.contrib.auth import authenticate


def index(request):

    context = {}

    # Go to login user if no session
    if not request.session.get('logged_in'):
        return render(request, 'login.html', context)

    # get assets
    assets = mod.asset.objects.all()

    context['assets'] = assets
    # go here with assets
    return render(request, 'index.html', context)


def addAsset(request):

    if request.POST:
        # create form from post
        form = assetForm(request.POST)
        if form.is_valid():
            # save form
            form.save()
            return redirect(index)

    else:
        form = assetForm()

    context = {}
    context['form'] = assetForm

    # go here
    return render(request, 'addAsset.html', context)


def editAsset(request, int):
    if request.POST:
        # get asset
        asset = mod.asset.objects.get(id=int)
        # populate form
        form = assetForm(request.POST, instance=asset)
        if form.is_valid():
            # save form
            form.save()

            return redirect(index)

    else:
        context = {}

    asset = mod.asset.objects.get(id=int)
    context['asset'] = asset
    form = assetForm(instance=asset)
    context['form'] = form

    # go here
    return render(request, 'editAsset.html', context)


def searchAssets(request):
    context = {}

    # Go to login user if no session
    if not request.session.get('logged_in'):
        return render(request, 'login.html', context)

    print("got in")
    if request.META['REQUEST_METHOD'] == 'POST':
        print("searching")
        str = request.POST.get('searchString')
        # get assets containing string
        context['assets'] = mod.asset.objects.all().filter(name__icontains=str)

    # go here with assets
    return render(request, 'index.html', context)


def deleteAsset(request, int):
    context = {}
    if request.META['REQUEST_METHOD'] == 'POST':
        print("posting")
        # find asset
        asset = mod.asset.objects.get(id=int)
        asset.delete()
        
        return redirect(index)

    else:
        print("not posting")

    # get asset
    asset = mod.asset.objects.get(id=int)
    context['asset'] = asset
    form = assetForm(instance=asset)
    context['form'] = form

    # go here
    return render(request, 'deleteAsset.html', context)


###### STUFF FOR MANUFACTURERS ######


def manufacturers(request):
    context = {}

    # Go to login user if no session
    if not request.session.get('logged_in'):
        return render(request, 'login.html', context)

    # get manufacturers
    manufacturers = mod.manufacturer.objects.all()

    context['manufacturers'] = manufacturers
    # go here
    return render(request, 'manufacturers.html', context)


def addManufacturer(request):
    if request.POST:
        # create form from post
        form = manufacturerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(manufacturers)

    else:
        form = manufacturerForm()

    context = {}
    context['form'] = form

    # go here
    return render(request, 'addManufacturer.html', context)


def editManufacturer(request, int):
    if request.POST:
        # get manufacturer
        manufacturer = mod.manufacturer.objects.get(id=int)
        # populate form
        form = manufacturerForm(request.POST, instance=manufacturer)
        if form.is_valid():
            form.save()

            return redirect(manufacturers)

    else:
        context = {}

    # get manufacturer
    manufacturer = mod.manufacturer.objects.get(id=int)
    context['manufacturer'] = manufacturer
    form = manufacturerForm(instance=manufacturer)
    context['form'] = form

    # go here
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

    # get manufacturer
    manufacturer = mod.manufacturer.objects.get(id=int)
    context['manufacturer'] = manufacturer
    form = manufacturerForm(instance=manufacturer)
    context['form'] = form

    # go here
    return render(request, 'deleteManufacturer.html', context)


###### STUFF FOR ORGANIZATIONS ######

def organizations(request):
    context = {}

    # Go to login user if no session
    if not request.session.get('logged_in'):
        return render(request, 'login.html', context)

    # get organizations
    organizations = mod.organization.objects.all()

    context['organizations'] = organizations
    # go here
    return render(request, 'organizations.html', context)


def addOrganization(request):
    if request.POST:
        # create form from post
        form = organizationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(organizations)

    else:
        form = organizationForm()

    context = {}
    context['form'] = form

    # go here
    return render(request, 'addOrganization.html', context)


def editOrganization(request, int):
    if request.POST:
        # get organization
        organization = mod.organization.objects.get(id=int)
        # populate form
        form = organizationForm(request.POST, instance=organization)
        if form.is_valid():
            form.save()

            return redirect(organizations)

    else:
        context = {}

    # get organization
    organization = mod.organization.objects.get(id=int)
    context['organization'] = organization
    form = organizationForm(instance=organization)
    context['form'] = form

    # go here
    return render(request, 'editOrganization.html', context)


def deleteOrganization(request, int):
    context = {}
    if request.META['REQUEST_METHOD'] == 'POST':
        print("posting")
        # get organization
        organization = mod.organization.objects.get(id=int)
        organization.delete()
        
        return redirect(organizations)

    else:
        print("not posting")

    # get organization
    organization = mod.organization.objects.get(id=int)
    context['organization'] = organization
    form = organizationForm(instance=organization)
    context['form'] = form

    # go here
    return render(request, 'deleteOrganization.html', context)


###### STUFF FOR LOCATIONS ######


def locations(request):
    context = {}

    # Go to login user if no session
    if not request.session.get('logged_in'):
        return render(request, 'login.html', context)

    # get locations
    locations = mod.location.objects.all()

    context['locations'] = locations
    # go here
    return render(request, 'locations.html', context)


def addLocation(request):
    if request.POST:
        # create form from post
        form = locationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(locations)

    else:
        form = locationForm()

    context = {}
    context['form'] = form

    # go here
    return render(request, 'addLocation.html', context)


def editLocation(request, int):
    if request.POST:
        # get location
        location = mod.location.objects.get(id=int)
        # populate form
        form = locationForm(request.POST, instance=location)
        if form.is_valid():
            form.save()

            return redirect(locations)

    else:
        context = {}

    # get location
    location = mod.location.objects.get(id=int)
    context['location'] = location
    form = locationForm(instance=location)
    context['form'] = form

    # go here
    return render(request, 'editLocation.html', context)


def deleteLocation(request, int):
    context = {}
    if request.META['REQUEST_METHOD'] == 'POST':
        print("posting")
        # get location
        location = mod.location.objects.get(id=int)
        location.delete()
        
        return redirect(locations)

    else:
        print("not posting")

    # get location
    location = mod.location.objects.get(id=int)
    context['location'] = location
    form = locationForm(instance=location)
    context['form'] = form

    # go here
    return render(request, 'deleteLocation.html', context)


def login(request):
    context = {}
    if request.META['REQUEST_METHOD'] == 'POST':
        print("logging in")
        # authenticate user
        user = authenticate(
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )

        if user is not None:
            # the password verified for the user
            if user.is_active:
                print("User is valid, active and authenticated")
                # Get index's asset data
                assets = mod.asset.objects.all()
                context['assets'] = assets
                context['failed'] = False
                request.session['logged_in'] = True
            else:
                print("The password is valid, but the account has been disabled!")
                context['failed'] = True
                # auth failed, go login
                return render(request, 'login.html', context)
        else:
            # the authentication system was unable to verify the username and password
            print("The username and password were incorrect.")
            context['failed'] = True
            # auth failed, go login
            return render(request, 'login.html', context)

    # go to index
    return render(request, 'index.html', context)


def logout(request):
    context = {}
    # if there's a session, delete it
    if request.session.get('logged_in'):
        del request.session['logged_in']

    # go to login
    return render(request, 'login.html', context)