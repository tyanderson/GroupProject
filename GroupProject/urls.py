from django.conf.urls import include, url
from django.contrib import admin
from GroupProject3 import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^GroupProject3/', include('GroupProject3.urls')),
]
