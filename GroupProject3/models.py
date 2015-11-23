from django.db import models
from localflavor.us.models import PhoneNumberField, USStateField


class location(models.Model):
    name = models.CharField(max_length=50)
    office_number = models.IntegerField()


class manufacturer(models.Model):
    name = models.CharField(max_length=50)
    hq_state = USStateField()
    contact_phone = PhoneNumberField()


class organization(models.Model):
    name = models.CharField(max_length=100)
    contact_phone = PhoneNumberField()


class asset(models.Model):
    name = models.CharField(max_length=50)
    location = models.ForeignKey(location)
    organization = models.ForeignKey(organization)
    manufacturer = models.ForeignKey(manufacturer)
    description = models.TextField()
    implemented = models.DateField()
    notes = models.TextField()
