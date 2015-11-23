from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^addAsset/', views.addAsset, name='addAsset'),
    url(r'^editAsset/([0-9]+$)', views.editAsset, name='editAsset'),
    url(r'^deleteAsset/([0-9]+$)', views.deleteAsset, name='deleteAsset'),
]
