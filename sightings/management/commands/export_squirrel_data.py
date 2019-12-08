from django.core.management.base import BaseCommand, CommandError
import os
import csv
from sightings.models import Squirrel
import datetime


class Command(BaseCommand):
    def add_arguments(self,parser):
        parser.add_argument('csvfile')

    def handle(self, *args, **options):
        path = options['csvfile']
        fields = Squirrel._meta.fields
        with open(path, 'w') as csvFile:
            writer = csv.writer(csvFile)
            for object in Squirrel.objects.all():
                line =[]
                for field in fields:
                    line.append(getattr(object, field.name))
                writer.writerow(row)
                    
                    

                
                
                
