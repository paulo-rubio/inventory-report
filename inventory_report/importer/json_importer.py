from inventory_report.importer.importer import Importer
import json


class csv_Importer(Importer):
    @staticmethod
    def csv(path):
        if path.split('.')[1] != 'json':
            raise ValueError
        with open(path) as file:
            return json.load(file)
