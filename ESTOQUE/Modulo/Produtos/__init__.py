def ver_arquivos():
    import pandas as pd
    ler = pd.read_csv("ESTOQUE/Modulo/Produtos/produtos.xlsx")
    print(ler.head())


def cdst_produto():
    nome_produto = str(input("Nome do Produto: "))
    # NOME PRODUTO - PRONTO
    desc_produto = str(input("Descrição do Produro: "))
    # DESCRIÇÃO PRODUTO - PRONTO
    while True:
        try:
            qntd_produto = int(input("Quantidade do Produto: "))
            if isinstance(qntd_produto, int):
                break
        except ValueError:
            print("\033[31mErro: Digite a Quantidade Em Números Validos!\033[0m")
    # QUANTIDADE PRODUTO - PRONTO
    while True:
        import locale
        try:
            usuario_valor = str(input("Preço do Produto:R$"))
            usuario_valor_convertido = float(usuario_valor.replace(',', '.'))
            locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
            valor = usuario_valor_convertido
            preço_produto = locale.currency(valor, symbol=True, grouping=True)
            if isinstance(usuario_valor_convertido, float):
                break
        except ValueError:
            print("\033[31mErro: Digite o Preço Em Números Validos!\033[0m")
    # PREÇO PRODUTO - PRONTO
    adicionar = f'{nome_produto},{desc_produto},{qntd_produto},{preço_produto}\n'
    nome_arquivo = "ESTOQUE/Modulo/Produtos/produtos.xlsx"
    with open(nome_arquivo, mode='a') as arquivo:
        arquivo.write(adicionar)
    print("-" * 40)
    print("\033[92mProduto Cadastrado Com Sucesso!\033[0m")
    print("-" * 40)
    # ADICIONAR PRODUTO - PRONTO
