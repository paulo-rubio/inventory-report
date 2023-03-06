from datetime import datetime
from collections import Counter

# tive que separar os methodos pois estavam dando erros


class SimpleReport:
    @staticmethod
    def __get_most_vender_item(report):
        empresa = Counter(product["nome_da_empresa"] for product in report)
        return empresa.most_common(1)[0][0]

    @staticmethod
    def __get_vali_item(report):
        old_date = min(
            [prod["data_de_fabricacao"] for prod in report])
        max_date = min([
            prod["data_de_validade"] for prod in report if datetime.strptime(
                prod["data_de_validade"],
                '%Y-%m-%d') > datetime.now()])
        return (old_date, max_date)

    @staticmethod
    def generate(report) -> str:
        data = SimpleReport.__get_vali_item(report)
        mostVenderCompany = SimpleReport.__get_most_vender_item(report)
        old_date, max_date = data

        return (
            f'Data de fabricação mais antiga: {old_date}\n'
            f'Data de validade mais próxima: {max_date}\n'
            f'Empresa com mais produtos: {mostVenderCompany}\n'
        )
