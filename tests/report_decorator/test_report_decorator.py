from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.importer.csv_importer import csv_Importer


def test_decorar_relatorio():
    path = 'inventory_report/data/inventory.csv'
    product = csv_Importer.import_data(path)
    collor_simple = ColoredReport(SimpleReport).generate(product)
    collor_complete = ColoredReport(CompleteReport).generate(product)
    collors = ["\033[36m", "\033[32m", "\033[31m"]

    for collor in collors:
        assert (collor in collor_simple) is True
        assert (collor in collor_complete) is True
