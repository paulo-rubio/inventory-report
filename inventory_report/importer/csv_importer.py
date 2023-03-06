from inventory_report.importer.importer import Importer
import csv


class csv_Importer(Importer):
    @staticmethod
    def csv(path):
        if path.split('.')[1] != 'csv':
            raise ValueError
        with open(path) as file:
            return list(csv.DictReader(file))
