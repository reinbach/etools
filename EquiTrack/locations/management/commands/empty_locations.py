__author__ = 'nikolatrncic'
from django.db import connection

from users.models import Country
from locations.models import Location
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        countries = Country.objects.exclude(name='Global')
        for country in countries:
            connection.set_tenant(country)
            print 'Country {}:'.format(country)
            empty_locs = Location.objects.values('name').filter(point__isnull=True, geom__isnull=True)
            for eloc in empty_locs:
                print eloc['name']



