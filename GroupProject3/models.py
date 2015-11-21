from django.db import models
from django.contrib.localflavor.fr.forms import us


class location(models.Model):
    name = models.CharField(max_length=50)
    office_number = models.IntegerField()


class manufacturer(models.Model):
    name = models.CharField(max_length=50)
    hq_state = us.models.USStateField
    contact_phone = us.models.PhoneNumberField


class part(models.Model):
    name = models.CharField(max_length=50)
    manufacturer = models.ForeignKey(manufacturer)


class organization(models.Model):
    name = models.CharField(max_length=100)
    contact_phone = us.models.PhoneNumberField


class asset(models.Model):
    location = models.ForeignKey(location)
    organization = models.ForeignKey(organization)
    manufacturer = models.ForeignKey(manufacturer)
    part = models.ForeignKey(manufacturer)
    description = models.CharField(max_length=400)
    implemented = models.DateField(auto_now=True)
    notes = models.CharField(max_length=400)
