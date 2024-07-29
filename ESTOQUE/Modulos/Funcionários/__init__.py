def ver_funcionários():
    import pandas as pd
    df = pd.read_csv("ESTOQUE/Modulos/Banco de Dados/Funcionários.csv")
    print(df.to_string(index=False))
