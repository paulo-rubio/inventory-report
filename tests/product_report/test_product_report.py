from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
      id=1,
      nome_do_produto='produtobonito',
      nome_da_empresa='INC',
      data_de_fabricacao='06/03/2023',
      data_de_validade='03/03/3023',
      numero_de_serie='2000',
      instrucoes_de_armazenamento='guardarbonito',
    )
    str = 'O produto produtobonito fabricado em 06/03/2023 por INC com'
    str2 = 'validade até 03/03/3023 precisa ser armazenado guardarbonito'

    assert repr(product) == f'{str} {str2}.'
