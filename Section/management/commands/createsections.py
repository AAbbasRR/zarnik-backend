from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError

from Section.models import Sections

import csv
import codecs


class Command(BaseCommand):
    help = 'Initiate DB with section csv file'

    def handle(self, *args, **options):
        sections_path = 'sections.csv'
        with open(sections_path, 'rb') as sections_file:
            section_reader = csv.reader(codecs.iterdecode(sections_file, 'utf-8'))
            section_header = next(section_reader)
            for row in section_reader:
                _object_dict = {key: value for key, value in zip(section_header, row)}
                section_query = Sections.objects.find_by_name(_object_dict['name'])
                if not section_query:
                    try:
                        Sections.objects.create(**_object_dict)
                    except:
                        _object_dict.pop('id')
                        Sections.objects.create(**_object_dict)
                else:
                    for data in _object_dict:
                        if data == "id":
                            pass
                        else:
                            setattr(section_query, data, _object_dict[data])
                    section_query.save()
