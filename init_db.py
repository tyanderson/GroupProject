#!/user/bin/env python

# Initialize django
import os
import sys
import datetime
from decimal import Decimal
import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'GroupProject.settings'
django.setup()

import GroupProject3.models as bmod
from django.db import connection
import subprocess
from django.contrib.auth.models import User


# DROP DATABASE, RECREATE IT, THEN MIGRATE IT #

__author__ = 'Group1-3'
cursor = connection.cursor()
cursor.execute("PRAGMA writable_schema = 1;")
cursor.execute("delete from sqlite_master where type in ('table', 'index', 'trigger');")
subprocess.call([sys.executable, "manage.py", "migrate"])

# Create new user
user = User.objects.create_user('thefinestcatsintown', 'admin@admin.com', 'thefinestcatsintown')

# create location data
for data in [
    {'name':          'Seattle',
     'office_number': 1,},
    {'name':          'Austin',
     'office_number': 2,},
     {'name':          'San Jose',
     'office_number': 3,},
     {'name':          'New York City',
     'office_number': 4,},
     {'name':          'Hong Kong',
     'office_number': 5,},
    
]:

    a = bmod.location()
    for k, v in data.items():
        setattr(a, k, v)
    a.save()

print('Locations initialized')

# create manufacturer data
for data in [
    {'name':          'Apple',
     'hq_state': 'CA',
     'contact_phone': '1234567890',},
     {'name':          'Microsoft',
     'hq_state': 'WA',
     'contact_phone': '1234567890',},
     {'name':          'LG',
     'hq_state': 'UT',
     'contact_phone': '1234567890',},
     {'name':          'Samsung',
     'hq_state': 'NY',
     'contact_phone': '1234567890',},
     {'name':          'Sony',
     'hq_state': 'FL',
     'contact_phone': '1234567890',},
]:

    a = bmod.manufacturer()
    for k, v in data.items():
        setattr(a, k, v)
    a.save()

print('Manufacturer initialized')

# create organization data
for data in [
    {'name':          'Cody',
     'contact_phone': '1234567890',},
    {'name':          'Sean',
     'contact_phone': '1234567890',},
     {'name':          'Kevin',
     'contact_phone': '1234567890',},
     {'name':          'Ty',
     'contact_phone': '1234567890',},
     {'name':          'Tom',
     'contact_phone': '1234567890',},
    
]:

    a = bmod.organization()
    for k, v in data.items():
        setattr(a, k, v)
    a.save()

print('Organizations initialized')

# create asset data
for data in [
    {'name':          'Ethernet Cable',
    'location': bmod.location.objects.get(office_number = 1),
    'organization': bmod.organization.objects.get(name = 'Cody'),
    'manufacturer':   bmod.manufacturer.objects.get(name='Sony'),
    'part_number': 12,
    'description': 'Used to connect to the internet',
    'implemented': '2015-11-22',
    'notes': 'I found this on the ground so it must be good' },
    
    {'name':          'Cell Phone',
    'location': bmod.location.objects.get(office_number = 2),
    'organization': bmod.organization.objects.get(name = 'Kevin'),
    'manufacturer':   bmod.manufacturer.objects.get(name='Apple'),
    'part_number': 200,
    'description': 'Call people and surf the web',
    'implemented': '2015-11-22',
    'notes': 'Iphone 7S+'},
    
    {'name':          'Rubber Duckie',
     'location': bmod.location.objects.get(office_number = 3),
    'organization': bmod.organization.objects.get(name = 'Ty'),
    'manufacturer':   bmod.manufacturer.objects.get(name='Microsoft'),
    'part_number': 23,
    'description': 'Rubbie Duckie I love you',
    'implemented': '2015-11-22',
    'notes': 'Programmers use this to talk about their code'},
    
    {'name':          'Spatula',
     'location': bmod.location.objects.get(office_number = 4),
    'organization': bmod.organization.objects.get(name = 'Sean'),
    'manufacturer':   bmod.manufacturer.objects.get(name='LG'),
    'part_number': 32,
    'description': 'Used for burgers and pancakes',
    'implemented': '2015-11-22',
    'notes': 'Pancakes were made',},
    
    {'name':          'Waistcoat',
    'location': bmod.location.objects.get(office_number = 5),
    'organization': bmod.organization.objects.get(name = 'Tom'),
    'manufacturer':   bmod.manufacturer.objects.get(name='Samsung'),
    'part_number': 42,
    'description': 'Leftovers from CHF',
    'implemented': '2015-11-22',
    'notes': 'Oh Gove...'},
    
]:

    a = bmod.asset()
    for k, v in data.items():
        setattr(a, k, v)
    a.save()

print('Assets initialized')
