from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET


class xml_Importer(Importer):
    @staticmethod
    def csv(path):
        if path.split('.')[1] != 'xml':
            raise ValueError
        with open(path) as file:
            xml = ET.parse(file).getroot()
            return [
              {
                  prod.tag: prod.text for prod in product
              } for product in xml
            ]
