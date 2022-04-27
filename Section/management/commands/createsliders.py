from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError

from Section.models import Slider

import csv
import codecs


class Command(BaseCommand):
    help = 'Initiate DB with slider csv file'

    def handle(self, *args, **options):
        sliders_path = 'sliders.csv'
        with open(sliders_path, 'rb') as sliders_file:
            sliders_reader = csv.reader(codecs.iterdecode(sliders_file, 'utf-8'))
            sliders_header = next(sliders_reader)
            for row in sliders_reader:
                _object_dict = {key: value for key, value in zip(sliders_header, row)}
                try:
                    Slider.objects.create(**_object_dict)
                except:
                    pass