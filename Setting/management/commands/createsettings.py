from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError

from Setting.models import ThemeSetting

import csv
import codecs


class Command(BaseCommand):
    help = 'Initiate DB with setting csv file'

    def handle(self, *args, **options):
        settings_path = 'settings.csv'
        with open(settings_path, 'rb') as settings_file:
            setting_reader = csv.reader(codecs.iterdecode(settings_file, 'utf-8'))
            setting_header = next(setting_reader)
            for row in setting_reader:
                _object_dict = {key: value for key, value in zip(setting_header, row)}
                setting_query = ThemeSetting.objects.find_by_name(_object_dict['name'])
                if not setting_query:
                    try:
                        ThemeSetting.objects.create(**_object_dict)
                    except:
                        _object_dict.pop('id')
                        ThemeSetting.objects.create(**_object_dict)
                else:
                    for data in _object_dict:
                        if data == "id":
                            pass
                        else:
                            setattr(setting_query, data, _object_dict[data])
                    setting_query.save()
