from Modulos import Linhas

def ver_arquivos():
    import pandas as pd
    df = pd.read_csv("ESTOQUE/Modulos/Banco de Dados/produtos.csv")
    df_sem_numeros = df.select_dtypes(include=['object'])
    print(df_sem_numeros)


def cdst_produto():
    import pandas as pd
    # IMPORTAÇÕES - PRONTO
    arquivo = "ESTOQUE/Modulos/Banco de Dados/produtos.csv"
    df = pd.read_csv(arquivo)
    numeros_linhas = len(df)
    gerando_id = numeros_linhas + 1
    id_produto = gerando_id
    # ID - PRODUTO
    nome_produto = str(input("\033[36mNome do Produto: \033[0m"))
    # NOME PRODUTO - PRONTO
    desc_produto = str(input("\033[36mDescrição do Produro: \033[0m"))
    # DESCRIÇÃO PRODUTO - PRONTO
    while True:
        try:
            qntd_produto = int(input("\033[36mQuantidade do Produto: \033[0m"))
            if isinstance(qntd_produto, int):
                break
        except ValueError:
            print("\033[31mErro: Digite a Quantidade Em Números Validos!\033[0m")
    # QUANTIDADE PRODUTO - PRONTO
    while True:
        try:
            usuario_valor = str(input("\033[36mPreço do Produto:\033[0mR$"))
            usuario_valor_convertido = float(usuario_valor.replace(',', '.'))
            if isinstance(usuario_valor_convertido, float):
                break
        except ValueError:
            print("\033[31mErro: Digite o Preço Em Números Validos!\033[0m")
    # PREÇO PRODUTO - PRONTO
    adicionar = f'{id_produto},{nome_produto},{desc_produto},{qntd_produto},{usuario_valor_convertido}\n'
    nome_arquivo = "ESTOQUE/Modulos/Banco de Dados/produtos.csv"
    with open(nome_arquivo, mode='a') as arquivo:
        arquivo.write(adicionar)
    Linhas.linha_verde()
    p = "\033[92mProduto Cadastrado Com Sucesso!\033[0m"
    print(f"{p:^100}")
    Linhas.linha_verde()
    # ADICIONAR PRODUTO - PRONTO
