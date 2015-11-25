from django.conf.urls import url
from . import views

# urls
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^addAsset/', views.addAsset, name='addAsset'),
    url(r'^editAsset/([0-9]+$)', views.editAsset, name='editAsset'),
    url(r'^deleteAsset/([0-9]+$)', views.deleteAsset, name='deleteAsset'),
    url(r'^searchAssets/', views.searchAssets, name='searchAssets'),

    url(r'^manufacturers/', views.manufacturers, name='manufacturers'),
    url(r'^addManufacturer/', views.addManufacturer, name='addManufacturer'),
    url(r'^editManufacturer/([0-9]+$)', views.editManufacturer, name='editManufacturer'),
    url(r'^deleteManufacturer/([0-9]+$)', views.deleteManufacturer, name='deleteManufacturer'),

    url(r'^organizations/', views.organizations, name='organizations'),
    url(r'^addOrganization/', views.addOrganization, name='addOrganization'),
    url(r'^editOrganization/([0-9]+$)', views.editOrganization, name='editOrganization'),
    url(r'^deleteOrganization/([0-9]+$)', views.deleteOrganization, name='deleteOrganization'),

    url(r'^locations/', views.locations, name='locations'),
    url(r'^addLocation/', views.addLocation, name='addLocation'),
    url(r'^editLocation/([0-9]+$)', views.editLocation, name='editLocation'),
    url(r'^deleteLocation/([0-9]+$)', views.deleteLocation, name='deleteLocation'),

    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),
]
