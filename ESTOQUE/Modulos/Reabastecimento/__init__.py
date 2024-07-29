def ver_reabastecimento():
    import pandas as pd
    df = pd.read_csv("ESTOQUE/Modulos/Banco de Dados/Reabastecimento.csv")
    print(df.to_string(index=False))
