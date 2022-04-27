from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError

from Product.models import Products

import csv
import codecs


class Command(BaseCommand):
    help = 'Initiate DB with product csv file'

    def handle(self, *args, **options):
        products_path = 'products.csv'
        with open(products_path, 'rb') as products_file:
            product_reader = csv.reader(codecs.iterdecode(products_file, 'utf-8'))
            product_header = next(product_reader)
            for row in product_reader:
                _object_dict = {key: value for key, value in zip(product_header, row)}
                product_query = Products.objects.find_by_name(_object_dict['name'])
                if not product_query:
                    try:
                        Products.objects.create(**_object_dict)
                    except:
                        _object_dict.pop('id')
                        Products.objects.create(**_object_dict)
                else:
                    for data in _object_dict:
                        if data == "id":
                            pass
                        else:
                            setattr(product_query, data, _object_dict[data])
                    product_query.save()
