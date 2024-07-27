def ver_arquivos():
    import pandas as pd
    ler = pd.read_csv("ESTOQUE/Modulo/Produtos/produtos.xlsx")
    print(ler.head())
