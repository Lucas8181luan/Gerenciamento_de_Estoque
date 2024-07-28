def ver_arquivos():
    import pandas as pd
    ler = pd.read_csv("ESTOQUE/Modulos/Produtos/produtos.csv")
    print(ler.head())


def cdst_produto():
    import pandas as pd
    # IMPORTAÇÕES - PRONTO
    arquivo = "ESTOQUE/Modulos/Produtos/produtos.csv"
    df = pd.read_csv(arquivo)
    numeros_linhas = len(df)
    gerando_id = numeros_linhas + 1
    id_produto = gerando_id
    # ID - PRODUTO
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
        try:
            usuario_valor = str(input("Preço do Produto:R$"))
            usuario_valor_convertido = float(usuario_valor.replace(',', '.'))
            if isinstance(usuario_valor_convertido, float):
                break
        except ValueError:
            print("\033[31mErro: Digite o Preço Em Números Validos!\033[0m")
    # PREÇO PRODUTO - PRONTO
    adicionar = f'{id_produto},{nome_produto},{desc_produto},{qntd_produto},{usuario_valor_convertido}\n'
    nome_arquivo = "ESTOQUE/Modulos/Produtos/produtos.csv"
    with open(nome_arquivo, mode='a') as arquivo:
        arquivo.write(adicionar)
    print("-" * 40)
    print("\033[92mProduto Cadastrado Com Sucesso!\033[0m")
    print("-" * 40)
    # ADICIONAR PRODUTO - PRONTO
