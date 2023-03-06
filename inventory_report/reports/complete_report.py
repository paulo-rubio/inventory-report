from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @staticmethod
    def __conty_company(report):
        company = Counter(prod['nome_da_empresa'] for prod in report)
        inf = ''

        for nameInc, qntVendas in company.items():
            inf += f' - {nameInc}: {qntVendas}\n'

        return f'Produtos estocados por empresa:\n {inf}'

    @classmethod
    def generate(cls, report) -> str:
        simple_report = super().generate(report)
        add_report = cls.__conty_company(report)
        return simple_report + '\n' + add_report
