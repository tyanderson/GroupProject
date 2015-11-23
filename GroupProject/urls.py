from django.conf.urls import include, url
from django.contrib import admin
from GroupProject3 import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('GroupProject3.urls')),
    url(r'^addAsset/', views.addAsset, name='addAsset'),
]
