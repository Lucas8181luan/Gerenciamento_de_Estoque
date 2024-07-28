def grafico():
    import pandas as pd
    import matplotlib.pyplot as plt
    # IMPOTAÇÕES - PRONTO
    arquivo = "ESTOQUE/Modulos/Banco de Dados/produtos.csv"
    df = pd.read_csv(arquivo)
    numeros_linhas = len(df)
    ids = []
    for i in range(numeros_linhas + 1):
        ids.append(i)
    # IDS - PRONTO
    nomes_produtos = df["Nome"]
    nomes = nomes_produtos.tolist()
    nomes_pdts = []
    for i in nomes:
        nomes_pdts.append(i)
    # NOMES - PRONTO
    nomes_produtos = df["Quantidade"]
    nomes = nomes_produtos.tolist()
    Quantidade_pdts = []
    for i in nomes:
        Quantidade_pdts.append(i)
    # QUANTIDADES - PRONTO
    data = {
        "ID": [ids],
        "Nome": [nomes_pdts],
        "Quantidade": [Quantidade_pdts]
    }
    df_dt = pd.DataFrame(data)
    # DADOS FORNECIDOS - PRONTO
    plt.figure(figsize=(5, 4)) 
    plt.bar(df['Nome'], df['Quantidade'], color='skyblue')
    # DADOS PARA O GRÁFICO - PRONTO
    plt.title('Quantidade de Produtos em Estoque')
    plt.xlabel('Nome do Produto')
    plt.ylabel('Quantidade')
    # TITULOS PARA O GRÁFICO - PRONTO
    plt.xticks(rotation=90)
    plt.tight_layout() 
    plt.show()
    # EXIBIR O GRÁFICO - PRONTO
